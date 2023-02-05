Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\benkimz\Documents\.AI-WORK-SPACE\bot-trader\trader-bot\draft\main.py
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=BNBUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001A25BBCCA90>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=BNBUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001A25BBCCBE0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=BNBUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001A25BBCC940>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
>>> 
= RESTART: C:\Users\benkimz\Documents\.AI-WORK-SPACE\bot-trader\trader-bot\draft\main.py
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 22s - loss: 0.0014 - 22s/epoch - 2s/step
Epoch 2/50
12/12 - 3s - loss: 6.0709e-04 - 3s/epoch - 271ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 18s - loss: 0.0015 - 18s/epoch - 2s/step
Epoch 2/50
12/12 - 5s - loss: 7.9738e-04 - 5s/epoch - 380ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 19s - loss: 0.0014 - 19s/epoch - 2s/step
Epoch 2/50
12/12 - 4s - loss: 6.2478e-04 - 4s/epoch - 359ms/step

 -------------------- done training--> -------------------- 




 Fast forecast:  387.56629180908203 



[{'openTime': 1651580580000, 'open': '387.70000000', 'high': '387.70000000', 'low': '387.60000000', 'close': '387.60000000', 'volume': '94.33300000', 'closeTime': 1651580639999, 'quoteVolume': '36563.61340000', 'numTrades': 41}]
high     387.687469
low      387.415039
open     387.519806
close    387.581604
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 387.58160400390625 
Bot concensus: 387.5611877441406

------------------------------ *************** ------------------------------ 




 Fast forecast:  387.64046478271484 



[{'openTime': 1651580580000, 'open': '387.70000000', 'high': '387.70000000', 'low': '387.50000000', 'close': '387.60000000', 'volume': '232.12400000', 'closeTime': 1651580639999, 'quoteVolume': '89971.25630000', 'numTrades': 78}]
high     387.758667
low      387.491333
open     387.595673
close    387.655609
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 387.6556091308594 
Bot concensus: 387.6354166666667

------------------------------ *************** ------------------------------ 




 Fast forecast:  387.64046478271484 



[{'openTime': 1651580580000, 'open': '387.70000000', 'high': '387.70000000', 'low': '387.50000000', 'close': '387.60000000', 'volume': '238.14900000', 'closeTime': 1651580639999, 'quoteVolume': '92306.54630000', 'numTrades': 90}]
high     387.758667
low      387.491333
open     387.595673
close    387.655609
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 387.6556091308594 
Bot concensus: 387.6354166666667

------------------------------ *************** ------------------------------ 




 Fast forecast:  387.64046478271484 



[{'openTime': 1651580580000, 'open': '387.70000000', 'high': '387.70000000', 'low': '387.50000000', 'close': '387.60000000', 'volume': '244.37700000', 'closeTime': 1651580639999, 'quoteVolume': '94720.17410000', 'numTrades': 102}]
high     387.758667
low      387.491333
open     387.595673
close    387.655609
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 387.6556091308594 
Bot concensus: 387.6354166666667

------------------------------ *************** ------------------------------ 




 Fast forecast:  387.64046478271484 



[{'openTime': 1651580580000, 'open': '387.70000000', 'high': '387.70000000', 'low': '387.50000000', 'close': '387.60000000', 'volume': '262.72600000', 'closeTime': 1651580639999, 'quoteVolume': '101830.58920000', 'numTrades': 113}]
high     387.758667
low      387.491333
open     387.595673
close    387.655609
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 387.6556091308594 
Bot concensus: 387.6354166666667

------------------------------ *************** ------------------------------ 

>>> for i in range(20):
	bot.learn(False)

	
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 21s - loss: 0.0014 - 21s/epoch - 2s/step
Epoch 2/50
12/12 - 5s - loss: 6.6649e-04 - 5s/epoch - 406ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 18s - loss: 0.0010 - 18s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 5.8209e-04 - 3s/epoch - 275ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0014 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 5s - loss: 6.7091e-04 - 5s/epoch - 382ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0016 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 7.6642e-04 - 4s/epoch - 307ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0018 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 7.3520e-04 - 4s/epoch - 339ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0014 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 6.5630e-04 - 4s/epoch - 333ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 18s - loss: 0.0013 - 18s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 5.5271e-04 - 4s/epoch - 350ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 17s - loss: 0.0015 - 17s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 6.7492e-04 - 4s/epoch - 327ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 15s - loss: 0.0014 - 15s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 7.2167e-04 - 4s/epoch - 323ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 20s - loss: 0.0016 - 20s/epoch - 2s/step
Epoch 2/50
12/12 - 4s - loss: 7.4539e-04 - 4s/epoch - 315ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 19s - loss: 0.0013 - 19s/epoch - 2s/step
Epoch 2/50
12/12 - 5s - loss: 5.9346e-04 - 5s/epoch - 429ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 19s - loss: 0.0013 - 19s/epoch - 2s/step
Epoch 2/50
12/12 - 4s - loss: 6.1238e-04 - 4s/epoch - 325ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 17s - loss: 0.0015 - 17s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 6.1701e-04 - 4s/epoch - 349ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 19s - loss: 0.0016 - 19s/epoch - 2s/step
Epoch 2/50
12/12 - 4s - loss: 7.3989e-04 - 4s/epoch - 366ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 18s - loss: 0.0012 - 18s/epoch - 2s/step
Epoch 2/50
12/12 - 4s - loss: 5.6869e-04 - 4s/epoch - 360ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 18s - loss: 0.0013 - 18s/epoch - 1s/step
Epoch 2/50
12/12 - 5s - loss: 6.7607e-04 - 5s/epoch - 435ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0014 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 7.3812e-04 - 4s/epoch - 329ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0011 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 6.2483e-04 - 4s/epoch - 344ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0013 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 6.4842e-04 - 4s/epoch - 300ms/step

 -------------------- done training--> -------------------- 

True
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 15s - loss: 8.5737e-04 - 15s/epoch - 1s/step

 -------------------- done training--> -------------------- 

True
>>> for i in range(20):
	bot.one_step_predict(1)

	



 Fast forecast:  388.19998931884766 



[{'openTime': 1651581240000, 'open': '387.90000000', 'high': '388.20000000', 'low': '387.90000000', 'close': '388.10000000', 'volume': '106.38300000', 'closeTime': 1651581299999, 'quoteVolume': '41274.26200000', 'numTrades': 98}]
high     388.310181
low      388.072235
open     388.178680
close    388.207764
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.207763671875 
Bot concensus: 388.19739786783856

------------------------------ *************** ------------------------------ 

388.19739786783856



 Fast forecast:  388.03789138793945 



[{'openTime': 1651581240000, 'open': '387.90000000', 'high': '388.20000000', 'low': '387.90000000', 'close': '388.10000000', 'volume': '181.82300000', 'closeTime': 1651581299999, 'quoteVolume': '70552.63330000', 'numTrades': 115}]
high     388.150604
low      387.903564
open     388.011841
close    388.047424
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.04742431640625 
Bot concensus: 388.0347137451172

------------------------------ *************** ------------------------------ 

388.0347137451172



 Fast forecast:  387.95683670043945 



[{'openTime': 1651581240000, 'open': '387.90000000', 'high': '388.20000000', 'low': '387.90000000', 'close': '387.90000000', 'volume': '217.89300000', 'closeTime': 1651581299999, 'quoteVolume': '84547.70560000', 'numTrades': 127}]
high     388.070801
low      387.819183
open     387.928436
close    387.967255
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 387.9672546386719 
Bot concensus: 387.953364054362

------------------------------ *************** ------------------------------ 

387.953364054362



 Fast forecast:  388.03789138793945 



[{'openTime': 1651581240000, 'open': '387.90000000', 'high': '388.20000000', 'low': '387.90000000', 'close': '388.00000000', 'volume': '220.54900000', 'closeTime': 1651581299999, 'quoteVolume': '85578.22400000', 'numTrades': 136}]
high     388.150604
low      387.903564
open     388.011841
close    388.047424
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.04742431640625 
Bot concensus: 388.0347137451172

------------------------------ *************** ------------------------------ 

388.0347137451172



 Fast forecast:  388.03789138793945 



[{'openTime': 1651581240000, 'open': '387.90000000', 'high': '388.20000000', 'low': '387.90000000', 'close': '388.10000000', 'volume': '221.25200000', 'closeTime': 1651581299999, 'quoteVolume': '85851.05830000', 'numTrades': 139}]
high     388.150604
low      387.903564
open     388.011841
close    388.047424
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.04742431640625 
Bot concensus: 388.0347137451172

------------------------------ *************** ------------------------------ 

388.0347137451172



 Fast forecast:  388.1189498901367 



[{'openTime': 1651581240000, 'open': '387.90000000', 'high': '388.20000000', 'low': '387.90000000', 'close': '388.10000000', 'volume': '225.99600000', 'closeTime': 1651581299999, 'quoteVolume': '87692.20470000', 'numTrades': 149}]
high     388.230408
low      387.987915
open     388.095306
close    388.127594
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.1275939941406 
Bot concensus: 388.11606852213544

------------------------------ *************** ------------------------------ 

388.11606852213544



 Fast forecast:  388.03789138793945 



[{'openTime': 1651581240000, 'open': '387.90000000', 'high': '388.20000000', 'low': '387.90000000', 'close': '388.10000000', 'volume': '226.84700000', 'closeTime': 1651581299999, 'quoteVolume': '88022.43310000', 'numTrades': 154}]
high     388.150604
low      387.903564
open     388.011841
close    388.047424
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.04742431640625 
Bot concensus: 388.0347137451172

------------------------------ *************** ------------------------------ 

388.0347137451172



 Fast forecast:  388.03789138793945 



[{'openTime': 1651581240000, 'open': '387.90000000', 'high': '388.20000000', 'low': '387.90000000', 'close': '388.10000000', 'volume': '228.73600000', 'closeTime': 1651581299999, 'quoteVolume': '88755.40090000', 'numTrades': 161}]
high     388.150604
low      387.903564
open     388.011841
close    388.047424
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.04742431640625 
Bot concensus: 388.0347137451172

------------------------------ *************** ------------------------------ 

388.0347137451172



 Fast forecast:  388.1189498901367 



[{'openTime': 1651581240000, 'open': '387.90000000', 'high': '388.20000000', 'low': '387.90000000', 'close': '388.00000000', 'volume': '231.58900000', 'closeTime': 1651581299999, 'quoteVolume': '89862.63690000', 'numTrades': 175}]
high     388.230408
low      387.987915
open     388.095306
close    388.127594
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.1275939941406 
Bot concensus: 388.11606852213544

------------------------------ *************** ------------------------------ 

388.11606852213544



 Fast forecast:  388.1189498901367 



[{'openTime': 1651581300000, 'open': '388.00000000', 'high': '388.10000000', 'low': '388.00000000', 'close': '388.10000000', 'volume': '2.89000000', 'closeTime': 1651581359999, 'quoteVolume': '1121.60520000', 'numTrades': 2}]
high     388.230408
low      387.987915
open     388.095306
close    388.127594
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.1275939941406 
Bot concensus: 388.11606852213544

------------------------------ *************** ------------------------------ 

388.11606852213544



 Fast forecast:  388.1196060180664 



[{'openTime': 1651581300000, 'open': '388.00000000', 'high': '388.20000000', 'low': '388.00000000', 'close': '388.10000000', 'volume': '23.01900000', 'closeTime': 1651581359999, 'quoteVolume': '8934.19530000', 'numTrades': 23}]
high     388.233398
low      387.990326
open     388.102173
close    388.126190
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.1261901855469 
Bot concensus: 388.11741129557294

------------------------------ *************** ------------------------------ 

388.11741129557294



 Fast forecast:  388.1209907531738 



