from sklearn.naive_bayes import GaussianNB
import pandas as pd
import csv
gaunb = GaussianNB()
df = pd.read_csv('data.csv')

X = df[['height','weight','shoeSize']]
Y = df[['gender']]
gaunb = gaunb.fit(X,Y)
prediction = gaunb.predict([[113,41,29]])
print(prediction)
print(X,Y)
