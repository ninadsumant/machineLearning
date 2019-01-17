import numpy as np
import statistics as s
import matplotlib.pyplot as plt

x=[1,2,4,3,5]
y=[1,3,3,2,5]

A=(s.mean(x),s.mean(y))

A=(x-A[0]*np.ones(len(x)),y-A[1]*np.ones(len(x)))

mul=A[0]*A[1]
xSquare=A[0]**2

dev=sum(mul)/sum(xSquare)

b0=s.mean(y)-(dev*s.mean(x))
b0=b0*np.ones(len(x));

b1=dev*np.ones(len(x))

pY=b0+(b1*x)
print('X           : ',x)
print('Y           : ',y)
print('Predicted y : ',pY)

plt.plot(x,y,'ro')
plt.plot(x,pY,'bs')
plt.plot(x,pY,'black')
plt.show()
