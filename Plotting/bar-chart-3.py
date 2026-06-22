import matplotlib.pyplot as plt
import numpy as np

# Define the X-axis (Months)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Define Y-axis data
chennai_temps = [24, 25, 28, 31, 33, 33, 31, 30, 30, 29, 27, 25]
madurai_temps = [24, 26, 29, 32, 34, 33, 31, 30, 29, 28, 26, 24]
coimbatore_temps = [23, 24, 26, 28, 29, 27, 26, 26, 25, 24, 23, 22]

# 1. Convert the month categories into numerical indices
x = np.arange(len(months))

# 2. Define the width of each individual bar
width = 0.25 

plt.figure(figsize=(12, 6))

# 3. Plot each city by shifting its x position
plt.bar(x - width, chennai_temps, width=width, color='red', label='Chennai')
plt.bar(x, madurai_temps, width=width, color='orange', label='Madurai')
plt.bar(x + width, coimbatore_temps, width=width, color='green', label='Coimbatore')

# 4. Replace the numerical indices on the X-axis with the actual month names
plt.xticks(x, months)

# Add styling and labels
plt.title('Average Monthly Temperatures in Tamil Nadu Cities', fontsize=14)
plt.xlabel('Months', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Clean up layout
plt.tight_layout()
plt.show()
