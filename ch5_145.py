# Chapter 5, First Class Functions, pg 145

def factorial(n):
    '''returns n factorial, e.g. n!'''
    return 1 if n < 2 else n * factorial(n-1)

factorial(42)