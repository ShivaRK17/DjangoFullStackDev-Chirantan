# a = 5
# print("a value is {}".format(a))
def add(a,b):
    return a+b
# b = add(3,4)
# print(b)

def mult(a,b):
    sum = 0
    i = b
    while(i!=0):
        sum=add(sum,a)
        i-=1
    return sum

a = 4
b = 9

print("sum of a and b is {} and product is {}".format(add(a,b),mult(a,b)))

a = [6,5,9.7,"hi",{"ind":78}]
print(a)

a = [5,3,6,1,3,6,8]
a.sort()
print(sum(a),max(a),min(a))

def func(a):
    return a%5
print(a)
# a.sort(reverse=True)
a.sort(key=func)
print(a)

# OOPS -> classes,objects,attributes, member functions or methods
# Partial sum, accumulate in cpp
# Custom comparators 

# Slicing [start:end:step]

print(a[0:len(a):2])
print(a[0:4:]) # = a[:4:]
print(a[::-2]) # Going from back with a step of 1
print(a[-1::-2])

# Sets
a = {4,2,1,5,3,5,2}
print(a)
# Dictionary
a = {
    "name":"spiderman",
    "age":12
}
print(a)
# Tuples
a = (3,2,1,5,2,3)
print(a)

class Student:
    def __init__(self,name,age):
        self.name =  name
        self.age = age
    def __str__(self):
        return "*****\nName:{}\nage:{}\n*****".format(self.name,self.age)
a = Student("Srk",12)
print(a)
print(a.name,a.age)

# datetime
import datetime
# dt = datetime.date(2023,3,10)
# print(dt)
dt = datetime.datetime.now()
print(dt)
