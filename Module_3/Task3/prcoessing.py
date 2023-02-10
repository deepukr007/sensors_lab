import numpy as np
import matplotlib.pyplot as plt
import random

loaded = np.load('outfileiaq.npz')
iaq = loaded['iaq']
co2 = loaded['co2']
hour = loaded['hour']
minute = loaded['minute']



range = np.arange(30 , (2880*30)+30, 30 , dtype=float)/3600


plt.figure(1)
plt.plot( range , iaq[0:2880] , color = 'red')
plt.rcParams["figure.autolayout"] = True
plt.xticks(np.arange(0,24))
plt.xlabel('Time in m')
plt.ylabel("IAQ" )
plt.title('Gas sensor readings')
plt.savefig('new'+'IAQ' )


plt.show() 