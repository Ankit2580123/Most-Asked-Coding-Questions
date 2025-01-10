#Write a program to find the missing numbers in the list

list=[1,2,3,4,6,7]
def find_missing_no(list):
    sum=0
    length=len(list)+1
    # print(length)
    total=(length*(length+1))//2
    for i in list:
        sum+=i
    return total-sum
ans=find_missing_no(list)
print(f'Missing Number is--> {ans}')