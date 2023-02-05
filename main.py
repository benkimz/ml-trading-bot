import os
import io
import time
import binance
import json
import asyncio
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import matplotlib.pyplot as plt
from utils.klines_api import *
from utils.bot_utils import *
from utils.binance_api import *

STOCKS_DIR, MODELS_DIR, HISTORY_DIR= "stocks/", "models/ai-", "logs/"

WINDOW_LENGTH = 60

def data_file(filename=None):
    return str(filename) + ".csv"

def model_file(filename=None):
    return str(filename) + ".h5"

class BotException:
    def invalidEntries(description=''):
        return f"{description}"
    def modelLoading(description=''):
        return f"{description}"
    def botLearning(description=''):
        return f"{description}"
    def forecastLoop(description=''):
        return f"{description}"
    def insufficientBalance(description=''):
        return f"{description}"
    def spotUnsupported(description=''):
        return f"{description}"  

ds_loader = PriceData()
LOGIN_TIMESTAMP = time.time()

def pred_to_history(value=None):
    if value == None:
        return False
    else:
        try:
            value = float(value)
            if os.path.exists(HISTORY_DIR+"history.log"):
                f = io.open(HISTORY_DIR+"history.log", mode="a", encoding="UTF-8")
            else:
                f = io.open(HISTORY_DIR+"history.log", mode="w", encoding="UTF-8")
            f.write(str(value)+"\n")
            f.close()
            return True
        except Exception as error:
            return False
        
class BotTrader:
    def one_step_predict(self, default_steps=1):
        ready = True
        if self.model_ready == False:
            return False
        
        if os.path.exists(data_file(self.symbol)):
            if not trash_file(STOCKS_DIR+data_file(self.symbol)):
                ready = False

        price_data = PriceUpdates(
                filename = STOCKS_DIR+data_file(self.symbol), 
                symbol = self.symbol, 
                limit = 1000, 
                interval = 1, 
                interval_units = "m"
            )
        if not price_data.refresh() == True:
            ready = False
            
        if ready == False:
            return False
        elif ready == True:
            latest_data = ds_loader.load_price_data(STOCKS_DIR+data_file(self.symbol))
            if type(latest_data) == 'bool':
                print("--from -@-bot- unable to load latest_price-data: {main}")
                return False
            else:
                history = latest_data[-(WINDOW_LENGTH * default_steps):].values
                history = ds_loader.normalizer.transform(history)
                window_length_slices = np.array(np.split(history, default_steps))
                try:
                    predictions = self.model.predict(window_length_slices)
                    predictions = ds_loader.normalizer.inverse_transform(predictions)
                    prediction_frame = parse_outputs(predictions)
                    custom_forecast = float(np.mean([prediction_frame.mean().mean(), prediction_frame.mean()["close"]]))
                    return custom_forecast
                except Exception as fatalError:
                    print(f"\n--warning-from--bot: a problem occured while try to make a prediction. |help|--> {fatalError}\n\n")
                    return False
    
    def learn(self, summary=True, silent=False):
        ready = True
        if os.path.exists(data_file(self.symbol)):
            if not trash_file(STOCKS_DIR+data_file(self.symbol)):
                ready = False

        price_data = PriceUpdates(
                filename = STOCKS_DIR+data_file(self.symbol), 
                symbol = self.symbol, 
                limit = 1000, 
                interval = 1, 
                interval_units = "m"
            )
        if not price_data.refresh() == True:
            ready = False
        if ready == True:
            if silent == False:
                print("--@-bot--preparing to learn...\n")
            try:
                x_train, y_train, x_test, y_test = ds_loader.load_dataset(
                        filename = STOCKS_DIR+data_file(self.symbol), 
                        interval_window = WINDOW_LENGTH, 
                        validation_split = 0.2                
                    )
                if os.path.exists(model_file(MODELS_DIR+self.symbol)) == True:
                    try:
                        if silent == False:
                            print("--@bot--relearning in a few...")
                        this_model = tf.keras.models.load_model(filepath=model_file(MODELS_DIR+self.symbol))
                    except:
                        this_model = PriceAnalyst(x_train.shape[1:], f"AI...{self.symbol}....PAIR..PRICE..FORECASTER..MODEL")
                else:
                    this_model = PriceAnalyst(x_train.shape[1:], f"AI...{self.symbol}....PAIR..PRICE..FORECASTER..MODEL")
                if summary == True:
                    this_model.summary()
                this_model.compile(
                        optimizer = tf.keras.optimizers.Adam(learning_rate=0.00178125),
                        loss = "mean_squared_error"
                    )
                if silent == False:
                    print("--learning...\n")
                this_model.fit(
                        x_train,
                        y_train,
                        batch_size = 64,
                        epochs = 50,
                        verbose = 0,
                        callbacks = [AnalystCallbacks]
                    )
                this_model.save(model_file(MODELS_DIR+self.symbol))
                if silent == False:
                    print("\n", "-"*20,"done training-->", "-"*20, "\n")
                return True
            except Exception as error:
                print("from --bot: I got a problem gathering price data csv file", error)
                return False
    
    def __init__(self, base_asset="BTC", quote_asset="USDT"):
        self.symbol = str(base_asset) + str(quote_asset)
        self.base_asset = base_asset
        self.quote_asset = quote_asset
        self.model_ready = True
        if not self.learn(summary=False) == True:
            self.model_ready = False
        else:
            self.model = tf.keras.models.load_model(filepath=model_file(MODELS_DIR+self.symbol))
            self.model_ready = True



