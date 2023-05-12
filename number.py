
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pandas.plotting import scatter_matrix
df= pd.read_csv('diabetes.csv')
np.genfromtxt('diabetes.csv', delimiter=',')

#plot=sns.load_dataset(df)

print(df.head())

#ai_cor=plot.corr()
#sns.heatmap(ai_cor,annot=True,cmap='coolwarm',linewidths=1)
#p= scatter_matrix(df,figsize=(25, 25))
p=sns.pairplot(df, hue = 'Outcome')
#sns.barplot(x="Age", y="Pregnancies", data=df, hue="Outcome")
plt.show()