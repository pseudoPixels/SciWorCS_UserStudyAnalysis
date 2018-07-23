from datetime import datetime

class TimeUtility:
    def __init__(self):
        pass



    def getTimeDifference(self, startTime, endTime):
        a = datetime.strptime(startTime, '%H:%M:%S.%f')
        b = datetime.strptime(endTime, '%H:%M:%S.%f')

        return  abs((a-b).total_seconds()*1000)

