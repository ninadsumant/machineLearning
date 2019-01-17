import constraint
from constraint import *
import matplotlib.pyplot as plt


problem=Problem()
problem.addVariable('a',range(1,50))
problem.addVariable('b',range(1,20))

problem2=problem

problem.addConstraint(lambda a,b:a+(2*b)<=16,["a","b"])
#problem.addConstraint(lambda a,b:(5*a)+(3*b)<=45,["a","b"])
problem.addConstraint(lambda a,b:a>=0,["a","b"])
problem.addConstraint(lambda a,b:b<20,["a","b"])

#problem.addConstraint(lambda a,b:a+(2*b)<=16,["a","b"])
problem2.addConstraint(lambda a,b:(5*a)+(3*b)<=45,["a","b"])
problem2.addConstraint(lambda a,b:a>=0,["a","b"])
problem2.addConstraint(lambda a,b:b<20,["a","b"])


solutions=problem.getSolutions()
solutions2=problem2.getSolutions()

print("Solution-1\n_____________________________")
for solution in solutions:
    val1=solution.get('a')
    val2=solution.get('b')
    print(val1,val2)
   
print("Solution-2\n_____________________________")
for solution2 in solutions2:
    val1=solution2.get('a')
    val2=solution2.get('b')
    print(val1,val2)

print("Intersection Points\n_____________________________")   
print("Not done")
