from Scripts.LogParser import *
from Scripts.UserLogIO import *



#required class objects
logIO = UserLogIO()
logParser = LogParser()


#load log file
aLog = logIO.loadLog('../Datasets/Pilot_User_Study/user2_study1.log')


formattedLogEntry = logParser.transformRawToRequiredFormat(aLog[1])

print(logParser.getTime(formattedLogEntry))

