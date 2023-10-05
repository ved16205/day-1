import numpy

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mut(x,y):
    return x * y

def devid(x,y):
    return x % y



print("wellcome to simple calculator")

x = float(input("first number: "))
y = float(input("secont number: "))

i = input("+, -, *, % :")

if i == "+":
    result = add(x, y)

elif i == "-":
    result = sub(x, y)
    
elif i == "*":
    result = mut(x, y)
    
elif i == "%":
    result = devid(x, y)
else:
    print("try again")

print("asn: ", result)