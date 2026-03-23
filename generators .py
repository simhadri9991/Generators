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
'''a="codegnan"
print(a)

print(list(a))
print(tuple(a))
print(set(a))

#print(dict(a))

b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"simha")
print(b)'''

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
    a=input("a value"))
    b=input("b value"))
    print(a+b)'''

'''a=eval(input("a value"))
b=eval(input("b value"))
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
print(*b)

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

#ord()
'''ord("a")
ord("9")'''


#-------TASK-----------
#1.print A-Z
#2.print a-z
#3.ASCII for yor name!!
'''

for i in range(65, 91):
    print(chr(i), end=" ")
    


for i in range(97,123):
    print(chr(i), end=" ")


name=input("enter your name:")
for i in name:
    print(ord(i))
'''


#annonymous:-
''' Annonymous functions are nameless functions we use a keyword called as lambda to create annonymous functions'''
#write a function to calculate 2*x+5 Where x=5

'''def f(x):
    print(2*x+5)
f(5)'''
#Runtime
'''def f():
    x=int(input("value"))
    print(2*x+5)          
f()'''
#syntax:-
#a=lambda arg:expr

'''a=lambda x:2*x+5
print(a(5))'''

#Runtime
'''a=int(input("value"))
b=lambda x:2*x+5
print(b(a))'''

#TASK
#multiple by 2 numbers
'''a=int(input("value a"))
b=int(input("value b"))
c=lambda a,b:a*b
print(c(a,b))'''

'''a=99
b=69
c=lambda a,b:a*b
print(c(a,b))'''

#TASK-2
'''a="python"
b=lambda a:a.upper()
print(b(a))'''

'''a=input("enter")
b=lambda a:a.upper()
print(b(a))'''

'''
b=lambda a:a.upper()
print(b("python"))
'''
#Fname and Lname
'''a=input("fname:")
b=input("lname:")
c=lambda a,b:a+" "+b
print(c(a,b))'''

'''a,b=[i for i in input("enter the name").split("0")]
c=lambda x,y:(x+" "+y).title()
print(c(a,b))'''
#filter()
a=[2,5,7,8,9,11,20,30,40]
'''if a%2==0:
    print(a)''' #error

'''for i in a:
    if i%2==0:
        print(i)'''

'''for i in a:
    if i%2==0:
        print(i, end=" ")'''

'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

'''b=list(filter(lambda x:x%2!=0,a))
print(b)'''

'''a=[[],(),set(),{}," ",None,2,3.4,"simha",5+2j,True,False]
b=list(filter(None,a))
print(b)'''
#map():-

'''Each object from a collection and forms a new collection'''
'''
a=[10,5,7,8,15,20,40,100]
b=[4,6,12,24,40,80,35,1,98]
c=list(map(max,a,b))
print(c)
c=list(map(min,a,b))
print(c)
'''

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=input("enter the names:").split(",")
print(a+b)'''

'''a,b=[x for x in input("enter the names:").split(",")
print(a+b)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a,b=int(input("enter the values:")).split(",")
print(a+b)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a,b=int(input("enter the values:")).split(",")
print(a+b)''' #value error

'''a,b=[int(x) for x in input("enter the names:").split(",")]
print(a+b)'''

'''a,b=map(int,input("enter the values:").split(","))
print(a+b)'''

'''a=list(map(int,input("enter the values:").split(",")))
print(a)'''

'''a=tuple(map(int,input("enter the values:").split(",")))
print(a)'''

'''a=set(map(int,input("enter the values:").split(",")))
print(a)'''

'''a=input("enter the key and value pairs:")
b=dict(i.split(":") for i in a.split(","))
print(b)'''