[{'openTime': 1651581300000, 'open': '388.00000000', 'high': '388.20000000', 'low': '388.00000000', 'close': '388.10000000', 'volume': '25.93300000', 'closeTime': 1651581359999, 'quoteVolume': '10065.18250000', 'numTrades': 29}]
high     388.234619
low      387.991638
open     388.103394
close    388.127655
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.1276550292969 
Bot concensus: 388.1187693277995

------------------------------ *************** ------------------------------ 

388.1187693277995



 Fast forecast:  388.1209907531738 



[{'openTime': 1651581300000, 'open': '388.00000000', 'high': '388.20000000', 'low': '388.00000000', 'close': '388.20000000', 'volume': '49.29600000', 'closeTime': 1651581359999, 'quoteVolume': '19132.67610000', 'numTrades': 36}]
high     388.234619
low      387.991638
open     388.103394
close    388.127655
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.1276550292969 
Bot concensus: 388.1187693277995

------------------------------ *************** ------------------------------ 

388.1187693277995



 Fast forecast:  388.20165252685547 



[{'openTime': 1651581300000, 'open': '388.00000000', 'high': '388.20000000', 'low': '388.00000000', 'close': '388.20000000', 'volume': '56.37800000', 'closeTime': 1651581359999, 'quoteVolume': '21881.89420000', 'numTrades': 42}]
high     388.314026
low      388.075531
open     388.186371
close    388.207458
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.20745849609375 
Bot concensus: 388.19971720377606

------------------------------ *************** ------------------------------ 

388.19971720377606



 Fast forecast:  388.20165252685547 



[{'openTime': 1651581300000, 'open': '388.00000000', 'high': '388.20000000', 'low': '388.00000000', 'close': '388.20000000', 'volume': '60.53500000', 'closeTime': 1651581359999, 'quoteVolume': '23495.27040000', 'numTrades': 47}]
high     388.314026
low      388.075531
open     388.186371
close    388.207458
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.20745849609375 
Bot concensus: 388.19971720377606

------------------------------ *************** ------------------------------ 

388.19971720377606



 Fast forecast:  388.1209907531738 




= RESTART: C:\Users\benkimz\Documents\.AI-WORK-SPACE\bot-trader\trader-bot\draft\main.py
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0012 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 5.9835e-04 - 3s/epoch - 270ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0013 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 6.6439e-04 - 3s/epoch - 269ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0013 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 7.3755e-04 - 3s/epoch - 264ms/step

 -------------------- done training--> -------------------- 




 Fast forecast:  388.3595314025879 



[{'openTime': 1651581420000, 'open': '388.20000000', 'high': '388.40000000', 'low': '388.20000000', 'close': '388.40000000', 'volume': '99.00400000', 'closeTime': 1651581479999, 'quoteVolume': '38446.86680000', 'numTrades': 95}]
high     388.483582
low      388.252319
open     388.365295
close    388.355011
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.3550109863281 
Bot concensus: 388.3610382080078

------------------------------ *************** ------------------------------ 




 Fast forecast:  388.27810287475586 



[{'openTime': 1651581420000, 'open': '388.20000000', 'high': '388.40000000', 'low': '388.20000000', 'close': '388.30000000', 'volume': '104.15800000', 'closeTime': 1651581479999, 'quoteVolume': '40448.43420000', 'numTrades': 103}]
high     388.402222
low      388.168610
open     388.282990
close    388.274200
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.2742004394531 
Bot concensus: 388.27940368652344

------------------------------ *************** ------------------------------ 




 Fast forecast:  388.392147064209 



[{'openTime': 1651581480000, 'open': '388.40000000', 'high': '388.40000000', 'low': '388.30000000', 'close': '388.40000000', 'volume': '1.99800000', 'closeTime': 1651581539999, 'quoteVolume': '776.01290000', 'numTrades': 6}]
high     388.516113
low      388.284637
open     388.399933
close    388.387299
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.3872985839844 
Bot concensus: 388.3937632242839

------------------------------ *************** ------------------------------ 




 Fast forecast:  388.38400650024414 



[{'openTime': 1651581480000, 'open': '388.40000000', 'high': '388.40000000', 'low': '388.30000000', 'close': '388.40000000', 'volume': '3.33600000', 'closeTime': 1651581539999, 'quoteVolume': '1295.61010000', 'numTrades': 12}]
high     388.507874
low      388.276825
open     388.391754
close    388.379120
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.3791198730469 
Bot concensus: 388.38563537597656

------------------------------ *************** ------------------------------ 




 Fast forecast:  388.38400650024414 



[{'openTime': 1651581480000, 'open': '388.40000000', 'high': '388.50000000', 'low': '388.30000000', 'close': '388.50000000', 'volume': '275.24700000', 'closeTime': 1651581539999, 'quoteVolume': '106918.17380000', 'numTrades': 76}]
high     388.507874
low      388.276825
open     388.391754
close    388.379120
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.3791198730469 
Bot concensus: 388.38563537597656

------------------------------ *************** ------------------------------ 

>>> for i in range(10):
	bot.one_step_predict()

	



 Fast forecast:  388.2157211303711 



[{'openTime': 1651581480000, 'open': '388.40000000', 'high': '388.50000000', 'low': '388.20000000', 'close': '388.20000000', 'volume': '697.20800000', 'closeTime': 1651581539999, 'quoteVolume': '270787.17850000', 'numTrades': 196}]
high     388.339661
low      388.104248
open     388.221375
close    388.212097
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.21209716796875 
Bot concensus: 388.21692911783856

------------------------------ *************** ------------------------------ 

388.21692911783856



 Fast forecast:  388.2157211303711 



[{'openTime': 1651581480000, 'open': '388.40000000', 'high': '388.50000000', 'low': '388.10000000', 'close': '388.20000000', 'volume': '800.22900000', 'closeTime': 1651581539999, 'quoteVolume': '310777.57360000', 'numTrades': 217}]
high     388.339661
low      388.104248
open     388.221375
close    388.212097
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.21209716796875 
Bot concensus: 388.21692911783856

------------------------------ *************** ------------------------------ 

388.21692911783856



 Fast forecast:  388.2076759338379 



[{'openTime': 1651581540000, 'open': '388.10000000', 'high': '388.20000000', 'low': '388.10000000', 'close': '388.20000000', 'volume': '5.91400000', 'closeTime': 1651581599999, 'quoteVolume': '2295.80930000', 'numTrades': 10}]
high     388.331543
low      388.096527
open     388.213287
close    388.204010
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.2040100097656 
Bot concensus: 388.2088979085286

------------------------------ *************** ------------------------------ 

388.2088979085286



 Fast forecast:  388.1650733947754 



[{'openTime': 1651581540000, 'open': '388.10000000', 'high': '388.20000000', 'low': '388.10000000', 'close': '388.10000000', 'volume': '6.58000000', 'closeTime': 1651581599999, 'quoteVolume': '2554.31950000', 'numTrades': 12}]
high     388.288940
low      388.053192
open     388.171112
close    388.161469
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.1614685058594 
Bot concensus: 388.16627502441406

------------------------------ *************** ------------------------------ 

388.16627502441406



 Fast forecast:  388.1650733947754 



[{'openTime': 1651581540000, 'open': '388.10000000', 'high': '388.20000000', 'low': '388.10000000', 'close': '388.10000000', 'volume': '258.61800000', 'closeTime': 1651581599999, 'quoteVolume': '100370.45820000', 'numTrades': 46}]
high     388.288940
low      388.053192
open     388.171112
close    388.161469
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.1614685058594 
Bot concensus: 388.16627502441406

------------------------------ *************** ------------------------------ 

388.16627502441406



 Fast forecast:  388.08387756347656 



[{'openTime': 1651581540000, 'open': '388.10000000', 'high': '388.20000000', 'low': '388.10000000', 'close': '388.10000000', 'volume': '268.73000000', 'closeTime': 1651581599999, 'quoteVolume': '104294.95620000', 'numTrades': 63}]
high     388.207794
low      387.969604
open     388.089111
close    388.080902
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.0809020996094 
Bot concensus: 388.0848693847656

------------------------------ *************** ------------------------------ 

388.0848693847656



 Fast forecast:  388.07595443725586 



[{'openTime': 1651581540000, 'open': '388.10000000', 'high': '388.20000000', 'low': '388.00000000', 'close': '388.10000000', 'volume': '281.70300000', 'closeTime': 1651581599999, 'quoteVolume': '109329.49040000', 'numTrades': 67}]
high     388.199768
low      387.962036
open     388.081146
close    388.072937
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.07293701171875 
Bot concensus: 388.07696024576825

------------------------------ *************** ------------------------------ 

388.07696024576825



 Fast forecast:  388.07595443725586 



[{'openTime': 1651581540000, 'open': '388.10000000', 'high': '388.20000000', 'low': '388.00000000', 'close': '388.10000000', 'volume': '294.47000000', 'closeTime': 1651581599999, 'quoteVolume': '114283.32310000', 'numTrades': 78}]
high     388.199768
low      387.962036
open     388.081146
close    388.072937
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.07293701171875 
Bot concensus: 388.07696024576825

------------------------------ *************** ------------------------------ 

388.07696024576825



 Fast forecast:  388.07595443725586 



[{'openTime': 1651581540000, 'open': '388.10000000', 'high': '388.20000000', 'low': '388.00000000', 'close': '388.10000000', 'volume': '352.53100000', 'closeTime': 1651581599999, 'quoteVolume': '136811.21690000', 'numTrades': 97}]
high     388.199768
low      387.962036
open     388.081146
close    388.072937
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.07293701171875 
Bot concensus: 388.07696024576825

------------------------------ *************** ------------------------------ 

388.07696024576825



 Fast forecast:  387.9948196411133 



[{'openTime': 1651581540000, 'open': '388.10000000', 'high': '388.20000000', 'low': '388.00000000', 'close': '388.10000000', 'volume': '356.37800000', 'closeTime': 1651581599999, 'quoteVolume': '138303.96250000', 'numTrades': 105}]
high     388.118713
low      387.878510
open     387.999176
close    387.992432
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 387.992431640625 
Bot concensus: 387.99561564127606

------------------------------ *************** ------------------------------ 

387.99561564127606
>>> bot.learn(False)
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 15s - loss: 0.0013 - 15s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 6.6992e-04 - 3s/epoch - 277ms/step

 -------------------- done training--> -------------------- 

True
>>> for i range(5):
	
SyntaxError: invalid syntax
>>> for i in range(5):
	bot.one_step_predict(1)

	



 Fast forecast:  388.1861877441406 



[{'openTime': 1651581600000, 'open': '388.20000000', 'high': '388.30000000', 'low': '388.10000000', 'close': '388.10000000', 'volume': '153.73900000', 'closeTime': 1651581659999, 'quoteVolume': '59683.11440000', 'numTrades': 123}]
high     388.308685
low      388.073151
open     388.190765
close    388.183380
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.1833801269531 
Bot concensus: 388.18712361653644

------------------------------ *************** ------------------------------ 

388.18712361653644



 Fast forecast:  388.1781463623047 



[{'openTime': 1651581600000, 'open': '388.20000000', 'high': '388.30000000', 'low': '388.10000000', 'close': '388.20000000', 'volume': '157.84600000', 'closeTime': 1651581659999, 'quoteVolume': '61277.12620000', 'numTrades': 130}]
high     388.300568
low      388.065460
open     388.182678
close    388.175293
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.17529296875 
Bot concensus: 388.17909749348956

------------------------------ *************** ------------------------------ 

388.17909749348956



 Fast forecast:  388.2452735900879 



[{'openTime': 1651581660000, 'open': '388.10000000', 'high': '388.30000000', 'low': '388.10000000', 'close': '388.30000000', 'volume': '92.04000000', 'closeTime': 1651581719999, 'quoteVolume': '35725.59270000', 'numTrades': 53}]
high     388.367554
low      388.134644
open     388.250427
close    388.241913
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.2419128417969 
Bot concensus: 388.24639383951825

