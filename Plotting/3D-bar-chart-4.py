import matplotlib.pyplot as plt
import numpy as np

# Define the X-axis (Months)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Define temperature data (Z-axis values)
chennai_temps = [24, 25, 28, 31, 33, 33, 31, 30, 30, 29, 27, 25]
madurai_temps = [24, 26, 29, 32, 34, 33, 31, 30, 29, 28, 26, 24]
coimbatore_temps = [23, 24, 26, 28, 29, 27, 26, 26, 25, 24, 23, 22]

# 1. Setup the figure and 3D projection
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(1, 1, 1, projection='3d')

# 2. Define X positions (Months numerical indices)
x_indices = np.arange(len(months))

# 3. Define Y positions (City numerical indices)
cities = ['Chennai', 'Madurai', 'Coimbatore']
y_indices = np.arange(len(cities))

# 4. Create arrays for the anchor points (x, y, z)
# Repeat X indices for each city series
xpos = np.tile(x_indices, len(cities))
# Repeat Y indices so each city stays on its own row
ypos = np.repeat(y_indices, len(months))
# All bars start at ground level (Z = 0)
zpos = np.zeros_like(xpos)

# 5. Combine the data lists for the bar heights (Z dimensions)
dz = np.array(chennai_temps + madurai_temps + coimbatore_temps)

# 6. Define the thickness/dimensions of each bar
dx = 0.4  # Width along the Month axis
dy = 0.2  # Depth along the City axis

# 7. Map colors to each city row
colors = ['red'] * len(months) + ['orange'] * len(months) + ['green'] * len(months)

# 8. Plot the 3D bars
# Subtracting dx/2 and dy/2 centers the bars on the tick marks
ax.bar3d(xpos - dx/2, ypos - dy/2, zpos, dx, dy, dz, color=colors, shade=True)

# 9. Customize axes ticks and labels
ax.set_xticks(x_indices)
ax.set_xticklabels(months)

ax.set_yticks(y_indices)
ax.set_yticklabels(cities)

ax.set_xlabel('Months', fontsize=12, labelpad=10)
ax.set_ylabel('Cities', fontsize=12, labelpad=10)
ax.set_zlabel('Temperature (°C)', fontsize=12, labelpad=5)
ax.set_title('Average Monthly Temperatures in Tamil Nadu Cities (3D)', fontsize=14, pad=20)

# Optional: Adjust the camera viewing angle for better depth perception
ax.view_init(elev=25, azim=-60)

plt.tight_layout()

plt.show()
