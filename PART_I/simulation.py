import random
import csv
import sys
import os
class Queue:
    def __init__(self):
        self.Jobs = []

    def isEmpty(self):
        return self.Jobs == []

    def Jobenqueue(self, item):
        self.Jobs.insert(0,item)

    def Jobdequeue(self):
        return self.Jobs.pop()

    def JobSize(self):
        return len(self.Jobs)

class Server:
    def __init__(self, ppm):
        self.requestrate = ppm
        self.currentRequest = None
        self.timeL = 0

    def tick(self):
        if self.currentRequest != None:
            self.timeL = self.timeL - 1
            if self.timeL <= 0:
                self.currentRequest = None

    def busy(self):
        if self.currentRequest != None:
            return True
        else:
            return False

    def startNext(self,newRequest):
        self.currentRequest = newRequest
        self.timeL = newRequest.getrequests() * 60/self.requestrate

class Request:
    def __init__(self,time):
        self.timestamp = time
        self.requests = random.randrange(1,21)

    def getStmp(self):
        return self.timestamp

    def getrequests(self):
        return self.requests

    def takeTime(self, currenttime):
        return currenttime - self.timestamp

def LoadFile(fileName):

    with open(fileName, newline='') as FileCsvFormate:
        filereader = csv.reader(FileCsvFormate)
        fileList = list(filereader)

    return fileList

def simulateOneServer(numSeconds, requestsPerMinute,i2,job):

    labServer = Server(requestsPerMinute)
    JobQueue = Queue()
    takeingtimes = []

    for currentSecond in range(numSeconds):

      if JobRequest():
         request = Request(currentSecond)
         JobQueue.Jobenqueue(request)

      if (not labServer.busy()) and (not JobQueue.isEmpty()):
        nextRequest = JobQueue.Jobdequeue()
        takeingtimes.append( nextRequest.takeTime(currentSecond))
        labServer.startNext(nextRequest)

      labServer.tick()

    averagetake=sum(takeingtimes)/len(takeingtimes)
    print("Average latency  %6.2f secs %3d Requests for  ."%(averagetake,JobQueue.JobSize()),job)

def JobRequest():
    number = random.randrange(1,181)
    if number == 180:
        return True
    else:
        return False




import urllib.request
def main():

    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'
  
    fileDirct = os.path.dirname(os.path.abspath(__file__))
    parentDirct = os.path.dirname(fileDirct)
    
    CSVFileName=parentDirct + '\\PART_I\\requests.csv'



    with urllib.request.urlopen(url) as resp, open(CSVFileName, 'wb') as outfile:
        filedata = resp.read() 
        outfile.write(filedata)

    
    
    InputsJob = LoadFile(CSVFileName)
    
    for lstItem in InputsJob:
     i=0
     i1=0;
     i2=0
     job=''
     for item in lstItem:
         i+=1
         if i==1 :
             i1=item
         if i==2 :
             job=item
         if i==3 :
             i2=item
             simulateOneServer(3600,int(i2),i1,job)


main()
