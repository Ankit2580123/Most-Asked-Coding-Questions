#Find maximum contigous subarray sum
list=[1,2,3,-5,6,-2,4,6,8]
print(len(list))
def max_cont_sum(list):
    max=list[0]
    current_sum=0
    for i in range(len(list)):
        current_sum+=list[i]
        if current_sum>max:
            max=current_sum
        elif current_sum<0:
            current_sum=0
        
        
    return max

ans=max_cont_sum(list)
print(ans)
