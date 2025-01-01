#you have qa given string you need to capitalize 
#starting character of string
str="my name is ankit kumar"
ans=""
traverse=""
for i in str:
    if i==' ':
        temp=traverse.capitalize()
        ans+=temp
        ans+=" "
        traverse=""
    
    else:
        traverse+=i

print(ans)