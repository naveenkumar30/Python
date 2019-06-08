def prime(m,n):
    for num in range(m,n+1):
        if num>1:
            for i in range(2,num):
                if(num%i==0):
                    break
            else:
                print(num)
            
a=int(input())
b=int(input())
l=prime(a,b)
