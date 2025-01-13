#There is two list you need to check both strings are anagram
#Anagram means the string one contains same characters in strings two 

str1 = "Listen"
str2 = "Silent"



#First Approach
def anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    first=list(str1.lower())
    second=list(str2.lower())
    first.sort()
    second.sort()
    return first==second

#second Approach
def anagram2(str1,str2):
    updated_str1=str1.upper()
    updated_str2=str2.upper()
    if len(str1)!=len(str2):
        return False
    
    for i in updated_str1:
        if i not in updated_str2:
            return False
    return True

x=anagram(str1,str2)
print(x)
print(anagram2(str1,str2))