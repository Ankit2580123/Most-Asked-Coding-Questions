#write a program to reverse the string without using builtin methods

# def reverse_string(str_input):
#     # return str_input[::-1]
#     ans=""
#     for char in str_input:
#         ans=char+ans 
#         print(ans)
#     return ans

output=""
def reverse_string(str_input):
    word= str_input.split()
    # print(word)
    string=""
    for i in word:
        string+=i
        string+=" "

    return string[::-1].lstrip()
    # for i in word:
    #     # print(i[::-1])
    #     output=''.join(i[::-1])
    # return output

print("Hello world India")
ans=reverse_string('Hello world India')
print(ans)