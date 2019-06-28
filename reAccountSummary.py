#very basic attempt to get account information
from ibapi.wrapper import EWrapper
from ibapi.client import EClient

class ibEWrapper(EWrapper):

    #we can override the EWrapper functions we are calling to customize them a bit here


class ibClient(EClient):

    def __init__(self,wrapper):
        EClient.__init__(self,wrapper)  #matches the init of EClient
    

#create a class for the main app, consisting of the EClient and the EWrapper
class ibapp(ibEWrapper, ibClient):
    def __init__(self, ipaddress, portid, clientid):
        EWrapper.__init__(self)
        EClient.__init__(self, wrapper=self)        #we pass in self as we are using the EWrapper functions built into ibapp since it inherits from EWrapper

        self.connect(ipaddress, portid, clientid)

#connection settings
runapp = ibapp("127.0.0.1", 7496, 99)

runapp.disconnect()