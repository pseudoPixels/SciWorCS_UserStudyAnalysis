import re


class LogParser:
    def __init__(self):
        pass

    def transformRawToRequiredFormat(self, rawLogEntry):
        res = ''
        spaceSplit = rawLogEntry.split(' ')

        for i in range(len(spaceSplit)):
            aSplit = spaceSplit[i]
            if re.match(r'^telepointer', aSplit):
                continue
            aSplit = aSplit.strip()

            if res == '':
                res = res + aSplit+"=>"
            else:
                res = res +  aSplit

        return res


    ##  15:19:18.183=>john@gmail.com=>P2P_CHAT_SENT=>to:darin_gmail_com*text:Hi.
    def getTime(self, formattedLog):
        return formattedLog.split('=>')[0]


    ##  15:19:18.183=>john@gmail.com=>P2P_CHAT_SENT=>to:darin_gmail_com*text:Hi.
    def getLogUser(self, formattedLog):
        return formattedLog.split('=>')[1]


    ##  15:19:18.183=>john@gmail.com=>P2P_CHAT_SENT=>to:darin_gmail_com*text:Hi.
    def getEventType(self, formattedLog):
        return formattedLog.split('=>')[2]


    ##  15:19:18.183=>john@gmail.com=>P2P_CHAT_SENT=>to:darin_gmail_com*text:Hi.
    def getEventDetails(self, formattedLog):
        return formattedLog.split('=>')[3]





    def get_P2P_sent_user(self, formattedLog):
        P2P_event_details = formattedLog.split('=>')[3]
        sent_to_info = P2P_event_details.split('*')[0]#to:darin_gmail_com
        return sent_to_info.split(':')[1]

    def get_P2P_sent_text(self, formattedLog):
        P2P_event_details = formattedLog.split('=>')[3]
        pre_text_len = 10 + len( self.get_P2P_sent_user(formattedLog) ) # to:_______*text: <== 9

        return P2P_event_details[pre_text_len-1:]


    def get_added_module_id(self, formattedLog):
        moduleAddedDetails = formattedLog.split('=>')[3] #module_id:7

        return moduleAddedDetails.split(":")[1]