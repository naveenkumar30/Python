def perfect(a,b):
    for i in range(a,b+1):
        s=0
        for j in range(1,i):
            if(i%j==0):
                s=s+j
        if(s==i):
           print(i)
            
m=int(input())
n=int(input())
l=perfect(m,n)
