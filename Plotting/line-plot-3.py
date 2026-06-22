import matplotlib.pyplot as plt

# Define the X-axis (Months)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Define the Y-axis (Temperature - Celcius)
chennai_temps = [24, 25, 28, 31, 33, 33, 31, 30, 30, 29, 27, 25]

# Add Marker, Color, Label and Line Width
plt.plot(months, chennai_temps, marker='o', color='red', label='Chennai', linewidth=2)

# Add titles and axis labels
plt.title('Average Monthly Temperatures of Chennai', fontsize=14)
plt.xlabel('Months of the Year', fontsize=12)
plt.ylabel('Temperature(Celcius)', fontsize=12)

# Show Legend
plt.legend()

# Display the chart
plt.show()
