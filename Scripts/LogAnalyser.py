from Scripts.LogParser import *
from Scripts.TimeUtility import *


#required class objects
logParser = LogParser()



class LogAnalyser:
    def __init__(self, rawLog):
        self._rawLog = rawLog
        self._totalEventCount = len(self._rawLog)









#################################################################
############  Communication Related Analysis ####################
########################STARTS###################################


    def get_P2P_communication_count(self):
        chatCount = 0

        for i in range(self._totalEventCount):
            formattedLogEntry = logParser.transformRawToRequiredFormat(self._rawLog[i])

            eventType = logParser.getEventType(formattedLogEntry)

            if eventType == 'P2P_CHAT_SENT':
                chatCount += 1

        return chatCount


    def get_P2P_communication_percentage(self):
        return self.get_P2P_communication_count() * 100 / self._totalEventCount


    def get_P2P_sent_text_char_counts(self):
        total_char_counts = 0

        for i in range(self._totalEventCount):
            formattedLogEntry = logParser.transformRawToRequiredFormat(self._rawLog[i])

            eventType = logParser.getEventType(formattedLogEntry)

            if eventType == 'P2P_CHAT_SENT':
                sentText = logParser.get_P2P_sent_text(formattedLogEntry)
                total_char_counts += len(sentText)
                #print(sentText)

        return total_char_counts



    def get_P2P_all_sent_texts(self):
        allTexts = ''
        for i in range(self._totalEventCount):
            formattedLogEntry = logParser.transformRawToRequiredFormat(self._rawLog[i])

            eventType = logParser.getEventType(formattedLogEntry)

            if eventType == 'P2P_CHAT_SENT':
                sentText = logParser.get_P2P_sent_text(formattedLogEntry)
                allTexts += sentText + '\n'

        return allTexts


########################ENDS#####################################
############  Communication Related Analysis ####################
#################################################################





















#################################################################
############  Floor Access Related Analysis #####################
########################STARTS###################################

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


    def get_floor_access_release_time_series(self):
        floor_request_time_stamp = ''
        floor_release_time_stamp = ''
        isFloorRequested = False
        floor_access_release_time_series = []


        for i in range(self._totalEventCount):
            formattedLogEntry = logParser.transformRawToRequiredFormat(self._rawLog[i])

            eventType = logParser.getEventType(formattedLogEntry)

            if eventType == 'FLOOR_REQUESTED':
                floor_request_time_stamp = logParser.getTime(formattedLogEntry)
                isFloorRequested = True
                floor_access_release_time_series.append(floor_request_time_stamp)
            elif eventType == 'FLOOR_RELEASED':
                floor_release_time_stamp = logParser.getTime(formattedLogEntry)
                isFloorRequested = False
                floor_access_release_time_series.append(floor_release_time_stamp)


        #special case: when collaborator requested the floor but never released (i.e., due to the end of experiment)
        if isFloorRequested == True:
            floor_access_release_time_series.append(floor_release_time_stamp)


        return floor_access_release_time_series



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



    #the time between the floor request and its granted access
    def get_total_waiting_time(self):
        floor_request_time_stamp = ''
        total_waiting_time = 0

        for i in range(self._totalEventCount):
            formattedLogEntry = logParser.transformRawToRequiredFormat(self._rawLog[i])

            eventType = logParser.getEventType(formattedLogEntry)

            if eventType == 'FLOOR_REQUESTED':
                floor_request_time_stamp = logParser.getTime(formattedLogEntry)
            elif eventType == 'GOT_THE_FLOOR':
                got_floor_time_stamp = logParser.getTime(formattedLogEntry)
                t_diff = TimeUtility().getTimeDifference(floor_request_time_stamp, got_floor_time_stamp)
                total_waiting_time += t_diff
        return total_waiting_time

########################ENDS#####################################
############  Floor Access Related Analysis #####################
#################################################################


























#################################################################
############ Module Related Analysis ############################
########################STARTS###################################
    def get_module_addition_count(self):
        module_add_count = 0

        for i in range(self._totalEventCount):
            formattedLogEntry = logParser.transformRawToRequiredFormat(self._rawLog[i])

            eventType = logParser.getEventType(formattedLogEntry)

            if eventType == 'MODULE_ADDED':
                module_add_count += 1

        return module_add_count

    def get_added_module_indices(self):
        indices = []

        for i in range(self._totalEventCount):
            formattedLogEntry = logParser.transformRawToRequiredFormat(self._rawLog[i])

            eventType = logParser.getEventType(formattedLogEntry)

            if eventType == 'MODULE_ADDED':
                #print(str(i) + "->")
                indices.append(logParser.get_added_module_id(formattedLogEntry))

        return indices






    def get_module_config_update_count(self):
        module_config_update_count = 0

        for i in range(self._totalEventCount):
            formattedLogEntry = logParser.transformRawToRequiredFormat(self._rawLog[i])

            eventType = logParser.getEventType(formattedLogEntry)

            if eventType == 'MODULE_CONFIG_CHANGE':
                module_config_update_count += 1

        return module_config_update_count


    def get_module_deletion_count(self):
        module_del_count = 0

        for i in range(self._totalEventCount):
            formattedLogEntry = logParser.transformRawToRequiredFormat(self._rawLog[i])

            eventType = logParser.getEventType(formattedLogEntry)

            if eventType == 'MODULE_DELETED':
                module_del_count += 1

        return module_del_count
########################ENDS#####################################
############  Module Related Analysis ###########################
#################################################################


