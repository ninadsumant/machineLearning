import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm
import pandas as pd
import numpy as np

iris = datasets.load_iris()
x = pd.DataFrame(iris.data)
x.columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']

y = pd.DataFrame(iris.target)
y.columns = ['Targets']

#K means Cluster
model = KMeans(n_clusters=3)
model.fit(x)
model.labels_

#view the results
#set the size of the plot

e=plt.figure(figsize=(14,7))

#create colormap
colormap = np.array(['red', 'lime', 'black'])

#plot original classification
plt.subplot(1, 2, 1)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.Targets], s=40)
f=plt.title('Real Classification')

#plot the models Classifications
plt.subplot(1, 2, 2)
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[model.labels_], s=40)
plt.title('K mean Classification')
plt.show()

