#Write a program to remove white spaces of the string


txt = ",,,,,rrttgg.....Lion....rrr"

x = txt.strip(",.grt")

print(x)


# def remove_spaces(str_input):
#     updated_str_input=str_input.strip()  #remove white spaces from both ends 
#     ans=""
#     for i in updated_str_input:
#         if i!=' ':
#             ans+=i
#         else:
#             continue
    
#     print(ans)


# str_input=" Ank i t Kuma r"
# final_output=remove_spaces(str_input)