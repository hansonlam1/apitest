#very basic attempt to get quote information
#going to use the minimum needed and enhance further
#not handling any errors, threading or anything

from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from ibapi.contract import Contract as IBContract
import pandas as pd

#class IBWrapper(EWrapper):
#class IBClient(EClient):


class ibapp(EWrapper, EClient):
    def __init__(self, ipaddress, portid, clientid):
        EWrapper.__init__(self)
        EClient.__init__(self,wrapper=self)

        self.connect(ipaddress, portid, clientid)

#need EWrapper to receive the information
ibwrapper = EWrapper()

#need the EClient to call for data
ibclient = EClient(ibwrapper)

#set the contract
contr = IBContract()
contr.symbol = "MSFT"
contr.secType = "STK"
contr.exchange = "NASDAQ"
contr.currency = "USD"

#connection settings
runapp = ibapp("127.0.0.1",7496,99)
bar = runapp.reqHistoricalData(1,contr,"20190601 11:00:00 GMT","10 D","1 day","MIDPOINT",1,1,False,[])
df = pd.DataFrame(bar)
print(df.head(2))
runapp.disconnect()
