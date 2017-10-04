import matplotlib.pyplot as plt

x1 = [2, 4, 6, 8, 10]
y1 = [6, 7, 8, 2, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

plt.bar(x1, y1, label='Bars1', color='b')
plt.bar(x2, y2, label='Bars2', color='r')

plt.xlabel('Plot Number')
plt.ylabel('Important bar')

plt.title('Interesting Graph\nCheck it out!')

plt.legend()

plt.show()
