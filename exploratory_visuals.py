import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("teams_scaled.csv")

min_data = data[data['team']=="MIN"]
#print(min_data.head())

plt.bar(min_data['season'], min_data['xGoalsFor_PerGame'], color='green')
plt.xlabel("Season")
plt.ylabel("corsiPercentage")
plt.xticks(np.arange(2008, 2026, step=1))
plt.tick_params("x", rotation=90)
# plt.title("Bar Chart Example")
plt.show()