import matplotlib.pyplot as plt

x1 = [1,2,3]
y1 = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x1, y1, label='First Line')
plt.plot(x2, y2, label='Second Line')

plt.xlabel('Plot Number')
plt.ylabel('Important bar')

plt.title('Interesting Graph\nCheck it out!')

plt.legend()

plt.show()
