import matplotlib.pyplot as plt 
import pandas as pd
cars_data=pd.read_csv("cars.csv")
cars=cars_data["cars"]
data=cars_data["Sold_cars"]
fig=plt.figure(figsize=(10,70))
plt.pie(data,labels=cars)
plt.show()