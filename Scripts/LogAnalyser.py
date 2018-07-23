from Scripts.LogParser import *
from Scripts.TimeUtility import *


#required class objects
logParser = LogParser()



class LogAnalyser:
    def __init__(self, rawLog):
        self._rawLog = rawLog
        self._totalEventCount = len(self._rawLog)




    def get_P2P_communication_count(self):
        chatCount = 0


        for i in range(self._totalEventCount):
            formattedLogEntry = logParser.transformRawToRequiredFormat(self._rawLog[i])

            eventType = logParser.getEventType(formattedLogEntry)

            if eventType == 'P2P_CHAT_SENT':
                chatCount += 1

        return chatCount


    def get_P2P_communication_percentage(self):
        totalEventCount = len(self._rawLog)

        return self.get_P2P_communication_count() * 100 / self._totalEventCount


    



    def get_floor_accessed_time(self):

        elapsedTime = 0
        floor_request_time_stamp = ''
        floor_release_time_stamp = ''
        isFloorRequested = False


        for i in range(self._totalEventCount):
            formattedLogEntry = logParser.transformRawToRequiredFormat(self._rawLog[i])

            eventType = logParser.getEventType(formattedLogEntry)

            if eventType == 'FLOOR_REQUESTED':
                floor_request_time_stamp = logParser.getTime(formattedLogEntry)
                isFloorRequested = True
            elif eventType == 'FLOOR_RELEASED':
                floor_release_time_stamp = logParser.getTime(formattedLogEntry)
                timeDiff = TimeUtility().getTimeDifference(floor_request_time_stamp, floor_release_time_stamp)
                elapsedTime += timeDiff
                isFloorRequested = False

        #special case: when collaborator requested the floor but never released (i.e., due to the end of experiment)
        if isFloorRequested == True:
            timeDiff = TimeUtility.getTimeDifference(floor_request_time_stamp, logParser.transformRawToRequiredFormat(self._rawLog[self._totalEventCount-1]))
            elapsedTime += timeDiff


        return elapsedTime



    #total time in between the start and end of the log
    def get_total_log_time(self):
        formattedLogEntry_start = logParser.transformRawToRequiredFormat(self._rawLog[0])
        formattedLogEntry_end = logParser.transformRawToRequiredFormat(self._rawLog[self._totalEventCount-1])

        start_time = logParser.getTime(formattedLogEntry_start)
        end_time = logParser.getTime(formattedLogEntry_end)

        return TimeUtility().getTimeDifference(start_time, end_time)



    #the time ratio of this user's floor access time
    def get_floor_access_percentage(self):
        return self.get_floor_accessed_time() * 100 / self.get_total_log_time()
