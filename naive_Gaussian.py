from sklearn.naive_bayes import GaussianNB
#create naive bayes classifier
gaunb=GaussianNB();

#create dataset
X=[[121,45],[131,76],[142,60],[165,50],[176,54],[176,87],[187,43]]
Y=['male','male','female','female','male','male','male']

#train classifier with dataset
gaunb=gaunb.fit(X,Y)

h=int(input("Enter Height : "))
w=int(input("Enter Weight : "))

#predict using classifier
prediction=gaunb.predict([[h,w]])
print(prediction[0])
