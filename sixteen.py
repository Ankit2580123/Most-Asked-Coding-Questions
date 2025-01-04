##write a program to check the given number is binary or not

def check_binary(num):
    input=str(num)
    print(input)
    for i in input:
        if i not in ('0','1'):
            return False
    return True
 
x=1101002
if check_binary(x):
    print("Binary")
else:
    print("Not Binary")




# import random

# ans=""
# for i in range(1,6):
#     x=random.randint(1,5)
#     val=str(x)
#     ans+=val
# print(type(ans))
# new_otp=int(ans)
# print(type(new_otp))
# print(new_otp)

# p=random.random() #floating number
# print(p)
# set1={1,2,3,4,5}
# set2={4,6,8,7,2}

# ans=set1 - set2
# print(ans)

# a=10
# b=10

# print(a is b)