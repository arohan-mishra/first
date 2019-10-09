x=[23,45,12,42,54,89,28,11]
for i in range(len(x)-1,0,-1):
    for j in range(i):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
print(x)