#!/bin/python3

import requests
import sys
import json

# assumption: length of columnOne and columnTwo is equal
def TablePrint(headlineOne:str, headlineTwo:str, columnOne:list, columnTwo:list):
    if len(columnOne) != len(columnTwo):
        # if that statement is true, its a critital error
        sys.exit -1

    print(headlineOne+"\t"+"\t"+headlineTwo)
    for iterator in range(len(columnOne)):
        print(str(columnOne[iterator])+"\t"+str(columnTwo[iterator]))

def CurrentExangeRate(CurrencyName:str):
    return float((json.loads(requests.get(f"http://api.nbp.pl/api/exchangerates/rates/A/{CurrencyName}/").text))["rates"][0]['mid'])

def Last5DaysCurrentExangeRate(CurrencyName:str):
    lastDays = 5
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{CurrencyName}/last/{lastDays}/"
    fiveDaysCurrency = json.loads(requests.get(url).text)["rates"]
    
    dates = []
    currencyRates = []
    for iterator in fiveDaysCurrency:
        currencyRates.append(iterator["mid"])
        dates.append(iterator["effectiveDate"])
    TablePrint("Dates", "CurrencyRates", dates, currencyRates)
    

if __name__ == "__main__":
    # todo: pobieranie nazwy waluty ze standardowego wejscia
    """
    currencyName = "USD"
    currentResponse = CurrentExangeRate(currencyName)
    print(currentResponse)
    """
    Last5DaysCurrentExangeRate("USD")