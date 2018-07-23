class UserLogIO:
    def __init__(self):
        pass


    def loadLog(self, filePath):
        theLog = ''
        with open(filePath, "r") as f:
            theLog = f.readlines()

        # remove the meta log info line (first line)
        return theLog  # [1:len(simLog):]