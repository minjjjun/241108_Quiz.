import matplotlib.pylab as plt

categories = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grape']
values = [25, 30, 15, 20, 35]

plt.clf()

plt.bar(categories, values, color='skyblue')

plt.title('Fruit Sales')

plt.xlabel('Fruits')

plt.ylabel('Sales')

plt.savefig("./results/bar_chart.png")

plt.show()