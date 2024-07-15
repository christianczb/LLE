import pandas as pd
import matplotlib.pyplot as plt

# Define the URL of the CSV file in the GitHub repository for LLE_data2.csv
url2 = 'https://raw.githubusercontent.com/christianczb/LLE/main/LLE_data2.csv'

# Read the CSV file into a DataFrame, specifying the header names
column_names = ['t', 'C_AS', 'C_BS', 'C_AL', 'C_BL']
data2 = pd.read_csv(url2, names=column_names, header=0)

# Plot the data from LLE_data2.csv
plt.figure(figsize=(10, 6))
plt.plot(data2['t'], data2['C_AS'], label='C_AS (Concentration of A in Solvent)')
plt.plot(data2['t'], data2['C_BS'], label='C_BS (Concentration of B in Solvent)')
plt.plot(data2['t'], data2['C_AL'], label='C_AL (Concentration of A in Liquid)')
plt.plot(data2['t'], data2['C_BL'], label='C_BL (Concentration of B in Liquid)')

# Add titles and labels
plt.title('Concentration of A and B in Solvent and Liquid over Time (LLE_data2)')
plt.xlabel('Time [t] in secs')
plt.ylabel('Concentration')
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
