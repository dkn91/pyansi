#!/usr/bin/env python

a=  range(10)
def asq(x):
    return x**2

print map(asq,a)

#map syntax returns the logical val for the whole set of list
print map(lambda x: x**2, a)


#filter syntax returns the numerical value
print filter(lambda x: x%2 ==0, a)

#reduce returns the val of operation 
print reduce(lambda x,y: x+y,a)
 
