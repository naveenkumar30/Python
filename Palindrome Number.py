a=int(input())
p=0
temp=a
while(a>0):
    l=a%10
    p=p*10+l
    a=a//10
if(temp==p):
    print("Palindrome")
else:
    print("Not a Palindrome")
