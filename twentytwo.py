##find the third largest of the list without using builtin methods

list=[1,2,35,4,6,8]  ##-->third Largest-->6


def finding_third_largest(list):
    length=len(list)
    for i in range(length):
        for j in range(length-i-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list[-3]

output=finding_third_largest(list)
print(output)

# def third_largest(list):
#     third_largest=float('-inf')
#     first_largest=float('-inf')
#     second_largest=float('-inf')
    
#     for i in list:
#         if i>first_largest:
#             third_largest=second_largest
#             second_largest=first_largest
#             first_largest=i
            
#         elif i>second_largest  and i!=first_largest:
#             third_largest=second_largest
#             second_largest=i

#         elif  i>third_largest and i!=second_largest and i!=first_largest:
#             third_largest=i

#     return third_largest

# ans=third_largest(list)
# print(ans)



# a = (1,2,3, [1,2,3])
# a[-1][0] = 11

# print(type(a))


# list=[1,2,3,4]
# try:
#     list[5]=10
# except Exception as e:
#     print(e)
# finally:
#     print("always executed..")
    
