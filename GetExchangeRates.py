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
        time.sleep(10)

def UpdateExchangeRates() -> dict:
    global exchangeRates
    Print("Updating of exchange rates has started.", "S")
    try:
        url = "http://data.fixer.io/api/latest?access_key=" + apiKey
        response = requests.get(url)
        exchangeRates = response.json()['rates']

        UpdateExchangeRatesDB(exchangeRates.copy())
        Print("Updating of exchange rates is successfull.", "S")
    except:
        Print("Updating ER failed.", "E")
        Print("Using exchange rates from DB.", "S")
        exchangeRates = GetExchangeRates()
    return exchangeRates.copy()

def UpdateCryptoRates() -> dict:
    global cryptoRates
    Print("Updating of crypto rates has started.", "S")
    try:
        url = "https://api.binance.com/api/v3/ticker/price"
        response = requests.get(url)
        cryptoRates = {}
        for pair in response.json():
            if pair['symbol'].find("USDT") != -1 and any(pair['symbol'][:-4] == s for s in cryptoList):
                cryptoRates[pair['symbol'][:-4]]=float(pair['price'])
        UpdateCryptoRatesDB(cryptoRates.copy())
        Print("Updating of exchange rates is successfull.", "S")
    except:
        Print("Updating CR failed.", "E")
        Print("Using crypto rates from DB.", "S")
        cryptoRates = GetCryptoRates()
    return cryptoRates.copy()