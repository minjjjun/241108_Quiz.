import matplotlib.pyplot as plt
import random

x = [random.uniform(0, 100) for _ in range(200)]
y = [2 * val + 1 + random.uniform(-10, 10) for val in x]

plt.clf()

plt.scatter(x, y, label='Scatter Plot', color='blue', marker='o', s=30, alpha=0.5)

plt.title('Scatter Plot Example')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.savefig("./results/scatter_2.png")

plt.show()


