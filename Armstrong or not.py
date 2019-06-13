a=int(input())
p=0
temp=a
while(temp>0):
    l=temp%10
    p=p+l**3
    temp=temp//10
if(a==p):
    print("Armstrong")
else:
    print("Not a Armstrong")
