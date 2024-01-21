import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('overall.csv')
types = df.iloc[:, 2].values

trucks = 0
cars = 0
buses = 0
overall = 0

for type in types:
    overall += 1
    if type == 'car':
        cars += 1
    elif type == 'bus':
        buses += 1
    elif type == 'trucks':
        buses += 1

labels = ['Cars', 'Trucks', 'Buses']
sizes = [cars, trucks, buses]
colors = ['red','blue', 'yellow']
explode = (0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Overall distribution of different vehicles in all videos')
plt.legend()
plt.savefig("overall.png", format="png")