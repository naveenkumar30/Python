a,b=map(int,input().split())

for i in range(a,b):
    l=len(str(i))
    p=0
    r=0
    temp=i
    while(temp>0):
        d=temp%10
        r=r+d**l
        temp=temp//10
    if(i==r):
        print(i,end=" ")
