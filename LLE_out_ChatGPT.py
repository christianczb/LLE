import pandas as pd
import matplotlib.pyplot as plt

# Define the URL of the CSV file in the GitHub repository
url = 'https://raw.githubusercontent.com/christianczb/LLE/main/LLE_data.csv'

# Read the CSV file into a DataFrame, specifying the header names
column_names = ['t', 'C_AS', 'C_BS', 'C_AL', 'C_BL']
data = pd.read_csv(url, names=column_names, header=0)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(data['t'], data['C_AS'], label='C_AS (Concentration of A in Solvent)')
plt.plot(data['t'], data['C_BS'], label='C_BS (Concentration of B in Solvent)')
plt.plot(data['t'], data['C_AL'], label='C_AL (Concentration of A in Liquid)')
plt.plot(data['t'], data['C_BL'], label='C_BL (Concentration of B in Liquid)')

# Add titles and labels
plt.title('Concentration of A and B in Solvent and Liquid over Time')
plt.xlabel('Time [t] in secs')
plt.ylabel('Concentration')
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
