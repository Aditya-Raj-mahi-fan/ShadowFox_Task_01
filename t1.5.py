import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D' , 'E'
sizes = [15, 30, 38, 10, 7]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')
plt. show()