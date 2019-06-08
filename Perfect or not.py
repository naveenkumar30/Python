def perfect(number):
    s=0
    for i in range(1,number):
        if(number%i==0):
            s=s+i
    if(s==number):
        return True
    else:
        return False
        
num=int(input())
print(perfect(num))
