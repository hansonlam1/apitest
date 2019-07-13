#get a set of historical data from IB

from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from threading import Thread
import queue    #queue is a requirement for ibapi python

class IBEWrapper(EWrapper):
    
    def init_getHistoricalData(self):
        histDataQ = queue.Queue() #create a queue to receive info
        self._histDataQ = histDataQ

        return histDataQ

#    override the EWrapper method to put the information coming into a queue
    def historiclData(self, reqId, bar)
        #takes the incoming data and put it in a queue
        #the EClient method call takes it out of the queue


class IBClient(EClient):

    def __init__(self,wrapper):
        EClient.__init__(self,wrapper)  #matches the init of EClient
    
#    override the method to call the functions in EClient, for example:   
    def getHistoricalData(self,contract,endDateTime,durationString,barSizeSetting,whatToShow,useRTH,formatDate,keepUptoDate,List)
        histdata = self.wrapper.init_getHistoricalData()    #queue that has the incoming data

        self.reqHistoricalData(self,contract,endDateTime,durationString,barSizeSetting,whatToShow,useRTH,formatDate,keepUptoDate,List)
        print("Getting the info")
        MAX_WAIT_SECONDS = 10

        try:
            histDataItem = histdata.get(timeout=MAX_WAIT_SECONDS)
        except queue.Empty:
            print("Timed Out")
            histDataItem = "No Data Items"

        return histData

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

#establish which contract we want to get information for

#get the information





#print(x)

runapp.Close()
runapp.disconnect()