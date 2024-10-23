import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("cars.csv")
df=pd.DataFrame(data)
X=list(df.iloc[:,0])
Y=list(df.iloc[:,1])
plt.bar(X,Y,color='g')
plt.title("Used cars sale")
plt.xlabel("cars")
plt.ylabel("Sold_cars")
plt.show()
