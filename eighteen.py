#implement lambda function and normal function also


def even(x): 
    return x%2==0
  
num=[2,6,5,3,8,9,4]     
ans=list(filter(even,num))
print(ans)
    
# evens=list(filter(lambda x: x%2==0,num))
# print(evens)
city=['patna','jaipur','goa','mumbai','jamshedpur']


sorted_city=list(sorted(city,key=lambda x : len(x)))
sort_city=list(sorted(city,key=len))
print(sort_city)