#Public libraries
import requests
import time
from Token import apiKey
from DBH import UpdateExchangeRatesDB, GetExchangeRates

#Own libraries
from NewPrint import Print

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

UpdateExchangeRates()