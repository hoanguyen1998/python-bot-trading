"""
Algo Trading with Angel SMART API
UDEMY Course: An Electronic Market Making Strategy
Author: Cyriac Kodath  www.algotrader.online
"""

from smartapi import SmartConnect
import urllib
import json

instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
response = urllib.request.urlopen(instrument_url)
instrument_list = json.loads(response.read())

exchange = ["BSE", "NSE"]

def stock_lookup(ticker, instrument_list, exchange):
    data = []
    for instrument in instrument_list:
        if instrument["name"] == ticker and ((instrument["exch_seg"] == exchange[0]) or (instrument ["exch_seg"] == exchange[1] and instrument["symbol"].split('-')[-1] == "EQ")):
            data.append([instrument["exch_seg"], \
                         instrument["symbol"], \
                         instrument["token"]
                         ])
    return data

stock_details = stock_lookup("RELIANCE", instrument_list, exchange)
print(stock_details)