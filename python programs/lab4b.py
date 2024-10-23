import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
cars_data=pd.read_csv("cars.csv")
plt.scatter(cars_data['cars'],cars_data['Sold_cars'],c='blue')
plt.xlabel('cars(Age)')
plt.ylabel('Sold_cars(Price)')
plt.show()