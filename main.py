import pandas as pd
import matplotlib.pyplot as plt

# Load the criminal data
criminal_data = pd.read_csv('./data/crimereport.xlsx')

# Load the unemployment data
unemployment_data = pd.read_csv('./data/unemploed.xlsx')

# Plotting criminal data
plt.figure(figsize=(10, 6))
plt.bar(criminal_data['Year'], criminal_data['Crime Rate'])
plt.title('Crime Rate by Year')
plt.xlabel('Year')
plt.ylabel('Crime Rate')
plt.show()

# Plotting unemployment data
plt.figure(figsize=(10, 6))
plt.plot(unemployment_data['Year'], unemployment_data['Unemployment Rate'], marker='o')
plt.title('Unemployment Rate by Year')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.grid(True)
plt.show()

print("hello")