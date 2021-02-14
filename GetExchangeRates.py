#Public libraries
import requests
import time
from Token import apiKey

#Own libraries
from NewPrint import Print

def SheduleUpdate():
    global exchangeRates
    while True:
        exchangeRates = UpdateExchangeRates()
        time.sleep(7200)

def UpdateExchangeRates():
    Print("Updating of exchange rates has started.")
    url = "http://data.fixer.io/api/latest?access_key=" + apiKey
    response = requests.get(url)
    exchangeRates = response.json()['rates']
    Print(exchangeRates)
    return exchangeRates.copy()