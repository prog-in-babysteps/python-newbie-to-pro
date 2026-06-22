import matplotlib.pyplot as plt

# Define the X-axis (Months)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Define Y-axis data (Average monthly temperatures in °C for Tamil Nadu cities)
# Note: These are representative historical averages
chennai_temps = [24, 25, 28, 31, 33, 33, 31, 30, 30, 29, 27, 25]
madurai_temps = [24, 26, 29, 32, 34, 33, 31, 30, 29, 28, 26, 24]
coimbatore_temps = [23, 24, 26, 28, 29, 27, 26, 26, 25, 24, 23, 22]

# Create the line chart
plt.figure(figsize=(10, 6)) # Sets the figure size

plt.plot(months, chennai_temps, marker='o', color='red', label='Chennai', linewidth=2)
plt.plot(months, madurai_temps, marker='s', color='orange', label='Madurai', linewidth=2)
plt.plot(months, coimbatore_temps, marker='^', color='green', label='Coimbatore', linewidth=2)

# Add titles and axis labels
plt.title('Average Monthly Temperatures of Major Cities in Tamil Nadu', fontsize=14)
plt.xlabel('Months of the Year', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)

# Add a grid, legend, and layout adjustments
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

# Display the chart
plt.show()
