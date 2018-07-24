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

    def get_config_change_module_id(self, formattedLog):
        moduleAddedDetails = formattedLog.split('=>')[3]  # moduleID:module_id_8
        tmp = moduleAddedDetails.split(":")[1]  # module_id_8
        return tmp.split("_")[2] # 8

    def get_datalink_add_details(self, formattedLog):
        addedDatalinkDetails = formattedLog.split('=>')[3] # from:module_id_7*frompid:multiplication_result.txt*to:module_id_8*topid:second_number.txt
        fromModule = addedDatalinkDetails.split('*')[0] # from:module_id_7
        fromModule = fromModule.split(":")[1] # module_id_7
        fromModule = fromModule.split("_")[2] #7

        toModule = addedDatalinkDetails.split('*')[2] # to:module_id_8
        toModule = toModule.split(":")[1] # module_id_8
        toModule = toModule.split("_")[2] #8


        return {"from":fromModule, "to":toModule}



    def get_module_move_details(self, formattedLog):
        module_moved = formattedLog.split('=>')[3] #key:module_id_8*x:424*y:61
        moduleId = module_moved.split("*")[0] #key:module_id_8
        moduleId = moduleId.split(":")[1] #module_id_8
        moduleId = moduleId.split("_")[2] #8

        newX = module_moved.split("*")[1].split(":")[1] #424
        newY = module_moved.split("*")[2].split(":")[1] #61


        return {"moduleId": moduleId, "x":newX, 'y':newY}


    def get_sub_workflow_lock_request_root(self, formattedLog):
        sub_workflow_root = formattedLog.split('=>')[3] # rootNode:module_id_15
        sub_workflow_root = sub_workflow_root.split(':')[1]
        sub_workflow_root = sub_workflow_root.split('_')[2]

        return sub_workflow_root


    def get_sub_workflow_lock_grant_root(self, formattedLog):
        #reuse, as both of them have the same format in log
        return self.get_sub_workflow_lock_request_root(formattedLog)









