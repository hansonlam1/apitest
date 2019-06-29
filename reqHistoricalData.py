#very basic attempt to get quote information
#going to use the minimum needed and enhance further
#not handling any errors, threading or anything

from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from ibapi.contract import Contract as IBContract
import pandas as pd

class ibEWrapper(EWrapper):
    
    def historicalData(self):
        hist_data = (bar.date, bar.time, bar.close)

        return hist_data

class ibapp(EWrapper, EClient):
    def __init__(self, ipaddress, portid, clientid):
        EWrapper.__init__(self)
        EClient.__init__(self, wrapper=self)

        self.connect(ipaddress, portid, clientid)

#need EWrapper to receive the information
ibwrapper = EWrapper()

#need the EClient to call for data
ibclient = EClient(ibwrapper)

#set the contract
contr = IBContract()
contr.symbol = "MSFT"
contr.secType = "STK"
contr.exchange = "SMART"
contr.primaryExchange = "NASDAQ"
contr.currency = "USD"
contr.conId = 272093

#connection settings
runapp = ibapp("127.0.0.1", 7496, 99)
historic_data = runapp.reqHistoricalData(1, contr, "201906013 12:00:00 GMT", "1 D", "1 hour", "MIDPOINT", 1, 1, False, [])
#df = pd.DataFrame(historic_data)
print(historic_data)
runapp.disconnect()
