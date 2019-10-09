x = input('Enter a number = ')
y = len(x)-1
z = 0
c = int(x)
while y>=0:
    a = c%10
    c = c//10
    z = z + a*(10**y)
    y = y - 1
print(z)
