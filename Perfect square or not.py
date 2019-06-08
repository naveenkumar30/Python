import math
def perfect_square(num):
    num=math.sqrt(num)
    return (num-math.floor(num)==0)
number=int(input())
if(perfect_square(number)):
    print(True)
else:
    print(False)
