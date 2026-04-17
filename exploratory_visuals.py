import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

data = pd.read_csv("teams_scaled.csv")

min_data = data[data['team']=="MIN"]
#print(min_data.head())

red_patch = mpatches.Patch(color='red', label='Missed Playoffs')
green_patch = mpatches.Patch(color='green', label='Made Playoffs')
colors = ['green' if x == 1 else 'red' for x in min_data['playoff']]

plt.bar(min_data['season'], min_data['xReboundsFor_PerGame'], label='playoff', color=colors)
plt.xlabel("Season")
plt.ylabel("corsiPercentage")
plt.xticks(np.arange(2008, 2026, step=1))
plt.tick_params("x", rotation=90)
plt.legend(handles=[red_patch, green_patch])
#plt.title("Bar Chart Example")
plt.show()