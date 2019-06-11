a=int(input())
b=int(input())
if(a>b):
    x=a
else:
    x=b
while(x):
    if((x%a==0) and (x%b==0)):
        print(x)
        break
    x=x+1
