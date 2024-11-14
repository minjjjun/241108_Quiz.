import matplotlib.pyplot as plt

labels = ['English', 'Math', 'Science', 'History']
sizes = [40, 30, 15, 10]

plt.clf()

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightblue','lightgreen','lightcoral','lightsalmon'])

plt.title('Subjects Distribution')

plt.savefig('./results/pie_chart.png')

plt.show()