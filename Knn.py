from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import *
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

digit = load_digits()
dig = pd.DataFrame(digit['data'][0:1700])
print("Data\n_______________\n",dig.head(),"\n__________________\n")


train_x=digit['data'][:1700]
train_y=digit['target'][:1700]

knn= KNeighborsClassifier(5)
knn.fit(train_x,train_y)

val=int(input("Enter your choice (0-1797): "))
test= np.array(digit['data'][val-1])
test1=test.reshape(1,-1)

print("Predicted Digiht : ",(knn.predict(test1))[0])
print("Target Digits : ",digit['target_names'])

