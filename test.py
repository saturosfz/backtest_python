'''backtest
backtest
start: 2019-09-19 00:00:00
end: 2019-09-28 12:00:00
period: 15m
exchanges: [{"eid":"Futures_OKCoin","currency":"BTC_USD", "stocks":1}, {"eid":"OKEX","currency":"BTC_USDT","balance":10000,"stocks":0}]
'''
from fmz import *
task = VCtx(__doc__) # initialize backtest engine from __doc__
# print(exchanges[0].GetAccount())
# print(exchange.GetTicker())
# print(task.Join(True)) # print backtest result
# task.Show() # or show backtest chart
exchanges[0].SetContractType("quarter")
try:
    while 1:
        initQuarterAcc = exchanges[0].GetAccount()

        initSpotAcc = exchanges[1].GetAccount()

        quarterTicker1 = exchanges[0].GetTicker()
        spotTicker1 = exchanges[1].GetTicker()

        exchanges[0].SetDirection("sell") 
        quarterId1 = exchanges[0].Sell(quarterTicker1.Buy, 10)

        spotAmount = 10 * 100 / quarterTicker1.Buy
        spotId1 = exchanges[1].Buy(spotTicker1.Sell, spotAmount)

        Sleep(1000 * 60 * 60 * 24 * 7)

        quarterTicker2 = exchanges[0].GetTicker()
        spotTicker2 = exchanges[1].GetTicker()

        exchanges[0].SetDirection("closesell")
        quarterId2 = exchanges[0].Buy(quarterTicker2.Sell, 10)

        spotId2 = exchanges[1].Sell(spotTicker2.Buy, spotAmount)

        Sleep(1000 * 60 * 60 * 24 * 7)
except:
    print(task.Join(True))