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


    def getTime(self, formattedLog):
        return formattedLog.split('=>')[0]