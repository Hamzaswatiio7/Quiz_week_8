import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('C:\\Users\\Msi\\Downloads\\Quiz_week_8-main\\Quiz_week_8-main\\Quiz_week_8\\climate.csv')


years = data['Year'].tolist()
co2 = data['CO2'].tolist()
temp = data['Temperature'].tolist()


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")


plt.savefig("climate_data_q2.png")
plt.show()