------------------------------ *************** ------------------------------ 

388.24639383951825



 Fast forecast:  388.0826530456543 



[{'openTime': 1651581660000, 'open': '388.10000000', 'high': '388.30000000', 'low': '388.10000000', 'close': '388.10000000', 'volume': '104.41300000', 'closeTime': 1651581719999, 'quoteVolume': '40527.95630000', 'numTrades': 64}]
high     388.205078
low      387.967316
open     388.086151
close    388.080536
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.0805358886719 
Bot concensus: 388.08335876464844

------------------------------ *************** ------------------------------ 

388.08335876464844



 Fast forecast:  388.16397857666016 



[{'openTime': 1651581660000, 'open': '388.10000000', 'high': '388.30000000', 'low': '388.10000000', 'close': '388.20000000', 'volume': '109.24000000', 'closeTime': 1651581719999, 'quoteVolume': '42401.79360000', 'numTrades': 72}]
high     388.286316
low      388.050964
open     388.168274
close    388.161255
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BNBUSDT forecasting model

Model prediction: 388.1612548828125 
Bot concensus: 388.1648864746094

------------------------------ *************** ------------------------------ 

388.1648864746094
>>> 
= RESTART: C:\Users\benkimz\Documents\.AI-WORK-SPACE\bot-trader\trader-bot\draft\main.py
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 15s - loss: 0.0024 - 15s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 262ms/step
Epoch 3/50
12/12 - 3s - loss: 9.0111e-04 - 3s/epoch - 264ms/step

 -------------------- done training--> -------------------- 

Fatal error! Could not refresh previous data! ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=BTCUSDT&interval=1m&limit=1000 (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1123)')))
Fatal error! Could not refresh previous data! ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 15s - loss: 0.0027 - 15s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 269ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 266ms/step
Epoch 4/50
12/12 - 3s - loss: 8.7132e-04 - 3s/epoch - 276ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 17s - loss: 0.0023 - 17s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 0.0011 - 4s/epoch - 365ms/step
Epoch 3/50
12/12 - 5s - loss: 8.1022e-04 - 5s/epoch - 383ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 18s - loss: 0.0023 - 18s/epoch - 2s/step
Epoch 2/50
12/12 - 4s - loss: 0.0011 - 4s/epoch - 339ms/step
Epoch 3/50
12/12 - 4s - loss: 9.4197e-04 - 4s/epoch - 315ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0023 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 272ms/step
Epoch 3/50
12/12 - 4s - loss: 8.0902e-04 - 4s/epoch - 315ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 18s - loss: 0.0021 - 18s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 0.0011 - 4s/epoch - 307ms/step
Epoch 3/50
12/12 - 4s - loss: 8.9204e-04 - 4s/epoch - 303ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 17s - loss: 0.0023 - 17s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 0.0010 - 4s/epoch - 295ms/step
Epoch 3/50
12/12 - 4s - loss: 7.5392e-04 - 4s/epoch - 306ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 18s - loss: 0.0015 - 18s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 8.0135e-04 - 3s/epoch - 271ms/step

 -------------------- done training--> -------------------- 




 Fast forecast:  38489.3486328125 



[{'openTime': 1651582380000, 'open': '38470.97000000', 'high': '38486.64000000', 'low': '38470.96000000', 'close': '38486.64000000', 'volume': '6.10916000', 'closeTime': 1651582439999, 'quoteVolume': '235085.12696500', 'numTrades': 390}]
high     38499.199219
low      38478.210938
open     38487.925781
close    38489.890625
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38489.890625 
Bot concensus: 38489.16796875

------------------------------ *************** ------------------------------ 




 Fast forecast:  38489.3486328125 



[{'openTime': 1651582380000, 'open': '38470.97000000', 'high': '38486.64000000', 'low': '38470.96000000', 'close': '38486.64000000', 'volume': '7.10003000', 'closeTime': 1651582439999, 'quoteVolume': '273220.37554430', 'numTrades': 426}]
high     38499.199219
low      38478.210938
open     38487.925781
close    38489.890625
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38489.890625 
Bot concensus: 38489.16796875

------------------------------ *************** ------------------------------ 




 Fast forecast:  38489.3486328125 



[{'openTime': 1651582380000, 'open': '38470.97000000', 'high': '38486.64000000', 'low': '38470.96000000', 'close': '38486.64000000', 'volume': '7.29076000', 'closeTime': 1651582439999, 'quoteVolume': '280560.93149990', 'numTrades': 456}]
high     38499.199219
low      38478.210938
open     38487.925781
close    38489.890625
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38489.890625 
Bot concensus: 38489.16796875

------------------------------ *************** ------------------------------ 




 Fast forecast:  38489.3486328125 



[{'openTime': 1651582380000, 'open': '38470.97000000', 'high': '38486.64000000', 'low': '38470.96000000', 'close': '38486.64000000', 'volume': '7.83067000', 'closeTime': 1651582439999, 'quoteVolume': '301340.25153810', 'numTrades': 498}]
high     38499.199219
low      38478.210938
open     38487.925781
close    38489.890625
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38489.890625 
Bot concensus: 38489.16796875

------------------------------ *************** ------------------------------ 




 Fast forecast:  38489.3486328125 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38489.40000000', 'low': '38486.63000000', 'close': '38489.39000000', 'volume': '0.92891000', 'closeTime': 1651582499999, 'quoteVolume': '35751.46340410', 'numTrades': 82}]
high     38499.199219
low      38478.210938
open     38487.925781
close    38489.890625
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38489.890625 
Bot concensus: 38489.16796875

------------------------------ *************** ------------------------------ 




 Fast forecast:  38495.640625 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38489.40000000', 'low': '38486.63000000', 'close': '38489.40000000', 'volume': '1.27165000', 'closeTime': 1651582499999, 'quoteVolume': '48943.31902290', 'numTrades': 131}]
high     38505.839844
low      38484.613281
open     38494.300781
close    38496.074219
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38496.07421875 
Bot concensus: 38495.49609375

------------------------------ *************** ------------------------------ 




 Fast forecast:  38495.64501953125 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38493.44000000', 'low': '38486.63000000', 'close': '38493.43000000', 'volume': '2.27211000', 'closeTime': 1651582499999, 'quoteVolume': '87451.84463000', 'numTrades': 196}]
high     38505.843750
low      38484.621094
open     38494.304688
close    38496.078125
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38496.078125 
Bot concensus: 38495.500651041664

------------------------------ *************** ------------------------------ 




 Fast forecast:  38497.47265625 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38493.44000000', 'low': '38486.63000000', 'close': '38493.44000000', 'volume': '2.71988000', 'closeTime': 1651582499999, 'quoteVolume': '104688.04971800', 'numTrades': 252}]
high     38507.769531
low      38486.488281
open     38496.167969
close    38497.871094
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38497.87109375 
Bot concensus: 38497.33984375

------------------------------ *************** ------------------------------ 




 Fast forecast:  38497.47900390625 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38495.30000000', 'low': '38486.63000000', 'close': '38495.30000000', 'volume': '4.49037000', 'closeTime': 1651582499999, 'quoteVolume': '172840.97527340', 'numTrades': 326}]
high     38507.773438
low      38486.492188
open     38496.171875
close    38497.878906
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38497.87890625 
Bot concensus: 38497.345703125

------------------------------ *************** ------------------------------ 




 Fast forecast:  38498.3232421875 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38498.25000000', 'low': '38486.63000000', 'close': '38498.24000000', 'volume': '4.63589000', 'closeTime': 1651582499999, 'quoteVolume': '178443.11733870', 'numTrades': 348}]
high     38508.664062
low      38487.355469
open     38497.031250
close    38498.707031
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38498.70703125 
Bot concensus: 38498.1953125

------------------------------ *************** ------------------------------ 




 Fast forecast:  38499.66455078125 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38501.45000000', 'low': '38486.63000000', 'close': '38501.45000000', 'volume': '5.53702000', 'closeTime': 1651582499999, 'quoteVolume': '213136.76314620', 'numTrades': 426}]
high     38510.078125
low      38488.722656
open     38498.398438
close    38500.023438
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38500.0234375 
Bot concensus: 38499.544921875

------------------------------ *************** ------------------------------ 




 Fast forecast:  38503.49462890625 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38507.87000000', 'low': '38486.63000000', 'close': '38507.87000000', 'volume': '6.67505000', 'closeTime': 1651582499999, 'quoteVolume': '256957.79959710', 'numTrades': 513}]
high     38514.113281
low      38492.632812
open     38502.304688
close    38503.781250
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38503.78125 
Bot concensus: 38503.399088541664

------------------------------ *************** ------------------------------ 




 Fast forecast:  38504.04296875 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38507.87000000', 'low': '38486.63000000', 'close': '38507.87000000', 'volume': '7.27549000', 'closeTime': 1651582499999, 'quoteVolume': '280079.46132090', 'numTrades': 580}]
high     38514.687500
low      38493.191406
open     38502.863281
close    38504.320312
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38504.3203125 
Bot concensus: 38503.950520833336

------------------------------ *************** ------------------------------ 




 Fast forecast:  38504.04736328125 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38507.87000000', 'low': '38486.63000000', 'close': '38504.22000000', 'volume': '8.10346000', 'closeTime': 1651582499999, 'quoteVolume': '311962.03829610', 'numTrades': 668}]
high     38514.695312
low      38493.195312
open     38502.867188
close    38504.324219
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38504.32421875 
Bot concensus: 38503.955078125

------------------------------ *************** ------------------------------ 




 Fast forecast:  38501.81494140625 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38507.87000000', 'low': '38486.63000000', 'close': '38504.22000000', 'volume': '8.83367000', 'closeTime': 1651582499999, 'quoteVolume': '340078.20988710', 'numTrades': 739}]
high     38512.335938
low      38490.941406
open     38500.578125
close    38502.132812
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38502.1328125 
Bot concensus: 38501.708984375

------------------------------ *************** ------------------------------ 




 Fast forecast:  38501.81982421875 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38507.87000000', 'low': '38486.63000000', 'close': '38504.22000000', 'volume': '9.70223000', 'closeTime': 1651582499999, 'quoteVolume': '373521.43804500', 'numTrades': 809}]
high     38512.339844
low      38490.949219
open     38500.585938
close    38502.136719
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38502.13671875 
Bot concensus: 38501.714192708336

------------------------------ *************** ------------------------------ 




 Fast forecast:  38499.70947265625 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38507.87000000', 'low': '38486.63000000', 'close': '38498.75000000', 'volume': '10.30318000', 'closeTime': 1651582499999, 'quoteVolume': '396658.62327840', 'numTrades': 888}]
high     38510.113281
low      38488.824219
open     38498.425781
close    38500.062500
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38500.0625 
Bot concensus: 38499.591796875

------------------------------ *************** ------------------------------ 




 Fast forecast:  38498.462890625 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38507.87000000', 'low': '38486.63000000', 'close': '38498.75000000', 'volume': '10.89190000', 'closeTime': 1651582499999, 'quoteVolume': '419323.60336520', 'numTrades': 951}]
high     38508.796875
low      38487.562500
open     38497.144531
close    38498.839844
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38498.83984375 
Bot concensus: 38498.337239583336

------------------------------ *************** ------------------------------ 




 Fast forecast:  38498.462890625 



[{'openTime': 1651582440000, 'open': '38486.64000000', 'high': '38507.87000000', 'low': '38486.63000000', 'close': '38498.74000000', 'volume': '11.31997000', 'closeTime': 1651582499999, 'quoteVolume': '435803.76122500', 'numTrades': 1010}]
high     38508.796875
low      38487.562500
open     38497.144531
close    38498.839844
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38498.83984375 
Bot concensus: 38498.337239583336

