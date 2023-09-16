import matplotlib.pyplot as plt
import sqlite3

# Initialize empty lists to store the data
years = []
co2 = []
temp = []

# Connect to the database (replace 'path/to/climate.db' with the actual path to your database file)
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

# Write a query to fetch all data from the ClimateData table
query = "SELECT * FROM ClimateData"

# Execute the query and fetch the data
cursor.execute(query)
data = cursor.fetchall()

# Close the database connection
conn.close()

# Populate the years, co2, and temp lists with the fetched data
for row in data:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

# Plotting the CO2 levels over the years
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

# Plotting the temperatures over the years
plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

# Save the plot as a PNG file (before plt.show())
plt.savefig("co2_temp_1.png")

# Display the plot
plt.show()
