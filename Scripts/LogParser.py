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