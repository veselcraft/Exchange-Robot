#Public libraries
import requests
import time
from Token import apiKey
from DBH import UpdateExchangeRatesDB, GetExchangeRates,UpdateCryptoRatesDB, GetCryptoRates

#Own libraries
from NewPrint import Print

cryptoList =["BTC","ETH","BNB","XRP","DOGE","BCH","LTC","ETC","XLM","TRX","XMR","DASH","RVN","ADA"]

def SheduleUpdate():
    global exchangeRates
    while True:
        exchangeRates = UpdateExchangeRates()
        time.sleep(7200)

def UpdateExchangeRates():
    Print("Updating of exchange rates has started.")
    try:
        url = "http://data.fixer.io/api/latest?access_key=" + apiKey
        response = requests.get(url)
        exchangeRates = response.json()['rates']
        Print(exchangeRates)
        UpdateExchangeRatesDB(exchangeRates.copy())
    except:
        Print("Updating failed. Using rates from DB")
        exchangeRates = GetExchangeRates()

    return exchangeRates.copy()

def UpdateCryptoRates():
    Print("Updating of crypto rates has started.")
    try:
        url = "https://api.binance.com/api/v3/ticker/price"
        response = requests.get(url)
        cryptoRates = {}
        for pair in response.json():
            if pair['symbol'].find("USDT") != -1 and any(pair['symbol'][:-4] == s for s in cryptoList):
                cryptoRates[pair['symbol']]=pair['price']
        UpdateCryptoRatesDB(cryptoRates.copy())
    except:
        Print("Updating failed. Using rates from DB")
        cryptoRates = GetCryptoRates()
    return cryptoRates.copy()
