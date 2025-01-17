'''You have a string an you need to sort the string and sort the numbers and final output will be firstly alphabets 
followed by Numbers'''
#Sample Input-->H1S8R5A6
# Sample Output-->AHRS1568

input_str=input("Enter the String like [AG5J9L] or [ag5j9l]-->")
alphabets=[]
numbers=[]
for ch in input_str:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        numbers.append(ch)
final_merge_sort_list=sorted(alphabets)+sorted(numbers)
ans=''.join(final_merge_sort_list)
print(ans)

