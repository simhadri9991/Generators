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
'''d=mygen()
print(next(d))
print(next(d))
print(next(d))
'''
#fromkeys()
a="codegnan"
print(a)

print(list(a))
print(tuple(a))
print(set(a))

#print(dict(a))

b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"simha")
print(b)

#eval():-
''' It will accept any data type'''

'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=(input("a value"))
    b=(input("b value"))
    print(a+b)'''
    

'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    print(type(a))'''

#zip():-
'''we can combine multiple collections into one collection'''
'''a=[10,20,30,40,50]
names=["simhadri","aditya","hitesh","mohith","mahesh"]
print(a+names)
b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

d=tuple(zip(a,names))
print(d)

e=set(zip(a,names))
print(e)

f=dict(zip(a,names))
print(f)'''

#enumerate():-
'''we can give count to the collections'''
''' it will work only in tuple and list '''
'''Mainly we can prioritize list for this enumerate'''


'''names=["simha","mahesh","naveen","hitesh","mohith"]
for i in range(len(names)):
    print(i,names[i])'''

'''names=["simha","mahesh","naveen","hitesh","mohith"]
b=dict(enumerate(names))
print(b) 

b=list(enumerate(names))
print(b)

b=tuple(enumerate(names))
print(b)

b=set(enumerate(names))
print(b)'''

#ascii:-
#chr()
'''chr(20) #\x14
chr(68) #D
chr(90) #Z'''
'''
#ord()
ord("a")
ord("9")'''

#1.print A-Z
#2.print a-z
#3.ASCII for yor name!!





































