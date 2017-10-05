import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # figure exists by default, to modify it you have to reference it

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

plt.close('all')


f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

#ax1 = plt.subplot2grid((1,2), (0,0)) # First tuple = Shape of Grid, Second tuple = Starting
#ax2 = plt.subplot2grid((1,2), (0,0)) # First tuple = Shape of Grid, Second tuple = Starting

#plt.xlabel('Date')
#plt.ylabel('Price')                
#plt.title('Interesting Graph\nCheck it out!!')
#plt.legend()
#plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()
