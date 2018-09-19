from Scripts.LogParser import *
from Scripts.UserLogIO import *
from Scripts.LogAnalyser import *



#required class objects
logIO = UserLogIO()
logParser = LogParser()


#load log file
rawLog = logIO.loadLog('/home/gom766/Documents/My_Research_Projects/MyGitRepo/SciWorCS_User_Study_Result_Analysis/Datasets/CHI19_Datasets/CHI 2019 (work)/Study 2/Participant 3/participant_3_task3.log')


#log analyser class object
logAnalyser = LogAnalyser(rawLog)





chatCount = logAnalyser.get_P2P_communication_count()
print('Chat Counts => ' + str(chatCount))

acc_reqCount = logAnalyser.get_floor_request_count() + logAnalyser.get_subworkflow_lock_request_counts()
print('Total Acc. Req. Count => ' + str(acc_reqCount))


moduleAdditionCount = logAnalyser.get_module_addition_count()
print( 'Module Addition Count => ' + str(moduleAdditionCount))



datalinkAdditionCount = logAnalyser.get_datalink_added_count()
print( 'Datalink Addition Count => ' + str(datalinkAdditionCount))



moduleRemoveCount = logAnalyser.get_module_deletion_count()
print( 'Module Remove Count => ' + str(moduleRemoveCount))



datalinkRemoveCount = logAnalyser.get_datalink_deleted_count()
print( 'Datalink Remove Count => ' + str(datalinkRemoveCount))



configUpdateCount = logAnalyser.get_module_config_update_count()
print( 'Config Update Count => ' + str(configUpdateCount))


totalEdits = moduleAdditionCount + datalinkAdditionCount + moduleRemoveCount + datalinkRemoveCount + configUpdateCount
print( 'Total Edit Count => ' + str(totalEdits))


moduleMovedCount = logAnalyser.get_module_move_counts()
print ( 'Module Move Count => ' + str(moduleMovedCount))





#print ('===========================================================')




#required class objects
logIO = UserLogIO()
logParser = LogParser()


#load log file
rawLog = logIO.loadLog('/home/gom766/Documents/My_Research_Projects/MyGitRepo/SciWorCS_User_Study_Result_Analysis/Datasets/CHI19_Datasets/CHI 2019 (work)/Study 2/Participant 8/Participant_task3.log')


#log analyser class object
logAnalyser = LogAnalyser(rawLog)





chatCount2 = logAnalyser.get_P2P_communication_count()
#print('Chat Counts => ' + str(chatCount))

acc_reqCount2 = logAnalyser.get_floor_request_count() + logAnalyser.get_subworkflow_lock_request_counts()
#print('Total Acc. Req. Count => ' + str(acc_reqCount))


moduleAdditionCount2 = logAnalyser.get_module_addition_count()
#print( 'Module Addition Count => ' + str(moduleAdditionCount))



datalinkAdditionCount2 = logAnalyser.get_datalink_added_count()
#print( 'Datalink Addition Count => ' + str(datalinkAdditionCount))



moduleRemoveCount2 = logAnalyser.get_module_deletion_count()
#print( 'Module Remove Count => ' + str(moduleRemoveCount))



datalinkRemoveCount2 = logAnalyser.get_datalink_deleted_count()
#print( 'Datalink Remove Count => ' + str(datalinkRemoveCount))



configUpdateCount2 = logAnalyser.get_module_config_update_count()
#print( 'Config Update Count => ' + str(configUpdateCount))


totalEdits2 = moduleAdditionCount2 + datalinkAdditionCount2 + moduleRemoveCount2 + datalinkRemoveCount2 + configUpdateCount2
#print( 'Total Edit Count => ' + str(totalEdits))


moduleMovedCount2 = logAnalyser.get_module_move_counts()
#print ( 'Module Move Count => ' + str(moduleMovedCount))



print('===============================RATIO=====================================')


print (float(chatCount)/float(chatCount + chatCount2))
print (float(acc_reqCount)/float(acc_reqCount + acc_reqCount2))
print (float(moduleAdditionCount)/float(moduleAdditionCount + moduleAdditionCount2))
print (float(datalinkAdditionCount)/float(datalinkAdditionCount + datalinkAdditionCount2))
print (float(moduleRemoveCount)/float(moduleRemoveCount + moduleRemoveCount2))
print ('0') #print (float(datalinkRemoveCount)/float(datalinkRemoveCount + datalinkRemoveCount2))
print (float(configUpdateCount)/float(configUpdateCount + configUpdateCount2))
print (float(totalEdits)/float(totalEdits + totalEdits2))
print (float(moduleMovedCount)/float(moduleMovedCount + moduleMovedCount2))


print('==========================================================================')

print (1- float(chatCount)/float(chatCount + chatCount2))
print (1- float(acc_reqCount)/float(acc_reqCount + acc_reqCount2))
print (1- float(moduleAdditionCount)/float(moduleAdditionCount + moduleAdditionCount2))
print (1- float(datalinkAdditionCount)/float(datalinkAdditionCount + datalinkAdditionCount2))
print (1- float(moduleRemoveCount)/float(moduleRemoveCount + moduleRemoveCount2))
print ('0') #print (float(datalinkRemoveCount)/float(datalinkRemoveCount + datalinkRemoveCount2))
print (1- float(configUpdateCount)/float(configUpdateCount + configUpdateCount2))
print (1- float(totalEdits)/float(totalEdits + totalEdits2))
print (1- float(moduleMovedCount)/float(moduleMovedCount + moduleMovedCount2))

