from Scripts.LogParser import *
from Scripts.UserLogIO import *
from Scripts.LogAnalyser import *





import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import NullFormatter  # useful for `logit` scale
from matplotlib.legend_handler import HandlerLine2D

import pandas as pd
import numpy as np



#required class objects
logIO = UserLogIO()
logParser = LogParser()


#load log file
rawLog = logIO.loadLog('../Datasets/Pilot_User_Study/user2_study1.log')


#log analyser class object
logAnalyser = LogAnalyser(rawLog)





chatCount = logAnalyser.get_P2P_communication_count()
print('Chat Counts => ' + str(chatCount))
















plt.figure(1)


m_turn = [1 ,6 ,2 ,7 ,2 ,8 ,9 ]
m_attr = [1 ,8 ,2 ,6 ,3 ,8 ,9 ]


p_turn = [3 ,2 ,3 ,10 ,5 ,9 ,9 ]
p_attr = [2 ,10 ,9 ,2 ,4 ,3 , 2 ]


t_turn = [1 ,4 ,2 ,10 ,4 ,7 ,3]
t_attr = [1 ,4 ,2 ,2 ,1 ,1 ,2 ]


pr_turn = [5 ,6 ,3 ,8 ,8 ,8 ,8 ,8]
pr_attr = [4 ,5 ,1 ,7 ,3 ,7 ,2 ,2]


e_turn = [3 ,7 ,6 ,10 ,6 ,8 ,4 ,8]
e_attr = [5 ,10 ,9 ,10 ,3 ,9 ,9 ,7]


f_turn = [2 ,4 ,3 ,8 ,7 ,7 ,2 ,3]
f_attr = [3 ,3 ,2 ,1 ,3 ,3 ,2 ,8]





bp = plt.boxplot((m_turn,m_attr,  p_turn,p_attr,  t_turn,t_attr,   pr_turn,pr_attr,  e_turn,e_attr,  f_turn,f_attr), labels=['Mental (Turn)','Mental (Attr.)',    'Physical (Turn)','Physical (Attr.)',    'Temporal (Turn)','Temporal (Attr.)',       'Performance (Turn)','Performance (Attr.)',             'Effort (Turn)','Effort (Attr.)',         'Frustration (Turn)','Frustration (Attr.)'], patch_artist=True)

bp['boxes'][0].set( facecolor = '#777777')
bp['boxes'][1].set( facecolor = '#CCCCCC')

bp['boxes'][2].set( facecolor = '#777777')
bp['boxes'][3].set( facecolor = '#CCCCCC')

bp['boxes'][4].set( facecolor = '#777777')
bp['boxes'][5].set( facecolor = '#CCCCCC')

bp['boxes'][6].set( facecolor = '#777777')
bp['boxes'][7].set( facecolor = '#CCCCCC')

bp['boxes'][8].set( facecolor = '#777777')
bp['boxes'][9].set( facecolor = '#CCCCCC')

bp['boxes'][10].set( facecolor = '#777777')
bp['boxes'][11].set( facecolor = '#CCCCCC')




#bp['medians'][0].set( color = '#FFFFFF')

plt.xlabel('Assessment Dimensions', fontsize=18)
plt.ylabel('NASA-TLX Scale', fontsize=18)

plt.xticks(rotation=25)

#plt.xticks(x, ['mental'])




# plt.plot(x, [20,26,27, 40, 50], marker='.', label='W. Update')
# plt.plot([1,2,3,4,5], [19,4,30, 31, 12], marker='.', label='Comms.')
#
# plt.grid(True)
plt.title('NASA-TLX Workload', fontsize=18)
# plt.xlabel('Collaborator', fontsize=18)
# plt.ylabel('Frequency', fontsize=18)
# plt.legend(loc="upper left", fontsize=14)








plt.show()
