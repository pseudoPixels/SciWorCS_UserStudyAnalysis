from Scripts.LogParser import *



#required class objects
logParser = LogParser()



class LogAnalyser:
    def __init__(self, rawLog):
        self.rawLog = rawLog




    def get_P2P_communication_count(self):
        chatCount = 0
        totalEventCount = len(self.rawLog)

        for i in range(totalEventCount):
            formattedLogEntry = logParser.transformRawToRequiredFormat(self.rawLog[i])

            eventType = logParser.getEventType(formattedLogEntry)

            if eventType == 'P2P_CHAT_SENT':
                chatCount += 1

        return chatCount


    def get_P2P_communication_percentage(self):
        totalEventCount = len(self.rawLog)

        return self.get_P2P_communication_count() * 100 / totalEventCount