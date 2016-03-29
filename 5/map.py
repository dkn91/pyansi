#!/usr/bin/env python

a=  range(10)
def asq(x):
    return x**2

print map(asq,a)

print map(lambda x: x**2, a)


