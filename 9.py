#write a program to print fibonacci sequence
#0,1,1,2,3,5,8

#1st Approach
def fibonacci(ulimit):
    fibo=[0,1]
    while len(fibo)<=ulimit:
        fibo.append(fibo[-1]+fibo[-2])

    print(fibo)
fibonacci(20)
#2nd Approach
# def fibonacci(ulimit):
#     a,b=0,1
#     print(a,end=" ")
#     print(b,end=" ")
#     c=a+b
#     while(b<=ulimit):
#         print(c,end=" ")
#         a=b
#         b=c
#         c=a+b
    
        
#3Approach  Using recursion
list=[]
def fibonacci_seq(num):
    if num<=0:
        return 0
    if num==1:
        return 1
    return fibonacci_seq(num-1)+fibonacci_seq(num-2)
   


ulimit=fibonacci_seq(5)
for i in range(ulimit):
    print(fibonacci_seq(i),end=" ")
