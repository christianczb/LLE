import pandas as pd
import matplotlib.pyplot as plt

# Load data from LLE_data.csv
df1 = pd.read_csv("https://raw.githubusercontent.com/christianczb/LLE/master/LLE_data.csv")
time1, C_AS1, C_BS1, C_AL1, C_BL1 = df1["time"], df1["C_AS"], df1["C_BS"], df1["C_AL"], df1["C_BL"]

# Load data from LLE_data2.csv
df2 = pd.read_csv("https://raw.githubusercontent.com/christianczb/LLE/master/LLE_data2.csv")
time2, C_AS2, C_BS2, C_AL2, C_BL2 = df2["time"], df2["C_AS"], df2["C_BS"], df2["C_AL"], df2["C_BL"]

# Plot all variables
plt.figure(figsize=(10, 6))
plt.plot(time1, C_AS1, label="C_AS (solvent, LLE_data)")
plt.plot(time1, C_BS1, label="C_BS (solvent, LLE_data)")
plt.plot(time1, C_AL1, label="C_AL (liquid, LLE_data)")
plt.plot(time1, C_BL1, label="C_BL (liquid, LLE_data)")

plt.plot(time2, C_AS2, linestyle="--", label="C_AS (solvent, LLE_data2)")
plt.plot(time2, C_BS2, linestyle="--", label="C_BS (solvent, LLE_data2)")
plt.plot(time2, C_AL2, linestyle="--", label="C_AL (liquid, LLE_data2)")
plt.plot(time2, C_BL2, linestyle="--", label="C_BL (liquid, LLE_data2)")

# Add labels and legend
plt.xlabel("Time (s)")
plt.ylabel("Concentration")
plt.title("Liquid-Liquid Extraction Concentrations Comparison")
plt.legend()

# Show the plot
plt.show()
