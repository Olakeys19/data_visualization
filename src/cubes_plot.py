import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=20)

plt.title('Cubes of Numbers', fontsize = 20)
plt.xlabel('Numbers', fontsize=14)
plt.ylabel('Cubes', fontsize=14)
plt.show()