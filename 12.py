#use generation to print fibonacci sequence in each call

def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

def even_number(num):
     for i in range(num+1):   
        if num%2==0:
            yield i

even_list=iter(even_number(20))
print(tuple(even_list))

ans=fibonacci()

for i in range(10):
        print(next(ans),end=" ")