------------------------------ *************** ------------------------------ 




 Fast forecast:  38498.462890625 



[{'openTime': 1651582500000, 'open': '38498.75000000', 'high': '38498.75000000', 'low': '38498.74000000', 'close': '38498.75000000', 'volume': '0.04488000', 'closeTime': 1651582559999, 'quoteVolume': '1727.82373530', 'numTrades': 22}]
high     38508.796875
low      38487.562500
open     38497.144531
close    38498.839844
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->BTCUSDT forecasting model

Model prediction: 38498.83984375 
Bot concensus: 38498.337239583336

------------------------------ *************** ------------------------------ 

>>> 
= RESTART: C:\Users\benkimz\Documents\.AI-WORK-SPACE\bot-trader\trader-bot\draft\main.py
--@-bot--praparing to learn...

--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0630 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0122 - 3s/epoch - 274ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0091 - 3s/epoch - 262ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0078 - 3s/epoch - 263ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0069 - 3s/epoch - 263ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0060 - 3s/epoch - 263ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0051 - 3s/epoch - 270ms/step
Epoch 8/50
12/12 - 3s - loss: 0.0046 - 3s/epoch - 271ms/step
Epoch 9/50
12/12 - 3s - loss: 0.0042 - 3s/epoch - 280ms/step
Epoch 10/50
12/12 - 3s - loss: 0.0037 - 3s/epoch - 263ms/step
Epoch 11/50
12/12 - 3s - loss: 0.0032 - 3s/epoch - 266ms/step
Epoch 12/50
12/12 - 3s - loss: 0.0028 - 3s/epoch - 259ms/step
Epoch 13/50
12/12 - 3s - loss: 0.0025 - 3s/epoch - 261ms/step
Epoch 14/50
12/12 - 3s - loss: 0.0026 - 3s/epoch - 263ms/step
Epoch 15/50
12/12 - 3s - loss: 0.0028 - 3s/epoch - 262ms/step
Epoch 16/50
12/12 - 3s - loss: 0.0033 - 3s/epoch - 265ms/step
Epoch 17/50
12/12 - 3s - loss: 0.0027 - 3s/epoch - 273ms/step
Epoch 18/50
12/12 - 3s - loss: 0.0020 - 3s/epoch - 260ms/step
Epoch 19/50
12/12 - 3s - loss: 0.0020 - 3s/epoch - 260ms/step
Epoch 20/50
12/12 - 3s - loss: 0.0019 - 3s/epoch - 284ms/step
Epoch 21/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 269ms/step
Epoch 22/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 267ms/step
Epoch 23/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 272ms/step
Epoch 24/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 285ms/step
Epoch 25/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 272ms/step
Epoch 26/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 261ms/step
Epoch 27/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 262ms/step
Epoch 28/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 263ms/step
Epoch 29/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 259ms/step
Epoch 30/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 258ms/step
Epoch 31/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 267ms/step
Epoch 32/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 278ms/step
Epoch 33/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 263ms/step
Epoch 34/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 261ms/step
Epoch 35/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 257ms/step
Epoch 36/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 275ms/step
Epoch 37/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 260ms/step
Epoch 38/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 261ms/step
Epoch 39/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 262ms/step
Epoch 40/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 260ms/step
Epoch 41/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 281ms/step
Epoch 42/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 281ms/step
Epoch 43/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 259ms/step
Epoch 44/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 282ms/step
Epoch 45/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 281ms/step
Epoch 46/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 273ms/step
Epoch 47/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 265ms/step
Epoch 48/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 262ms/step
Epoch 49/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 263ms/step
Epoch 50/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 262ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 15s - loss: 0.0231 - 15s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 0.0039 - 4s/epoch - 306ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0021 - 3s/epoch - 271ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 278ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 265ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 276ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 267ms/step
Epoch 8/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 271ms/step
Epoch 9/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 266ms/step
Epoch 10/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 265ms/step
Epoch 11/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 262ms/step
Epoch 12/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 265ms/step
Epoch 13/50
12/12 - 3s - loss: 9.8285e-04 - 3s/epoch - 261ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0084 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0025 - 3s/epoch - 267ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 266ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 267ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 267ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 269ms/step
Epoch 7/50
12/12 - 3s - loss: 9.9231e-04 - 3s/epoch - 267ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 15s - loss: 0.0045 - 15s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 279ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 273ms/step
Epoch 4/50
12/12 - 3s - loss: 9.9735e-04 - 3s/epoch - 277ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0043 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 275ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 279ms/step
Epoch 4/50
12/12 - 3s - loss: 9.7233e-04 - 3s/epoch - 275ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0041 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 278ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 287ms/step
Epoch 4/50
12/12 - 3s - loss: 9.5447e-04 - 3s/epoch - 273ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0028 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 283ms/step
Epoch 3/50
12/12 - 3s - loss: 9.9666e-04 - 3s/epoch - 275ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0026 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 277ms/step
Epoch 4/50
12/12 - 3s - loss: 9.4089e-04 - 3s/epoch - 273ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0035 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 286ms/step
Epoch 3/50
12/12 - 3s - loss: 9.4164e-04 - 3s/epoch - 266ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0032 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 277ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 277ms/step
Epoch 4/50
12/12 - 3s - loss: 9.6420e-04 - 3s/epoch - 273ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0035 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 277ms/step
Epoch 3/50
12/12 - 3s - loss: 9.6248e-04 - 3s/epoch - 275ms/step

 -------------------- done training--> -------------------- 




 Fast forecast:  5.046966850757599 



[{'openTime': 1651583040000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '86.31000000', 'closeTime': 1651583099999, 'quoteVolume': '435.00240000', 'numTrades': 3}]
high     5.048124
low      5.044843
open     5.046567
close    5.047240
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047240257263184 
Bot concensus: 5.046875715255737

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046966850757599 



[{'openTime': 1651583040000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '86.31000000', 'closeTime': 1651583099999, 'quoteVolume': '435.00240000', 'numTrades': 3}]
high     5.048124
low      5.044843
open     5.046567
close    5.047240
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047240257263184 
Bot concensus: 5.046875715255737

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046966850757599 



[{'openTime': 1651583040000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '243.63000000', 'closeTime': 1651583099999, 'quoteVolume': '1227.89520000', 'numTrades': 4}]
high     5.048124
low      5.044843
open     5.046567
close    5.047240
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047240257263184 
Bot concensus: 5.046875715255737

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046966850757599 



[{'openTime': 1651583040000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '243.63000000', 'closeTime': 1651583099999, 'quoteVolume': '1227.89520000', 'numTrades': 4}]
high     5.048124
low      5.044843
open     5.046567
close    5.047240
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047240257263184 
Bot concensus: 5.046875715255737

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046966850757599 



[{'openTime': 1651583040000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '705.95000000', 'closeTime': 1651583099999, 'quoteVolume': '3557.98800000', 'numTrades': 7}]
high     5.048124
low      5.044843
open     5.046567
close    5.047240
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047240257263184 
Bot concensus: 5.046875715255737

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046966850757599 



[{'openTime': 1651583040000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '705.95000000', 'closeTime': 1651583099999, 'quoteVolume': '3557.98800000', 'numTrades': 7}]
high     5.048124
low      5.044843
open     5.046567
close    5.047240
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047240257263184 
Bot concensus: 5.046875715255737

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046966850757599 



[{'openTime': 1651583040000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '705.95000000', 'closeTime': 1651583099999, 'quoteVolume': '3557.98800000', 'numTrades': 7}]
high     5.048124
low      5.044843
open     5.046567
close    5.047240
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047240257263184 
Bot concensus: 5.046875715255737

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046966850757599 



[{'openTime': 1651583040000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '705.95000000', 'closeTime': 1651583099999, 'quoteVolume': '3557.98800000', 'numTrades': 7}]
high     5.048124
low      5.044843
open     5.046567
close    5.047240
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047240257263184 
Bot concensus: 5.046875715255737

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046966850757599 



[{'openTime': 1651583040000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '705.95000000', 'closeTime': 1651583099999, 'quoteVolume': '3557.98800000', 'numTrades': 7}]
high     5.048124
low      5.044843
open     5.046567
close    5.047240
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047240257263184 
Bot concensus: 5.046875715255737

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046966850757599 



[{'openTime': 1651583100000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '35.12000000', 'closeTime': 1651583159999, 'quoteVolume': '177.00480000', 'numTrades': 1}]
high     5.048124
low      5.044843
open     5.046567
close    5.047240
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047240257263184 
Bot concensus: 5.046875715255737

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046943664550781 



[{'openTime': 1651583100000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '35.12000000', 'closeTime': 1651583159999, 'quoteVolume': '177.00480000', 'numTrades': 1}]
high     5.048170
low      5.044977
open     5.046650
close    5.047151
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047150611877441 
Bot concensus: 5.0468746821085615

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046943664550781 



[{'openTime': 1651583100000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '38.84000000', 'closeTime': 1651583159999, 'quoteVolume': '195.75360000', 'numTrades': 2}]
high     5.048170
low      5.044977
open     5.046650
close    5.047151
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047150611877441 
Bot concensus: 5.0468746821085615

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046943664550781 



[{'openTime': 1651583100000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '38.84000000', 'closeTime': 1651583159999, 'quoteVolume': '195.75360000', 'numTrades': 2}]
high     5.048170
low      5.044977
open     5.046650
close    5.047151
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047150611877441 
Bot concensus: 5.0468746821085615

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046943664550781 



[{'openTime': 1651583100000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '38.84000000', 'closeTime': 1651583159999, 'quoteVolume': '195.75360000', 'numTrades': 2}]
high     5.048170
low      5.044977
open     5.046650
close    5.047151
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047150611877441 
Bot concensus: 5.0468746821085615

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046943664550781 



[{'openTime': 1651583100000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '38.84000000', 'closeTime': 1651583159999, 'quoteVolume': '195.75360000', 'numTrades': 2}]
high     5.048170
low      5.044977
open     5.046650
close    5.047151
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047150611877441 
Bot concensus: 5.0468746821085615

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.046943664550781 



[{'openTime': 1651583100000, 'open': '5.04000000', 'high': '5.04000000', 'low': '5.04000000', 'close': '5.04000000', 'volume': '38.84000000', 'closeTime': 1651583159999, 'quoteVolume': '195.75360000', 'numTrades': 2}]
high     5.048170
low      5.044977
open     5.046650
close    5.047151
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.047150611877441 
Bot concensus: 5.0468746821085615

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.051619291305542 



[{'openTime': 1651583100000, 'open': '5.04000000', 'high': '5.05000000', 'low': '5.04000000', 'close': '5.05000000', 'volume': '46.68000000', 'closeTime': 1651583159999, 'quoteVolume': '235.34560000', 'numTrades': 3}]
high     5.052876
low      5.049423
open     5.051260
close    5.051879
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.051878929138184 
Bot concensus: 5.051532745361328

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.051619291305542 



[{'openTime': 1651583100000, 'open': '5.04000000', 'high': '5.05000000', 'low': '5.04000000', 'close': '5.05000000', 'volume': '46.68000000', 'closeTime': 1651583159999, 'quoteVolume': '235.34560000', 'numTrades': 3}]
high     5.052876
low      5.049423
open     5.051260
close    5.051879
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.051878929138184 
Bot concensus: 5.051532745361328

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.051619291305542 



[{'openTime': 1651583100000, 'open': '5.04000000', 'high': '5.05000000', 'low': '5.04000000', 'close': '5.05000000', 'volume': '46.68000000', 'closeTime': 1651583159999, 'quoteVolume': '235.34560000', 'numTrades': 3}]
high     5.052876
low      5.049423
open     5.051260
close    5.051879
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.051878929138184 
Bot concensus: 5.051532745361328

------------------------------ *************** ------------------------------ 




 Fast forecast:  5.051619291305542 



