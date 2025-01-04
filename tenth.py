#you have qa given string you need to capitalize 
#starting character of string

str="My Name is Ankit"
ans=str.split()
print(ans)
list=["Hello", "World"]
print(' '.join(list))

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