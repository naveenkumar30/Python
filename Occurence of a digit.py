i=int(input())
f=0
c=0
d=int(input())
while (i>0):
    r=i%10
    if r==d:
        c+=1
        f=1
    i=i//10
if(f==0):
    print("digit not found")
else:
    print("digit's count:",c)