[{'openTime': 1651583100000, 'open': '5.04000000', 'high': '5.05000000', 'low': '5.04000000', 'close': '5.05000000', 'volume': '360.01000000', 'closeTime': 1651583159999, 'quoteVolume': '1817.66210000', 'numTrades': 5}]
high     5.052876
low      5.049423
open     5.051260
close    5.051879
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ALICEUSDT forecasting model

Model prediction: 5.051878929138184 
Bot concensus: 5.051532745361328

------------------------------ *************** ------------------------------ 

>>> 
= RESTART: C:\Users\benkimz\Documents\.AI-WORK-SPACE\bot-trader\trader-bot\draft\main.py
--@-bot--praparing to learn...

--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0569 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0128 - 3s/epoch - 273ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0096 - 3s/epoch - 265ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0077 - 3s/epoch - 265ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0066 - 3s/epoch - 261ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0054 - 3s/epoch - 263ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0044 - 3s/epoch - 261ms/step
Epoch 8/50
12/12 - 3s - loss: 0.0037 - 3s/epoch - 279ms/step
Epoch 9/50
12/12 - 3s - loss: 0.0031 - 3s/epoch - 282ms/step
Epoch 10/50
12/12 - 3s - loss: 0.0026 - 3s/epoch - 269ms/step
Epoch 11/50
12/12 - 3s - loss: 0.0025 - 3s/epoch - 279ms/step
Epoch 12/50
12/12 - 3s - loss: 0.0024 - 3s/epoch - 269ms/step
Epoch 13/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 273ms/step
Epoch 14/50
12/12 - 4s - loss: 0.0016 - 4s/epoch - 294ms/step
Epoch 15/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 261ms/step
Epoch 16/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 17/50
12/12 - 4s - loss: 0.0012 - 4s/epoch - 302ms/step
Epoch 18/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 267ms/step
Epoch 19/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 259ms/step
Epoch 20/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 264ms/step
Epoch 21/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 261ms/step
Epoch 22/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 277ms/step
Epoch 23/50
12/12 - 3s - loss: 8.7265e-04 - 3s/epoch - 283ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0351 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0062 - 3s/epoch - 266ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0028 - 3s/epoch - 265ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0020 - 3s/epoch - 279ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 267ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 277ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 266ms/step
Epoch 8/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 281ms/step
Epoch 9/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 274ms/step
Epoch 10/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 269ms/step
Epoch 11/50
12/12 - 3s - loss: 9.5322e-04 - 3s/epoch - 265ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0080 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0022 - 3s/epoch - 273ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 276ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 272ms/step
Epoch 5/50
12/12 - 3s - loss: 8.6855e-04 - 3s/epoch - 270ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0060 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 0.0016 - 4s/epoch - 315ms/step
Epoch 3/50
12/12 - 4s - loss: 9.9217e-04 - 4s/epoch - 323ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0026 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 0.0010 - 4s/epoch - 348ms/step
Epoch 3/50
12/12 - 4s - loss: 7.2901e-04 - 4s/epoch - 329ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0022 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 8.6649e-04 - 4s/epoch - 307ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0047 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 0.0014 - 4s/epoch - 303ms/step
Epoch 3/50
12/12 - 4s - loss: 7.7074e-04 - 4s/epoch - 302ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 15s - loss: 0.0030 - 15s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 284ms/step
Epoch 3/50
12/12 - 4s - loss: 6.2516e-04 - 4s/epoch - 293ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0026 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 0.0010 - 4s/epoch - 293ms/step
Epoch 3/50
12/12 - 3s - loss: 6.0109e-04 - 3s/epoch - 277ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0025 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 8.8956e-04 - 3s/epoch - 276ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 15s - loss: 0.0015 - 15s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 7.6698e-04 - 3s/epoch - 282ms/step

 -------------------- done training--> -------------------- 




 Fast forecast:  0.792701467871666 



[{'openTime': 1651583580000, 'open': '0.79330000', 'high': '0.79330000', 'low': '0.79140000', 'close': '0.79180000', 'volume': '166233.10000000', 'closeTime': 1651583639999, 'quoteVolume': '131670.63529000', 'numTrades': 209}]
high     0.792985
low      0.792769
open     0.792857
close    0.792600
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.792600154876709 
Bot concensus: 0.792735238869985

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7920510247349739 



[{'openTime': 1651583580000, 'open': '0.79330000', 'high': '0.79330000', 'low': '0.79140000', 'close': '0.79200000', 'volume': '193655.40000000', 'closeTime': 1651583639999, 'quoteVolume': '153386.92525000', 'numTrades': 239}]
high     0.792311
low      0.792099
open     0.792196
close    0.791961
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7919605374336243 
Bot concensus: 0.7920811871687571

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7922445982694626 



[{'openTime': 1651583580000, 'open': '0.79330000', 'high': '0.79330000', 'low': '0.79140000', 'close': '0.79220000', 'volume': '202264.30000000', 'closeTime': 1651583639999, 'quoteVolume': '160207.13107000', 'numTrades': 258}]
high     0.792508
low      0.792288
open     0.792389
close    0.792154
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7921544313430786 
Bot concensus: 0.7922746539115906

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7922058552503586 



[{'openTime': 1651583580000, 'open': '0.79330000', 'high': '0.79330000', 'low': '0.79140000', 'close': '0.79220000', 'volume': '203315.70000000', 'closeTime': 1651583639999, 'quoteVolume': '161040.04792000', 'numTrades': 263}]
high     0.792468
low      0.792250
open     0.792350
close    0.792116
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7921156287193298 
Bot concensus: 0.7922359307607015

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7922058552503586 



[{'openTime': 1651583580000, 'open': '0.79330000', 'high': '0.79330000', 'low': '0.79140000', 'close': '0.79220000', 'volume': '203443.30000000', 'closeTime': 1651583639999, 'quoteVolume': '161141.13264000', 'numTrades': 264}]
high     0.792468
low      0.792250
open     0.792350
close    0.792116
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7921156287193298 
Bot concensus: 0.7922359307607015

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7922445982694626 



[{'openTime': 1651583580000, 'open': '0.79330000', 'high': '0.79330000', 'low': '0.79140000', 'close': '0.79220000', 'volume': '204255.10000000', 'closeTime': 1651583639999, 'quoteVolume': '161784.24253000', 'numTrades': 266}]
high     0.792508
low      0.792288
open     0.792389
close    0.792154
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7921544313430786 
Bot concensus: 0.7922746539115906

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7922058552503586 



[{'openTime': 1651583580000, 'open': '0.79330000', 'high': '0.79330000', 'low': '0.79140000', 'close': '0.79210000', 'volume': '214167.40000000', 'closeTime': 1651583639999, 'quoteVolume': '169636.13568000', 'numTrades': 287}]
high     0.792468
low      0.792250
open     0.792350
close    0.792116
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7921156287193298 
Bot concensus: 0.7922359307607015

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7922058552503586 



[{'openTime': 1651583580000, 'open': '0.79330000', 'high': '0.79330000', 'low': '0.79140000', 'close': '0.79200000', 'volume': '215104.40000000', 'closeTime': 1651583639999, 'quoteVolume': '170378.32549000', 'numTrades': 293}]
high     0.792468
low      0.792250
open     0.792350
close    0.792116
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7921156287193298 
Bot concensus: 0.7922359307607015

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7921284288167953 



[{'openTime': 1651583580000, 'open': '0.79330000', 'high': '0.79330000', 'low': '0.79140000', 'close': '0.79200000', 'volume': '215131.20000000', 'closeTime': 1651583639999, 'quoteVolume': '170399.55109000', 'numTrades': 294}]
high     0.792390
low      0.792175
open     0.792273
close    0.792038
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.792038083076477 
Bot concensus: 0.7921585440635681

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7921284288167953 



[{'openTime': 1651583580000, 'open': '0.79330000', 'high': '0.79330000', 'low': '0.79140000', 'close': '0.79200000', 'volume': '215131.20000000', 'closeTime': 1651583639999, 'quoteVolume': '170399.55109000', 'numTrades': 294}]
high     0.792390
low      0.792175
open     0.792273
close    0.792038
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.792038083076477 
Bot concensus: 0.7921585440635681

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7921284288167953 



[{'openTime': 1651583640000, 'open': '0.79200000', 'high': '0.79200000', 'low': '0.79200000', 'close': '0.79200000', 'volume': '0.00000000', 'closeTime': 1651583699999, 'quoteVolume': '0.00000000', 'numTrades': 0}]
high     0.792390
low      0.792175
open     0.792273
close    0.792038
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.792038083076477 
Bot concensus: 0.7921585440635681

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7916051596403122 



[{'openTime': 1651583640000, 'open': '0.79200000', 'high': '0.79200000', 'low': '0.79200000', 'close': '0.79200000', 'volume': '20.00000000', 'closeTime': 1651583699999, 'quoteVolume': '15.84000000', 'numTrades': 2}]
high     0.791875
low      0.791605
open     0.791748
close    0.791523
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7915225625038147 
Bot concensus: 0.7916326920191447

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7916051596403122 



[{'openTime': 1651583640000, 'open': '0.79200000', 'high': '0.79200000', 'low': '0.79190000', 'close': '0.79190000', 'volume': '1275.60000000', 'closeTime': 1651583699999, 'quoteVolume': '1010.22277000', 'numTrades': 8}]
high     0.791875
low      0.791605
open     0.791748
close    0.791523
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7915225625038147 
Bot concensus: 0.7916326920191447

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7915578484535217 



[{'openTime': 1651583640000, 'open': '0.79200000', 'high': '0.79200000', 'low': '0.79170000', 'close': '0.79180000', 'volume': '3609.40000000', 'closeTime': 1651583699999, 'quoteVolume': '2858.12561000', 'numTrades': 17}]
high     0.791827
low      0.791557
open     0.791700
close    0.791476
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7914758324623108 
Bot concensus: 0.7915851871172587

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7915019616484642 



[{'openTime': 1651583640000, 'open': '0.79200000', 'high': '0.79200000', 'low': '0.79170000', 'close': '0.79170000', 'volume': '11809.80000000', 'closeTime': 1651583699999, 'quoteVolume': '9351.16901000', 'numTrades': 28}]
high     0.791768
low      0.791499
open     0.791643
close    0.791421
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7914212346076965 
Bot concensus: 0.7915288706620535

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7913688197731972 



[{'openTime': 1651583640000, 'open': '0.79200000', 'high': '0.79200000', 'low': '0.79150000', 'close': '0.79160000', 'volume': '15470.80000000', 'closeTime': 1651583699999, 'quoteVolume': '12248.90277000', 'numTrades': 39}]
high     0.791631
low      0.791365
open     0.791509
close    0.791289
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.791289210319519 
Bot concensus: 0.7913953562577566

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7914074286818504 



[{'openTime': 1651583640000, 'open': '0.79200000', 'high': '0.79200000', 'low': '0.79150000', 'close': '0.79160000', 'volume': '15470.80000000', 'closeTime': 1651583699999, 'quoteVolume': '12248.90277000', 'numTrades': 39}]
high     0.791671
low      0.791402
open     0.791547
close    0.791328
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7913278937339783 
Bot concensus: 0.7914339403311411

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7914074286818504 



[{'openTime': 1651583640000, 'open': '0.79200000', 'high': '0.79200000', 'low': '0.79150000', 'close': '0.79170000', 'volume': '15536.80000000', 'closeTime': 1651583699999, 'quoteVolume': '12301.15497000', 'numTrades': 41}]
high     0.791671
low      0.791402
open     0.791547
close    0.791328
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7913278937339783 
Bot concensus: 0.7914339403311411

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7914460897445679 



[{'openTime': 1651583640000, 'open': '0.79200000', 'high': '0.79200000', 'low': '0.79150000', 'close': '0.79190000', 'volume': '15667.20000000', 'closeTime': 1651583699999, 'quoteVolume': '12404.41873000', 'numTrades': 43}]
high     0.791710
low      0.791440
open     0.791586
close    0.791367
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7913666367530823 
Bot concensus: 0.7914725740750631

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.7914847359061241 