class BotSession(BotTrader):
    async def get_notional(self):
            if TESTNET == True:
                user = await AsyncClient.create(api_key=TESTNET_API_KEY, api_secret=TESTNET_API_SECRET, testnet=True)
            else:
                user = await AsyncClient.create(api_key=API_KEY, api_secret=API_SECRET, testnet=False)
                
            symbol_info = await user.get_symbol_info(self.symbol)
            await user.close_connection()
            notional_value = 0
            if symbol_info["isSpotTradingAllowed"] == True:
                base_asset_precision = int(symbol_info["baseAssetPrecision"])
                quantity, maxQty, minQty, minPrice, maxPrice, tickSize = 0, 0, 0, 0, 0, 0
                for pfilter in symbol_info["filters"]:
                    if pfilter["filterType"] == "MIN_NOTIONAL":
                        notional_value = float(pfilter["minNotional"])
                return notional_value
            else:
                raise Warning(BotException.spotUnsupported("This pair is cannot be traded on spot"))
                
                        
        
    def test_iterator(self, valid_margin=0.9):
        iterations, max_iterations = 0, 10
        test_prediction = self.one_step_predict(1)
        time.sleep(0.97)
        true_value = float(live_data(self.symbol))        
        while(True):
            try:
                if (test_prediction - true_value) > valid_margin or (true_value - test_prediction) > valid_margin:
                    if iterations >= max_iterations:
                        return False
                    self.learn(summary=False, silent=True)
                    iterations = iterations + 1
                    test_prediction = self.one_step_predict(1)
                    time.sleep(0.97)#MEANS I GIVE 300ms FOR BOT TO REALTIME DATA
                    true_value = float(live_data(self.symbol))
                else:
                    return True
            except:
                return False
                
                
    def __init__(self, base_asset=None, quote_asset=None):
        if base_asset == None or quote_asset == None:
            raise Warning(
                BotException.invalidEntries(
                    "Invalid arguments passed to BotSession(self, **args)"
                    )
                )
        else:
            super(BotSession, self).__init__(
                    base_asset=base_asset,
                    quote_asset=quote_asset
                )
            if self.model_ready == False:
                raise Warning(BotException.modelLoading("A problem occured while loading the model!"))
            self.loop = asyncio.get_event_loop()
            
            try:
                initial_balances = self.loop.run_until_complete(bal(base_asset, quote_asset))
            except:
                initial_balances = self.loop.create_task(bal(base_asset, quote_asset))
                
            base_balance, quote_balance = initial_balances
            initial_quote_balance = quote_balance
            print(
                    "\n",
                    f"STARTED A NEW SESSION FOR {self.symbol} PAIR {int(time.time())}\n",
                    "-"*50, "\n",
                    "***BALANCES***\n", "-"*30, "\n",
                    f"BASE ASSET: {base_balance}\n",
                    f"QUOTE ASSET: {quote_balance}\n",
                    "PROFITS: 0\n",
                    "-"*50, "\n"
                )
            PROFIT, NEW_BASE_BAL, NEW_QUOTE_BAL = 0, 0, 0
            PROFIT_MARGIN, LOSS_MARGIN = 0.125, 0.125
            POSITION = False
            ##################
            try:
                notional_value = self.loop.run_until_complete(self.get_notional())
            except:
                notional_value = self.loop.create_task(self.get_notional())
                
            if quote_balance < notional_value: #SHOULD ALWAYS START FROM QUOTE --just to be sure it doesn't sell for losses
                print(
                        "\n\n",
                        f"--bot- warning-- you have insufficient amount of {quote_asset}\n",
                        f"Minumum allowed is {notional_value}. Available is {quote_balance}\n",
                        f"--bot-exits session with command 0\n\n"
                    )
                return None
            ##################
            if self.test_iterator() == True:
                #KNOW THE INITIAL PRICE TO CREATE REFERENCE
                reference = float(live_data(self.symbol))
                iteration_count = 0
                while(True):
                    try:
                        prediction = self.one_step_predict(
                                default_steps=1
                            )
                        pred_to_history(prediction)
                        if POSITION == False and (prediction - reference) >= PROFIT_MARGIN:
                            try:
                                self.loop.run_until_complete(buy(base_asset, quote_asset, 'auto'))
                                base_balance, quote_balance = self.loop.run_until_complete(bal(base_asset, quote_asset))
                            except:
                                self.loop.create_task(buy(base_asset, quote_asset, 'auto'))
                                base_balance, quote_balance = self.loop.create_task(bal(base_asset, quote_asset))
                                
                            print(
                                    "\n",
                                    f"NEW BASE BALANCE: {base_balance}\n",
                                    f"NEW QUOTE BALANCE: {quote_balance}\n",
                                    f"CUMMULATIVE PROFITS: {PROFIT}\n"
                                )
                            POSITION = True
                            reference = float(live_data(self.symbol))
                            iteration_count = iteration_count + 1
                            
                        elif POSITION == True and (reference - prediction) >= LOSS_MARGIN:
                            try:
                                self.loop.run_until_complete(sell(base_asset, quote_asset, 'auto'))
                                base_balance, quote_balance = self.loop.run_until_complete(bal(base_asset, quote_asset))
                            except:
                                self.loop.create_task(sell(base_asset, quote_asset, 'auto'))
                                base_balance, quote_balance = self.loop.create_task(bal(base_asset, quote_asset))
                                
                            print(
                                    "\n",
                                    f"NEW BASE BALANCE: {base_balance}\n",
                                    f"NEW QUOTE BALANCE: {quote_balance}\n",
                                    f"CUMMULATIVE PROFITS: {PROFIT}\n"
                                )
                            POSITION = False
                            PROFIT = PROFIT + (quote_balance - initial_quote_balance)
                            reference = float(live_data(self.symbol))
                            iteration_count = iteration_count + 1

                        if iteration_count >= 4:
                            if not self.test_iterator() == True:
                                raise Warning(BotException.botLearning("The curve for this pair is so tough for Mr bot."))
                        if (float(time.time()) - LOGIN_TIMESTAMP) >= (60**2):#BREAK AFTER 1hr
                            print(
                                    "\n\n",
                                    "--bot-session....................\n",
                                    f"LAST LOGIN: {LOGIN_TIMESTAMP}, CURRENT_STAMP: {int(time.time())}"
                                    "TAKING A BREAK, CONTINUE WITH SESSION?\n",
                                )
                            user_response = input()
                            try:
                                if str(user_response).lower() == "y" or str(user_response).lower() == "yes" or str(user_response).lower() == "yeah":
                                    continue
                                else:
                                    break
                            except Exception as fatalerror:
                                print(
                                        "\n\n",
                                        f"FATAL ERROR!!! {fatalerror}\n"
                                        "--bot-exits session with command 0\n"
                                    )
                                break
                            
                    except Exception as loopBreakDown:
                        print(
                                "\n\n",
                                "FATAL ERROR!!!\n"
                            )
                        raise Warning(BotException.forecastLoop("Forecast loop was interrupted"))
            else:
                raise Warning(BotException.botLearning("The curve for this pair is so tough for Mr bot."))


# Invoke a new trade session
trade_session = BotSession(base_asset="BNB", quote_asset="USDT")
