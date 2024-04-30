#!/bin/python3

import requests
import sys
import json

def CurrentExangeRate(CurrencyName):
    return float((json.loads(requests.get(f"http://api.nbp.pl/api/exchangerates/rates/A/{CurrencyName}/").text))["rates"][0]['mid'])

def Last5DaysCurrentExangeRate(CurrencyName):
    lastDays = 5
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{CurrencyName}/last/{lastDays}/"
    fiveDaysCurrency = json.loads(requests.get(url).text)["rates"]
    print(fiveDaysCurrency)
    """
    currencyRates = []
    for iterator in fiveDaysCurrency:
        currencyRates.append(iterator["mid"])
    return currencyRates
    """
    




if __name__ == "__main__":
    # todo: pobieranie nazwy waluty ze standardowego wejscia
    """
    currencyName = "USD"
    currentResponse = CurrentExangeRate(currencyName)
    print(currentResponse)
    """
    print(Last5DaysCurrentExangeRate("USD"))