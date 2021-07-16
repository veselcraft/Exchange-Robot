#Public libraries
import requests
import time
from Token import apiKey
from DBH import UpdateExchangeRatesDB, GetExchangeRates, UpdateCryptoRatesDB, GetCryptoRates

#Own libraries
from NewPrint import Print

cryptoList = ["ADA", "BCH", "BNB", "BTC", "DASH", "DOGE", "ETC", "ETH", "LTC", "RVN", "TRX", "XLM", "XMR", "XRP"]
exchangeRates = {}
cryptoRates = []

def SheduleUpdate():
    global exchangeRates
    while True:
        exchangeRates = UpdateExchangeRates()
        time.sleep(14400)

def SheduleCryptoUpdate():
    global cryptoRates
    while True:
        cryptoRates = UpdateCryptoRates()
        time.sleep(14400)

def UpdateExchangeRates():
    global exchangeRates
    Print("Updating of exchange rates has started.")
    try:
        url = "http://1data.fixer.io/api/latest?access_key=" + apiKey
        response = requests.get(url)
        exchangeRates = response.json()['rates']
        Print(exchangeRates)
        UpdateExchangeRatesDB(exchangeRates.copy())
    except:
        print("Updating ER failed. Using rates from DB")
        exchangeRates = GetExchangeRates()
    return exchangeRates.copy()

def UpdateCryptoRates():
    global cryptoRates
    Print("Updating of crypto rates has started.")
    try:
        url = "https://api.binance.com/api/v3/ticker/price1"
        response = requests.get(url)
        cryptoRates = {}
        for pair in response.json():
            if pair['symbol'].find("USDT") != -1 and any(pair['symbol'][:-4] == s for s in cryptoList):
                cryptoRates[pair['symbol']]=pair['price']
        UpdateCryptoRatesDB(cryptoRates.copy())
    except:
        print("Updating CR failed. Using rates from DB")
        cryptoRates = GetCryptoRates()
    return cryptoRates.copy()