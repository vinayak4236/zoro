import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
cars_data=pd.read_csv("cars.csv")
plt.title("Histogram for distance travelled in KiloMeter")
plt.hist(cars_data['Sold_cars'],color='g',bins=5)
plt.xlabel("KiloMeter")
plt.ylabel("Frequency")
plt.show()