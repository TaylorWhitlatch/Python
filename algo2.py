a = 1
b = 1
total = 0
while a <= 4000000:
    if(a % 2 == 0):
        total += a
    c = a
    a = b
    b = (c + b)

print total

sumNum = 0
a,b = 0,1
while b < 4000000:
    a,b = b,a+b
    if(b%2 == 0):
        numNum += b
print sumNum