[{'openTime': 1651583640000, 'open': '0.79200000', 'high': '0.79200000', 'low': '0.79150000', 'close': '0.79180000', 'volume': '16042.80000000', 'closeTime': 1651583699999, 'quoteVolume': '12701.81881000', 'numTrades': 45}]
high     0.791749
low      0.791478
open     0.791624
close    0.791405
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->ADAUSDT forecasting model

Model prediction: 0.7914053797721863 
Bot concensus: 0.79151118795077

------------------------------ *************** ------------------------------ 

>>> 
= RESTART: C:\Users\benkimz\Documents\.AI-WORK-SPACE\bot-trader\trader-bot\draft\main.py
--@-bot--praparing to learn...

--learning...

Epoch 1/50
12/12 - 17s - loss: 0.0725 - 17s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 0.0162 - 4s/epoch - 336ms/step
Epoch 3/50
12/12 - 4s - loss: 0.0119 - 4s/epoch - 322ms/step
Epoch 4/50
12/12 - 4s - loss: 0.0101 - 4s/epoch - 300ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0086 - 3s/epoch - 283ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0070 - 3s/epoch - 263ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0059 - 3s/epoch - 259ms/step
Epoch 8/50
12/12 - 3s - loss: 0.0048 - 3s/epoch - 266ms/step
Epoch 9/50
12/12 - 3s - loss: 0.0040 - 3s/epoch - 262ms/step
Epoch 10/50
12/12 - 3s - loss: 0.0035 - 3s/epoch - 260ms/step
Epoch 11/50
12/12 - 3s - loss: 0.0032 - 3s/epoch - 259ms/step
Epoch 12/50
12/12 - 3s - loss: 0.0029 - 3s/epoch - 266ms/step
Epoch 13/50
12/12 - 3s - loss: 0.0029 - 3s/epoch - 264ms/step
Epoch 14/50
12/12 - 3s - loss: 0.0029 - 3s/epoch - 260ms/step
Epoch 15/50
12/12 - 3s - loss: 0.0023 - 3s/epoch - 257ms/step
Epoch 16/50
12/12 - 3s - loss: 0.0024 - 3s/epoch - 268ms/step
Epoch 17/50
12/12 - 3s - loss: 0.0027 - 3s/epoch - 262ms/step
Epoch 18/50
12/12 - 3s - loss: 0.0023 - 3s/epoch - 263ms/step
Epoch 19/50
12/12 - 3s - loss: 0.0021 - 3s/epoch - 262ms/step
Epoch 20/50
12/12 - 3s - loss: 0.0019 - 3s/epoch - 263ms/step
Epoch 21/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 260ms/step
Epoch 22/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 263ms/step
Epoch 23/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 258ms/step
Epoch 24/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 279ms/step
Epoch 25/50
12/12 - 3s - loss: 0.0022 - 3s/epoch - 267ms/step
Epoch 26/50
12/12 - 4s - loss: 0.0016 - 4s/epoch - 345ms/step
Epoch 27/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 269ms/step
Epoch 28/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 265ms/step
Epoch 29/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 262ms/step
Epoch 30/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 267ms/step
Epoch 31/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 263ms/step
Epoch 32/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 269ms/step
Epoch 33/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 261ms/step
Epoch 34/50
12/12 - 3s - loss: 9.1881e-04 - 3s/epoch - 263ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0249 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0041 - 3s/epoch - 270ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0024 - 3s/epoch - 280ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 274ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 267ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 271ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 270ms/step
Epoch 8/50
12/12 - 3s - loss: 9.6476e-04 - 3s/epoch - 272ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 15s - loss: 0.0105 - 15s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 0.0027 - 4s/epoch - 347ms/step
Epoch 3/50
12/12 - 4s - loss: 0.0015 - 4s/epoch - 319ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 291ms/step
Epoch 5/50
12/12 - 4s - loss: 9.4697e-04 - 4s/epoch - 298ms/step

 -------------------- done training--> -------------------- 

Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=XRPUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x00000200AD47C970>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0061 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 272ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 272ms/step
Epoch 4/50
12/12 - 3s - loss: 8.8631e-04 - 3s/epoch - 270ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0032 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 279ms/step
Epoch 3/50
12/12 - 3s - loss: 8.2812e-04 - 3s/epoch - 288ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0035 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0010 - 3s/epoch - 277ms/step
Epoch 3/50
12/12 - 3s - loss: 7.5756e-04 - 3s/epoch - 279ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 15s - loss: 0.0022 - 15s/epoch - 1s/step
Epoch 2/50
12/12 - 4s - loss: 8.5721e-04 - 4s/epoch - 297ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0051 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 278ms/step
Epoch 3/50
12/12 - 3s - loss: 8.3036e-04 - 3s/epoch - 282ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0036 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 9.5133e-04 - 3s/epoch - 273ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0019 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 7.7273e-04 - 3s/epoch - 279ms/step

 -------------------- done training--> -------------------- 




 Fast forecast:  0.6181168407201767 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61780000', 'close': '0.61780000', 'volume': '3991.00000000', 'closeTime': 1651584299999, 'quoteVolume': '2465.64700000', 'numTrades': 6}]
high     0.618246
low      0.617923
open     0.617987
close    0.618156
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.618155837059021 
Bot concensus: 0.6181038419405619

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6181681603193283 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61780000', 'close': '0.61790000', 'volume': '6593.00000000', 'closeTime': 1651584299999, 'quoteVolume': '4073.42280000', 'numTrades': 8}]
high     0.618297
low      0.617974
open     0.618038
close    0.618207
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6182073950767517 
Bot concensus: 0.6181550820668539

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6181681603193283 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61780000', 'close': '0.61790000', 'volume': '6593.00000000', 'closeTime': 1651584299999, 'quoteVolume': '4073.42280000', 'numTrades': 8}]
high     0.618297
low      0.617974
open     0.618038
close    0.618207
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6182073950767517 
Bot concensus: 0.6181550820668539

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6181681603193283 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61780000', 'close': '0.61780000', 'volume': '6625.00000000', 'closeTime': 1651584299999, 'quoteVolume': '4093.19240000', 'numTrades': 9}]
high     0.618297
low      0.617974
open     0.618038
close    0.618207
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6182073950767517 
Bot concensus: 0.6181550820668539

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6181199327111244 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61780000', 'close': '0.61780000', 'volume': '6625.00000000', 'closeTime': 1651584299999, 'quoteVolume': '4093.19240000', 'numTrades': 9}]
high     0.618247
low      0.617926
open     0.617989
close    0.618160
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6181596517562866 
Bot concensus: 0.6181066930294037

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6180559247732162 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61760000', 'close': '0.61760000', 'volume': '49122.00000000', 'closeTime': 1651584299999, 'quoteVolume': '30347.56090000', 'numTrades': 31}]
high     0.618182
low      0.617860
open     0.617923
close    0.618096
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6180964112281799 
Bot concensus: 0.6180424292882284

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6180077940225601 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61760000', 'close': '0.61760000', 'volume': '57791.00000000', 'closeTime': 1651584299999, 'quoteVolume': '35701.54100000', 'numTrades': 37}]
high     0.618133
low      0.617812
open     0.617874
close    0.618049
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6180487275123596 
Bot concensus: 0.6179941495259603

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6180077940225601 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61750000', 'close': '0.61750000', 'volume': '57849.00000000', 'closeTime': 1651584299999, 'quoteVolume': '35737.35600000', 'numTrades': 40}]
high     0.618133
low      0.617812
open     0.617874
close    0.618049
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6180487275123596 
Bot concensus: 0.6179941495259603

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6179518550634384 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61750000', 'close': '0.61760000', 'volume': '58540.00000000', 'closeTime': 1651584299999, 'quoteVolume': '36164.11760000', 'numTrades': 42}]
high     0.618076
low      0.617756
open     0.617816
close    0.617993
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6179934144020081 
Bot concensus: 0.6179380019505819

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6179998591542244 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61750000', 'close': '0.61750000', 'volume': '58667.00000000', 'closeTime': 1651584299999, 'quoteVolume': '36242.54010000', 'numTrades': 45}]
high     0.618125
low      0.617803
open     0.617865
close    0.618041
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.618040919303894 
Bot concensus: 0.6179861724376678

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6179518550634384 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61750000', 'close': '0.61750000', 'volume': '58887.00000000', 'closeTime': 1651584299999, 'quoteVolume': '36378.39010000', 'numTrades': 48}]
high     0.618076
low      0.617756
open     0.617816
close    0.617993
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6179934144020081 
Bot concensus: 0.6179380019505819

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6179518550634384 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61750000', 'close': '0.61750000', 'volume': '59137.00000000', 'closeTime': 1651584299999, 'quoteVolume': '36532.76510000', 'numTrades': 50}]
high     0.618076
low      0.617756
open     0.617816
close    0.617993
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6179934144020081 
Bot concensus: 0.6179380019505819

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6179518550634384 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61750000', 'close': '0.61750000', 'volume': '59137.00000000', 'closeTime': 1651584299999, 'quoteVolume': '36532.76510000', 'numTrades': 50}]
high     0.618076
low      0.617756
open     0.617816
close    0.617993
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6179934144020081 
Bot concensus: 0.6179380019505819

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6179518550634384 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61750000', 'close': '0.61750000', 'volume': '59497.00000000', 'closeTime': 1651584299999, 'quoteVolume': '36755.06510000', 'numTrades': 51}]
high     0.618076
low      0.617756
open     0.617816
close    0.617993
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6179934144020081 
Bot concensus: 0.6179380019505819

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6179518550634384 



[{'openTime': 1651584240000, 'open': '0.61780000', 'high': '0.61790000', 'low': '0.61750000', 'close': '0.61750000', 'volume': '59497.00000000', 'closeTime': 1651584299999, 'quoteVolume': '36755.06510000', 'numTrades': 51}]
high     0.618076
low      0.617756
open     0.617816
close    0.617993
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6179934144020081 
Bot concensus: 0.6179380019505819

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6179518550634384 



[{'openTime': 1651584300000, 'open': '0.61750000', 'high': '0.61750000', 'low': '0.61740000', 'close': '0.61740000', 'volume': '14468.00000000', 'closeTime': 1651584359999, 'quoteVolume': '8933.95660000', 'numTrades': 17}]
high     0.618076
low      0.617756
open     0.617816
close    0.617993
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6179934144020081 
Bot concensus: 0.6179380019505819

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.617794930934906 



[{'openTime': 1651584300000, 'open': '0.61750000', 'high': '0.61750000', 'low': '0.61730000', 'close': '0.61730000', 'volume': '19281.00000000', 'closeTime': 1651584359999, 'quoteVolume': '11905.37030000', 'numTrades': 32}]
high     0.617913
low      0.617608
open     0.617651
close    0.617837
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.6178374290466309 
Bot concensus: 0.6177807648976644

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6178426519036293 



[{'openTime': 1651584300000, 'open': '0.61750000', 'high': '0.61750000', 'low': '0.61730000', 'close': '0.61740000', 'volume': '21027.00000000', 'closeTime': 1651584359999, 'quoteVolume': '12983.31350000', 'numTrades': 35}]
high     0.617962
low      0.617656
open     0.617700
close    0.617885
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.617884635925293 
Bot concensus: 0.6178286572297415

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6178426519036293 



[{'openTime': 1651584300000, 'open': '0.61750000', 'high': '0.61750000', 'low': '0.61730000', 'close': '0.61740000', 'volume': '21338.00000000', 'closeTime': 1651584359999, 'quoteVolume': '13175.32490000', 'numTrades': 36}]
high     0.617962
low      0.617656
open     0.617700
close    0.617885
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.617884635925293 
Bot concensus: 0.6178286572297415

