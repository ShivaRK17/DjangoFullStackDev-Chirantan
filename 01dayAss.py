# 01
def sumOfSquares(n):
    sum = 0
    for item in n:
        sum+=(item**2)
    return sum

a = [1,2,3]
print(sumOfSquares(a))

# 02
def nLargestEl(a,n):
    a.sort(reverse=True)
    print(a[:n:])
a = [3,2,5,7,1,9]
nLargestEl(a, 2)

# 03
k = -3
l = -9
for i in range(l,k):
    print(i)


# 04
def isSubstring(a,b):
    return (a in b)
a = "ell"
b = "hello"
print(isSubstring(a, b))

# 05
dic = dict()
dic["sky"] = "blue"
dic["grass"] = "green"
dic["sun"] = "yellow"
print(dic)

# 06
a = ["abcd","dcba","abdb"]
