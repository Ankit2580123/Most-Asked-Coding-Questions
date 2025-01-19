#Generate a fibonacci series using generator

def fibonacci_using_generator():
    a,b=0,1
    while True:
        yield a
        a,b = b,a+b
        
        

ans=fibonacci_using_generator()
print(next(ans))  #0
print(next(ans))  #1
print(next(ans))  #1
print(next(ans))  #2
print(next(ans))  #3
