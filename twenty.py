# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
        
#         reversed_str = char + reversed_str
#         print(reversed_str)
#     return reversed_str

# print(reverse_string("Python")) 


str="Ankit"
reveres=""
for i in range(len(str)-1,-1,-1):
    reveres+=str[i]
print(reveres)

