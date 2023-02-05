# Building Bot Trader in TensorFlow
## *I'm a TensorFlow & Keras fanatic and passionate about machine learning.

This is the first thing I built when I was getting started with TensorFlow and the Keras API. It might seem rough but I liked it. It was my baby step 😂. <br> Usually the bot trains on realtime data from binance api and then makes predictions for the price. Before performing an actual transactions, the bot does some warm-up peredictions and compares results with realtime data to ensure that a high precision. For every pair you want to trade, a different model is created. 

<br>
 It's worth noting that some pairs are easy for the bot to learn patterns while others are really difficult. I tried it on [BTC/USDT] for instance and the performance was terrible. However, it seemed to perform quit well on other pairs like the [BNB/USDT].<br>
  <strong> <mark>Warning!!! the prices for crypto currences are very much volatile and investing in them is not risk free!!!</mark> <br>
  <mark> You can make an indefinate loss! This project or individuals behind it are not trying to promote crypto, trading bots, or anything about trading! The project is just for educational purposes and is intended to showcase how one can train a model on price data. </mark></strong>

## Dependancies
    * TensorFlow
    * Numpy
    * binance
    * matplotlib

## <p> Installing libraries.</p>

```console
    $pip install [library name]
```

## Example:  Installing numpy

```console
    $pip install numpy
```
## Installing binance from pip.

```console
    $python -m pip install --upgrade binance
```
## Contributing

This project welcomes all constructive contributions. Contributions take many forms,
from code for bug fixes and enhancements, to additions and fixes to documentation, additional
tests, triaging incoming pull requests and issues, and more!

## People

Author and maintainer [benkimz](https://github.com/benkimz)

## License

  [MIT](LICENSE)