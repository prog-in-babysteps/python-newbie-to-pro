import matplotlib.pyplot as plt

# Define the X-axis (Months)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Define the Y-axis (Temperature - Celcius)
chennai_temps = [24, 25, 28, 31, 33, 33, 31, 30, 30, 29, 27, 25]

plt.bar(months, chennai_temps)

# Add titles and axis labels
plt.title('Average Monthly Temperatures of Chennai', fontsize=14)
plt.xlabel('Months of the Year', fontsize=12)
plt.ylabel('Temperature', fontsize=12)

# Display the chart
plt.show()
