def perfect_num(a,b):
    p=0
    for i in range(a,b+1):
        j=1
        while (j*j<=i):
            if(j*j==i):
                p=p+1
            j=j+1
        i=i+1
    return p
m=int(input())
n=int(input())
print(perfect_num(m,n))
