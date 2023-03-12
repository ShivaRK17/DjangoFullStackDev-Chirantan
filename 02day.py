'''
Lambda Function - single line function
Regex
Dictionary and lists
git and github basics
pip = package manager
venv = virtual environments
django
'''

is_negative = lambda n : n<0
add_2 = lambda a,b: a+b

print(is_negative(-4))
print(add_2(4,5))

a = [3,-2,-4,1,2,-9]
print(list(filter(is_negative, a)))


# Regex
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(bool(x))

txt = "This-is-django"
x = txt.split('-')
print(x)

txt = "Rain in spain gain some pain"
x = re.findall('.?ai', txt)
print(x,len(x))


# Hashing
print(hash("21MEB0B25"))


# Dictionary
dic = {
    "A":1,
    "B":2,
    "C":3
}
print(dic.keys())
print(dic.values())
print(dic.items())
for k,v in dic.items():
    print(k,v,end=" , ")

print()
# Traverse two lists simultaneously - using zip
a = ["a","b","c","d"]
b = [1,2,3,4]

print(list(zip(a,b)))

for i,j in zip(a,b):
    print(i,j,end=" , ")

# Git and Github 
# installed
