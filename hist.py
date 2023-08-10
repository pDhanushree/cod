import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("C:\\Users\\Sys\\Desktop\\mtcars.csv")
cyl_mpg_1 = df[df['mpg']==1]['cyl']
plt.hist(df['mpg'],color='b',alpha=0.5,label='mpg')
plt.xlabel("mpg")
plt.ylabel("frequency")

plt.show()