------------------------------ *************** ------------------------------ 




 Fast forecast:  0.6178426519036293 



[{'openTime': 1651584300000, 'open': '0.61750000', 'high': '0.61750000', 'low': '0.61730000', 'close': '0.61740000', 'volume': '22175.00000000', 'closeTime': 1651584359999, 'quoteVolume': '13692.08870000', 'numTrades': 40}]
high     0.617962
low      0.617656
open     0.617700
close    0.617885
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->XRPUSDT forecasting model

Model prediction: 0.617884635925293 
Bot concensus: 0.6178286572297415

------------------------------ *************** ------------------------------ 

>>> 
= RESTART: C:\Users\benkimz\Documents\.AI-WORK-SPACE\bot-trader\trader-bot\draft\main.py
--@-bot--praparing to learn...

--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0527 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0179 - 3s/epoch - 283ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0130 - 3s/epoch - 279ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0092 - 3s/epoch - 281ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0073 - 3s/epoch - 289ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0062 - 3s/epoch - 274ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0056 - 3s/epoch - 263ms/step
Epoch 8/50
12/12 - 3s - loss: 0.0048 - 3s/epoch - 264ms/step
Epoch 9/50
12/12 - 3s - loss: 0.0044 - 3s/epoch - 265ms/step
Epoch 10/50
12/12 - 3s - loss: 0.0037 - 3s/epoch - 264ms/step
Epoch 11/50
12/12 - 3s - loss: 0.0034 - 3s/epoch - 266ms/step
Epoch 12/50
12/12 - 3s - loss: 0.0034 - 3s/epoch - 272ms/step
Epoch 13/50
12/12 - 3s - loss: 0.0032 - 3s/epoch - 267ms/step
Epoch 14/50
12/12 - 3s - loss: 0.0031 - 3s/epoch - 265ms/step
Epoch 15/50
12/12 - 3s - loss: 0.0028 - 3s/epoch - 272ms/step
Epoch 16/50
12/12 - 3s - loss: 0.0027 - 3s/epoch - 266ms/step
Epoch 17/50
12/12 - 3s - loss: 0.0026 - 3s/epoch - 269ms/step
Epoch 18/50
12/12 - 3s - loss: 0.0024 - 3s/epoch - 267ms/step
Epoch 19/50
12/12 - 3s - loss: 0.0024 - 3s/epoch - 267ms/step
Epoch 20/50
12/12 - 3s - loss: 0.0023 - 3s/epoch - 281ms/step
Epoch 21/50
12/12 - 3s - loss: 0.0028 - 3s/epoch - 267ms/step
Epoch 22/50
12/12 - 3s - loss: 0.0024 - 3s/epoch - 281ms/step
Epoch 23/50
12/12 - 4s - loss: 0.0022 - 4s/epoch - 314ms/step
Epoch 24/50
12/12 - 3s - loss: 0.0023 - 3s/epoch - 269ms/step
Epoch 25/50
12/12 - 4s - loss: 0.0023 - 4s/epoch - 339ms/step
Epoch 26/50
12/12 - 4s - loss: 0.0024 - 4s/epoch - 330ms/step
Epoch 27/50
12/12 - 4s - loss: 0.0022 - 4s/epoch - 314ms/step
Epoch 28/50
12/12 - 3s - loss: 0.0020 - 3s/epoch - 287ms/step
Epoch 29/50
12/12 - 4s - loss: 0.0019 - 4s/epoch - 329ms/step
Epoch 30/50
12/12 - 4s - loss: 0.0020 - 4s/epoch - 303ms/step
Epoch 31/50
12/12 - 4s - loss: 0.0020 - 4s/epoch - 309ms/step
Epoch 32/50
12/12 - 3s - loss: 0.0021 - 3s/epoch - 290ms/step
Epoch 33/50
12/12 - 4s - loss: 0.0019 - 4s/epoch - 302ms/step
Epoch 34/50
12/12 - 3s - loss: 0.0019 - 3s/epoch - 282ms/step
Epoch 35/50
12/12 - 4s - loss: 0.0019 - 4s/epoch - 337ms/step
Epoch 36/50
12/12 - 3s - loss: 0.0019 - 3s/epoch - 259ms/step
Epoch 37/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 281ms/step
Epoch 38/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 264ms/step
Epoch 39/50
12/12 - 3s - loss: 0.0019 - 3s/epoch - 260ms/step
Epoch 40/50
12/12 - 4s - loss: 0.0021 - 4s/epoch - 310ms/step
Epoch 41/50
12/12 - 4s - loss: 0.0020 - 4s/epoch - 313ms/step
Epoch 42/50
12/12 - 4s - loss: 0.0018 - 4s/epoch - 318ms/step
Epoch 43/50
12/12 - 4s - loss: 0.0018 - 4s/epoch - 304ms/step
Epoch 44/50
12/12 - 3s - loss: 0.0019 - 3s/epoch - 288ms/step
Epoch 45/50
12/12 - 4s - loss: 0.0018 - 4s/epoch - 303ms/step
Epoch 46/50
12/12 - 4s - loss: 0.0017 - 4s/epoch - 306ms/step
Epoch 47/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 283ms/step
Epoch 48/50
12/12 - 3s - loss: 0.0019 - 3s/epoch - 256ms/step
Epoch 49/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 258ms/step
Epoch 50/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 257ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0073 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0025 - 3s/epoch - 281ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0020 - 3s/epoch - 284ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 268ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 272ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 271ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 270ms/step
Epoch 8/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 272ms/step
Epoch 9/50
12/12 - 4s - loss: 0.0017 - 4s/epoch - 299ms/step
Epoch 10/50
12/12 - 4s - loss: 0.0017 - 4s/epoch - 312ms/step
Epoch 11/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 281ms/step
Epoch 12/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 267ms/step
Epoch 13/50
12/12 - 4s - loss: 0.0018 - 4s/epoch - 299ms/step
Epoch 14/50
12/12 - 3s - loss: 0.0019 - 3s/epoch - 264ms/step
Epoch 15/50
12/12 - 3s - loss: 0.0019 - 3s/epoch - 262ms/step
Epoch 16/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 264ms/step
Epoch 17/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 279ms/step
Epoch 18/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 272ms/step
Epoch 19/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 263ms/step
Epoch 20/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 262ms/step
Epoch 21/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 266ms/step
Epoch 22/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 263ms/step
Epoch 23/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 260ms/step
Epoch 24/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 266ms/step
Epoch 25/50
12/12 - 3s - loss: 0.0021 - 3s/epoch - 262ms/step
Epoch 26/50
12/12 - 3s - loss: 0.0020 - 3s/epoch - 276ms/step
Epoch 27/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 264ms/step
Epoch 28/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 260ms/step
Epoch 29/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 262ms/step
Epoch 30/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 266ms/step
Epoch 31/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 267ms/step
Epoch 32/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 265ms/step
Epoch 33/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 262ms/step
Epoch 34/50
12/12 - 3s - loss: 0.0019 - 3s/epoch - 279ms/step
Epoch 35/50
12/12 - 4s - loss: 0.0017 - 4s/epoch - 324ms/step
Epoch 36/50
12/12 - 4s - loss: 0.0017 - 4s/epoch - 297ms/step
Epoch 37/50
12/12 - 4s - loss: 0.0017 - 4s/epoch - 350ms/step
Epoch 38/50
12/12 - 4s - loss: 0.0018 - 4s/epoch - 301ms/step
Epoch 39/50
12/12 - 4s - loss: 0.0017 - 4s/epoch - 300ms/step
Epoch 40/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 268ms/step
Epoch 41/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 267ms/step
Epoch 42/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 266ms/step
Epoch 43/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 266ms/step
Epoch 44/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 267ms/step
Epoch 45/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 273ms/step
Epoch 46/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 262ms/step
Epoch 47/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 264ms/step
Epoch 48/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 260ms/step
Epoch 49/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 266ms/step
Epoch 50/50
12/12 - 3s - loss: 0.0017 - 3s/epoch - 267ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0037 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0018 - 3s/epoch - 267ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 262ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 267ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 268ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 264ms/step
Epoch 8/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 269ms/step
Epoch 9/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 266ms/step
Epoch 10/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 276ms/step
Epoch 11/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 266ms/step
Epoch 12/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 267ms/step
Epoch 13/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 271ms/step
Epoch 14/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 290ms/step
Epoch 15/50
12/12 - 4s - loss: 0.0013 - 4s/epoch - 347ms/step
Epoch 16/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 283ms/step
Epoch 17/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 279ms/step
Epoch 18/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 267ms/step
Epoch 19/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 282ms/step
Epoch 20/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 266ms/step
Epoch 21/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 267ms/step
Epoch 22/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 268ms/step
Epoch 23/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 271ms/step
Epoch 24/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 271ms/step
Epoch 25/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 271ms/step
Epoch 26/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 270ms/step
Epoch 27/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 267ms/step
Epoch 28/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 263ms/step
Epoch 29/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 270ms/step
Epoch 30/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 271ms/step
Epoch 31/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 267ms/step
Epoch 32/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 267ms/step
Epoch 33/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 267ms/step
Epoch 34/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 264ms/step
Epoch 35/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 269ms/step
Epoch 36/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 270ms/step
Epoch 37/50
12/12 - 4s - loss: 0.0014 - 4s/epoch - 297ms/step
Epoch 38/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 286ms/step
Epoch 39/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 281ms/step
Epoch 40/50
12/12 - 4s - loss: 0.0017 - 4s/epoch - 317ms/step
Epoch 41/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 279ms/step
Epoch 42/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 268ms/step
Epoch 43/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 281ms/step
Epoch 44/50
12/12 - 4s - loss: 0.0013 - 4s/epoch - 293ms/step
Epoch 45/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 269ms/step
Epoch 46/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 271ms/step
Epoch 47/50
12/12 - 4s - loss: 0.0013 - 4s/epoch - 293ms/step
Epoch 48/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 281ms/step
Epoch 49/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 268ms/step
Epoch 50/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 267ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0033 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 275ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 291ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 269ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 273ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 273ms/step
Epoch 8/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 9/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 271ms/step
Epoch 10/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 277ms/step
Epoch 11/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 274ms/step
Epoch 12/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 274ms/step
Epoch 13/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 277ms/step
Epoch 14/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 269ms/step
Epoch 15/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 271ms/step
Epoch 16/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 271ms/step
Epoch 17/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 271ms/step
Epoch 18/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 273ms/step
Epoch 19/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 272ms/step
Epoch 20/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 284ms/step
Epoch 21/50
12/12 - 3s - loss: 0.0016 - 3s/epoch - 270ms/step
Epoch 22/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 272ms/step
Epoch 23/50
12/12 - 4s - loss: 0.0015 - 4s/epoch - 307ms/step
Epoch 24/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 272ms/step
Epoch 25/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 274ms/step
Epoch 26/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 279ms/step
Epoch 27/50
12/12 - 4s - loss: 0.0013 - 4s/epoch - 313ms/step
Epoch 28/50
12/12 - 4s - loss: 0.0014 - 4s/epoch - 303ms/step
Epoch 29/50
12/12 - 4s - loss: 0.0013 - 4s/epoch - 296ms/step
Epoch 30/50
12/12 - 4s - loss: 0.0013 - 4s/epoch - 313ms/step
Epoch 31/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 270ms/step
Epoch 32/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 33/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 271ms/step
Epoch 34/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 35/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 269ms/step
Epoch 36/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 284ms/step
Epoch 37/50
12/12 - 4s - loss: 0.0013 - 4s/epoch - 313ms/step
Epoch 38/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 279ms/step
Epoch 39/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 278ms/step
Epoch 40/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 272ms/step
Epoch 41/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 272ms/step
Epoch 42/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 272ms/step
Epoch 43/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 44/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 272ms/step
Epoch 45/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 269ms/step
Epoch 46/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 271ms/step
Epoch 47/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 272ms/step
Epoch 48/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 272ms/step
Epoch 49/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 277ms/step
Epoch 50/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 275ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0026 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 283ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 274ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 283ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 285ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 275ms/step
Epoch 8/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 275ms/step
Epoch 9/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 275ms/step
Epoch 10/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 276ms/step
Epoch 11/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 271ms/step
Epoch 12/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 276ms/step
Epoch 13/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 271ms/step
Epoch 14/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 274ms/step
Epoch 15/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 16/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 270ms/step
Epoch 17/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 18/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 272ms/step
Epoch 19/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 20/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 291ms/step
Epoch 21/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 271ms/step
Epoch 22/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 23/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 272ms/step
Epoch 24/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 273ms/step
Epoch 25/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 273ms/step
Epoch 26/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 277ms/step
Epoch 27/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 275ms/step
Epoch 28/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 29/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 275ms/step
Epoch 30/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 280ms/step
Epoch 31/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 281ms/step
Epoch 32/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 33/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 275ms/step
Epoch 34/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 35/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 277ms/step
Epoch 36/50
12/12 - 4s - loss: 0.0013 - 4s/epoch - 293ms/step
Epoch 37/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 278ms/step
Epoch 38/50
12/12 - 4s - loss: 0.0013 - 4s/epoch - 295ms/step
Epoch 39/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 275ms/step
Epoch 40/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 278ms/step
Epoch 41/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 272ms/step
Epoch 42/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 277ms/step
Epoch 43/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 44/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 45/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 46/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 274ms/step
Epoch 47/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 48/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 277ms/step
Epoch 49/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 271ms/step
Epoch 50/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 276ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0028 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0014 - 3s/epoch - 285ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 269ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 272ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 269ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 8/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 270ms/step
Epoch 9/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 10/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 272ms/step
Epoch 11/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 272ms/step
Epoch 12/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 271ms/step
Epoch 13/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 277ms/step
Epoch 14/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 268ms/step
Epoch 15/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 269ms/step
Epoch 16/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 272ms/step
Epoch 17/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 269ms/step
Epoch 18/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 19/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 20/50
12/12 - 4s - loss: 0.0012 - 4s/epoch - 292ms/step
Epoch 21/50
12/12 - 4s - loss: 0.0012 - 4s/epoch - 325ms/step
Epoch 22/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 280ms/step
Epoch 23/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 291ms/step
Epoch 24/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 277ms/step
Epoch 25/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 274ms/step
Epoch 26/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 275ms/step
Epoch 27/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 271ms/step
Epoch 28/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 285ms/step
Epoch 29/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 289ms/step
Epoch 30/50
12/12 - 3s - loss: 0.0015 - 3s/epoch - 291ms/step
Epoch 31/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 271ms/step
Epoch 32/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 270ms/step
Epoch 33/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 273ms/step
Epoch 34/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 270ms/step
Epoch 35/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 36/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 269ms/step
Epoch 37/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 270ms/step
Epoch 38/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 39/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 40/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 279ms/step
Epoch 41/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 42/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 275ms/step
Epoch 43/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 44/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 283ms/step
Epoch 45/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 271ms/step
Epoch 46/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 272ms/step
Epoch 47/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 268ms/step
Epoch 48/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 272ms/step
Epoch 49/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 270ms/step
Epoch 50/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0019 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 273ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 271ms/step
Epoch 4/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 285ms/step
Epoch 5/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 278ms/step
Epoch 6/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 268ms/step
Epoch 7/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 270ms/step
Epoch 8/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 265ms/step
Epoch 9/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 267ms/step
Epoch 10/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 271ms/step
Epoch 11/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 267ms/step
Epoch 12/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 265ms/step
Epoch 13/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 271ms/step
Epoch 14/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 271ms/step
Epoch 15/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 272ms/step
Epoch 16/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 269ms/step
Epoch 17/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 269ms/step
Epoch 18/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 268ms/step
Epoch 19/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 273ms/step
Epoch 20/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 269ms/step
Epoch 21/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 272ms/step
Epoch 22/50
12/12 - 4s - loss: 0.0011 - 4s/epoch - 295ms/step
Epoch 23/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 285ms/step
Epoch 24/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 276ms/step
Epoch 25/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 267ms/step
Epoch 26/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 268ms/step
Epoch 27/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 265ms/step
Epoch 28/50
12/12 - 4s - loss: 0.0011 - 4s/epoch - 310ms/step
Epoch 29/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 286ms/step
Epoch 30/50
12/12 - 4s - loss: 0.0012 - 4s/epoch - 297ms/step
Epoch 31/50
12/12 - 4s - loss: 0.0011 - 4s/epoch - 292ms/step
Epoch 32/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 280ms/step
Epoch 33/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 291ms/step
Epoch 34/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 275ms/step
Epoch 35/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 268ms/step
Epoch 36/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 270ms/step
Epoch 37/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 264ms/step
Epoch 38/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 268ms/step
Epoch 39/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 264ms/step
Epoch 40/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 266ms/step
Epoch 41/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 288ms/step
Epoch 42/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 286ms/step
Epoch 43/50
12/12 - 3s - loss: 0.0012 - 3s/epoch - 291ms/step
Epoch 44/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 278ms/step
Epoch 45/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 268ms/step
Epoch 46/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 266ms/step
Epoch 47/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 265ms/step
Epoch 48/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 267ms/step
Epoch 49/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 267ms/step
Epoch 50/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 263ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0024 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 275ms/step
Epoch 3/50
12/12 - 3s - loss: 9.4325e-04 - 3s/epoch - 267ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0028 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0013 - 3s/epoch - 274ms/step
Epoch 3/50
12/12 - 3s - loss: 9.6043e-04 - 3s/epoch - 271ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 14s - loss: 0.0020 - 14s/epoch - 1s/step
Epoch 2/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 275ms/step
Epoch 3/50
12/12 - 3s - loss: 0.0011 - 3s/epoch - 269ms/step
Epoch 4/50
12/12 - 3s - loss: 9.0438e-04 - 3s/epoch - 277ms/step

 -------------------- done training--> -------------------- 

