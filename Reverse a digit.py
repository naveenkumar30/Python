a=int(input())
p=0
while(a>0):
    l=a%10
    p=p*10+l
    a=a//10
print(p)
