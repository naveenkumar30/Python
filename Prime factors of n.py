def prime(number):
    for i in range(2,num+1):
        if(number%i==0):
            a=1
        for j in range(2,i+1):
            if(i%j==0):
                a=a+1
        if(a==2):
            print(i)
        
num=int(input())
l=prime(num)
