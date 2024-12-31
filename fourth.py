##Reverse the strings how many approach you know to solve
#1.Slicing 
#2.Use Reverse() function
#3.Implement from scratch


def reverse_string_from_scratch(input):
    #first we need to convert into list then we can implements because str' object does not 
    #support item assignment will throw
    lists=list(input)
    start=0
    end=len(lists)-1
    
    while start<=end:
        temp=lists[start]
        lists[start]=lists[end]
        lists[end]=temp
        start=start+1
        end=end-1
    return lists

strings="Ankit"
final_output=reverse_string_from_scratch(strings)
ans=''.join(final_output)
print(ans)



def reverse_string(input):
    # return input[::-1]
    ans= list(reversed(input))
    return ans

str=reverse_string("Ankit")

# ans2=""
# for i in str:
#     ans2+=i

# print(ans2)

# list=[1,2,3,45,2]
# list.reverse()
# print(list)