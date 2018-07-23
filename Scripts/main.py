from Scripts.LogParser import *
from Scripts.UserLogIO import *
from Scripts.LogAnalyser import *



#required class objects
logIO = UserLogIO()
logParser = LogParser()


#load log file
rawLog = logIO.loadLog('../Datasets/Pilot_User_Study/user2_study1.log')


#log analyser class object
logAnalyser = LogAnalyser(rawLog)





chatCount = logAnalyser.get_P2P_communication_count()

print('Chat Counts -> ' + str(chatCount))

chatPar = logAnalyser.get_P2P_communication_percentage()


print('Chat Counts -> ' + str(chatPar) + "%")




