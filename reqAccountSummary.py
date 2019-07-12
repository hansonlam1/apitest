#very basic attempt to get account information
from ibapi.wrapper import EWrapper
from ibapi.client import EClient
#from threading import Thread
import queue    #queue is a requirement for ibapi python

class IBEWrapper(EWrapper):
    
    def init_AccountSummary(self):
        accountSummaryQ = queue.Queue() #create the queue to receive account summary info
        self._accountSummaryQ = accountSummaryQ

        return accountSummaryQ

    #we need to put the information coming from the reAccountSummary into a queue
    def accountSummary(self, reqId, account, tag, value, currency):
        #put the values in a tuple and add it to the queue
        summaryrow = (reqId, account, tag, value, currency)
        self._accountSummaryQ.put(summaryrow)   #note the underscore in _accountSummaryQ
        
class IBClient(EClient):

    def __init__(self,wrapper):
        EClient.__init__(self,wrapper)  #matches the init of EClient
    
    def getAccountSummary(self, reqId, group, tags):
        acctsumq = self.wrapper.init_AccountSummary() #queue that gets the summary

        self.reqAccountSummary(reqId,group,tags)
        print("trying to get the number")        
        #the values should get put into the queue by ibEWrapper.accountSummary
        MAX_WAIT_SECONDS = 10

        try:
            accountsummaryitem = acctsumq.get(timeout=MAX_WAIT_SECONDS)
        except queue.Empty:
            print("Exceeded maximum wait for wrapper to respond")
            accountsummaryitem = "nothing here"
        
        return accountsummaryitem

    def Close(self):
        EClient.Close()

#create a class for the main app, consisting of the EClient and the EWrapper
class IBApp(IBEWrapper, IBClient):
    def __init__(self, ipaddress, portid, clientid):
        IBEWrapper.__init__(self)
        IBClient.__init__(self, wrapper=self)        #we pass in self as we are using the EWrapper functions built into ibapp since it inherits from EWrapper

        #self.init_error()
        self.connect(ipaddress, portid, clientid)

        thread = Thread(target = self.run)
        thread.start()

        setattr(self, "_thread", thread)
    
#if __name__ == '__main__':
runapp = IBApp("127.0.0.1", 7496, 99)   #connection settings
runapp.startApi()   #documentation mentions a run function but the class definition only shows startApi()
x = runapp.getAccountSummary(1,"All","NetLiquidation")
print(x)
runapp.Close()
runapp.disconnect()