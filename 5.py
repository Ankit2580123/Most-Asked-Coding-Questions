#you have a given a range start, end and you need to print all prime number comes under between

from math import sqrt
def print_prime_between(num):
    if num<2:
        return False
    else:
        for i in range(2,int(sqrt(num))+1):
            if num%i==0:
                return False
    return True


start=1
end=19
primes=[]
for i in range(start,end+1):
    if print_prime_between(i):
        primes.append(i)

print(primes)

