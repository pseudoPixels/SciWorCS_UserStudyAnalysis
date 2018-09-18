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



plt.subplot(221)
plt.plot([1,2,3,4,5], [20,26,27, 40, 50], marker='.', label='W. Update')
plt.plot([1,2,3,4,5], [19,4,30, 31, 12], marker='.', label='Comms.')
plt.grid(True)
plt.title('Collab. W. Comp. (Session 1)', fontsize=18)
plt.xlabel('Collaborator', fontsize=18)
plt.ylabel('Frequency', fontsize=18)
plt.legend(loc="upper left", fontsize=14)





plt.subplot(222)
plt.plot([1,2,3,4,5], [25,26,5, 25, 21], marker='.', label='W. Update')
plt.plot([1,2,3,4,5], [12,30,13, 21, 12], marker='.', label='Comms.')
plt.grid(True)
plt.title('Collab. W. Comp. (Session 2)', fontsize=18)
plt.xlabel('Collaborator', fontsize=18)
plt.ylabel('Frequency', fontsize=18)
plt.legend(loc="upper right", fontsize=14)





plt.subplot(223)
plt.plot([1,2,3,4,5], [20,26,27, 40, 50], marker='.', label='W. Update')
plt.plot([1,2,3,4,5], [19,4,30, 31, 12], marker='.', label='Comms.')
plt.grid(True)
plt.title('Collab. W. Comp. (Session 3)', fontsize=18)
plt.xlabel('Collaborator', fontsize=18)
plt.ylabel('Frequency', fontsize=18)
plt.legend(loc="upper left", fontsize=14)





plt.subplot(224)
plt.plot([1,2,3,4,5], [20,26,27, 40, 50], marker='.', label='W. Update')
plt.plot([1,2,3,4,5], [19,4,30, 31, 12], marker='.', label='Comms.')
plt.grid(True)
plt.title('Collab. W. Comp. (Whole Collab.)', fontsize=18)
plt.xlabel('Collaborator', fontsize=18)
plt.ylabel('Frequency', fontsize=18)
plt.legend(loc="upper left", fontsize=14)



plt.show()
