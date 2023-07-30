'''backtest
backtest
start: 2018-05-01 00:00:00
end: 2018-05-05 00:00:00
period: 15m
exchanges: [{"eid":"Futures_CTP","currency":"FUTURES"}]
'''
from fmz import *
task = VCtx(__doc__) # initialize backtest engine from __doc__
# print(exchanges[0].GetAccount())
# print(exchange.GetTicker())
# print(task.Join(True)) # print backtest result
# task.Show() # or show backtest chart
exchanges[0].SetContractType("MA888")
print(exchanges[0])
try:
    while 1:
        # print(exchanges[0].GetTicker())

        Sleep(1000 * 60 * 5)
except:
    print(task.Join(True))