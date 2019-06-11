def power(num):
    if num<=0:
        return False
    else:
        p=(num & (num-1)==0)
        return p
x=int(input())
print(power(x))
