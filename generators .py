#generators: no tuple comphrehensions in above cases if we remove those braces and if we remove paranthesis then the outcome is generators..
#syntax for list comprehension
'''a=[i for i in range(21)]
print(a)
print(type(a))'''

'''a=(i for i in range(16))
print(*a)
print(type(a))'''

'''a=(i for i  in range(16))
#print(list(a))
#print(tupe(a))
print(set(a))'''

#generators is also a function which can be used as an iterator(loop) by producing group of values,were we use yile keyword.
#yile vs return:return will terminate the function ,where as yile can pass the function and born with every successive iteration..
'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
#return a
print(check(a,b))'''


#diff yeild vs return examples
'''def mygen():
    #return "python"
    #return "java"
    #return "dsa"
    return "python","java","dsa"
print(*mygen())'''

'''def mygen():
    yield "vja"
    yield "hyd"
    yield "vzg"
print(*mygen())'''


#next
d=mygen()
print(next(d))
print(next(d))
print(next(d))

