import numpy as a
import pandas as b
import matplotlib.pyplot as plt

num_points = 1000
x_coords = a.random.randint(0, 1001, num_points)
y_coords = a.random.randint(0, 1001, num_points)
df = b.DataFrame({'X': x_coords, 'Y': y_coords})

excel_file = 'koordinatlar.xlsx'
df.to_excel(excel_file, index=False)

df = b.read_excel(excel_file)


x_coords = df['X']
y_coords = df['Y']
grid_size = 200
num_grids = (1000 // grid_size) + 1
colors = plt.cm.tab20(a.linspace(0, 1, num_grids**2))

plt.figure(figsize=(10, 10))


for i in range(0, 1000, grid_size):
    for j in range(0, 1000, grid_size):
        mask = (x_coords >= i) & (x_coords < i + grid_size) & (y_coords >= j) & (y_coords < j + grid_size)
        color_index = (i // grid_size) * num_grids + (j // grid_size)
        plt.scatter(x_coords[mask], y_coords[mask], color=colors[color_index])

plt.xlabel('X Koordinatları')
plt.ylabel('Y Koordinatları')
plt.title('Rastgele Noktaların Izgara Üzerinde Görselleştirilmesi')
plt.grid(True)
plt.show()