--@-bot--praparing to learn...

--@bot--relearning in a few...
--learning...

Epoch 1/50
12/12 - 16s - loss: 0.0016 - 16s/epoch - 1s/step
Epoch 2/50
12/12 - 5s - loss: 9.6499e-04 - 5s/epoch - 400ms/step

 -------------------- done training--> -------------------- 




 Fast forecast:  99.51073741912842 



[{'openTime': 1651585800000, 'open': '99.40000000', 'high': '99.50000000', 'low': '99.40000000', 'close': '99.50000000', 'volume': '7.32100000', 'closeTime': 1651585859999, 'quoteVolume': '727.81950000', 'numTrades': 2}]
high     99.525459
low      99.558350
open     99.677948
close    99.464828
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->LTCUSDT forecasting model

Model prediction: 99.46482849121094 
Bot concensus: 99.5260403951009

------------------------------ *************** ------------------------------ 




 Fast forecast:  99.46641826629639 



[{'openTime': 1651585800000, 'open': '99.40000000', 'high': '99.50000000', 'low': '99.40000000', 'close': '99.50000000', 'volume': '8.16500000', 'closeTime': 1651585859999, 'quoteVolume': '811.78320000', 'numTrades': 5}]
high     99.487274
low      99.527458
open     99.555511
close    99.432220
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->LTCUSDT forecasting model

Model prediction: 99.43222045898438 
Bot concensus: 99.47781753540039

------------------------------ *************** ------------------------------ 




 Fast forecast:  99.50863838195801 



[{'openTime': 1651585800000, 'open': '99.40000000', 'high': '99.60000000', 'low': '99.40000000', 'close': '99.50000000', 'volume': '99.42800000', 'closeTime': 1651585859999, 'quoteVolume': '9892.75320000', 'numTrades': 15}]
high     99.530464
low      99.567589
open     99.596710
close    99.474869
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->LTCUSDT forecasting model

Model prediction: 99.47486877441406 
Bot concensus: 99.51989491780598

------------------------------ *************** ------------------------------ 




 Fast forecast:  99.54952335357666 



[{'openTime': 1651585800000, 'open': '99.40000000', 'high': '99.70000000', 'low': '99.40000000', 'close': '99.60000000', 'volume': '167.39300000', 'closeTime': 1651585859999, 'quoteVolume': '16662.54730000', 'numTrades': 59}]
high     99.572029
low      99.606529
open     99.636147
close    99.516296
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->LTCUSDT forecasting model

Model prediction: 99.51629638671875 
Bot concensus: 99.56059900919597

------------------------------ *************** ------------------------------ 




 Fast forecast:  99.54756259918213 



[{'openTime': 1651585800000, 'open': '99.40000000', 'high': '99.70000000', 'low': '99.40000000', 'close': '99.60000000', 'volume': '233.93800000', 'closeTime': 1651585859999, 'quoteVolume': '23290.42930000', 'numTrades': 65}]
high     99.569771
low      99.604691
open     99.633789
close    99.514450
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->LTCUSDT forecasting model

Model prediction: 99.51445007324219 
Bot concensus: 99.55860010782878

------------------------------ *************** ------------------------------ 




 Fast forecast:  99.54756259918213 



[{'openTime': 1651585800000, 'open': '99.40000000', 'high': '99.70000000', 'low': '99.40000000', 'close': '99.60000000', 'volume': '308.77900000', 'closeTime': 1651585859999, 'quoteVolume': '30744.59290000', 'numTrades': 71}]
high     99.569771
low      99.604691
open     99.633789
close    99.514450
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->LTCUSDT forecasting model

Model prediction: 99.51445007324219 
Bot concensus: 99.55860010782878

------------------------------ *************** ------------------------------ 




 Fast forecast:  99.54756259918213 



[{'openTime': 1651585800000, 'open': '99.40000000', 'high': '99.70000000', 'low': '99.40000000', 'close': '99.60000000', 'volume': '402.82600000', 'closeTime': 1651585859999, 'quoteVolume': '40111.67410000', 'numTrades': 82}]
high     99.569771
low      99.604691
open     99.633789
close    99.514450
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->LTCUSDT forecasting model

Model prediction: 99.51445007324219 
Bot concensus: 99.55860010782878

------------------------------ *************** ------------------------------ 




 Fast forecast:  99.54756259918213 



[{'openTime': 1651585800000, 'open': '99.40000000', 'high': '99.70000000', 'low': '99.40000000', 'close': '99.60000000', 'volume': '403.79700000', 'closeTime': 1651585859999, 'quoteVolume': '40208.38570000', 'numTrades': 83}]
high     99.569771
low      99.604691
open     99.633789
close    99.514450
dtype: float64
[---------------------------------------------------------------------------]

 ------------------------------ @--bot - forecast results- ------------------------------ 

--from: --ai-bot--{model}-->LTCUSDT forecasting model

Model prediction: 99.51445007324219 
Bot concensus: 99.55860010782878

------------------------------ *************** ------------------------------ 




 Fast forecast:  99.54756259918213 



--warning-from--bot: a problem occured while try to make a prediction. |help|--> ('Connection aborted.', ConnectionAbortedError(10053, 'An established connection was aborted by the software in your host machine', None, 10053, None))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=LTCUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001CC4250BD90>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=LTCUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001CC4250B400>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=LTCUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001CC4250B7C0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=LTCUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001CC4250B580>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=LTCUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001CC4250BE20>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=LTCUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001CC4250B640>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=LTCUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001CC4250B160>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=LTCUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001CC4250B460>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=LTCUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001CC4250BB50>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=LTCUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001CC4250B400>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
Fatal error! Could not refresh previous data! HTTPSConnectionPool(host='www.binance.com', port=443): Max retries exceeded with url: /api/v1/klines?symbol=LTCUSDT&interval=1m&limit=1000 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001CC4250B7C0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
>>> 