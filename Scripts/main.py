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
print('Chat Counts => ' + str(chatCount))


chatPar = logAnalyser.get_P2P_communication_percentage()
print('Communication Parcentage => ' + str(round(chatPar,2)) + " %")



floorAccessTime = logAnalyser.get_floor_accessed_time()
print('Floor Access Time => ' + str(floorAccessTime) + ' ms')


totalLogTime = logAnalyser.get_total_log_time()
print('Total Session Time => ' + str(totalLogTime) + ' ms')


accessP = logAnalyser.get_floor_access_percentage()
print("Floor Access Percentage => " + str(round(accessP, 2)) + " %")


#print(logAnalyser.get_P2P_all_sent_texts())
print('Total Subworkflow Locks => '+ str(logAnalyser.get_total_subworkflow_req_access_waiting_time()))


module_addition_count = logAnalyser.get_module_addition_count()
print('Module Addition Count => ' + str(module_addition_count))


total_workflow_edit_operations = logAnalyser.get_total_edit_operations_on_workflow_object()
print('Total Workflow Edit Operations => ' + str(total_workflow_edit_operations))