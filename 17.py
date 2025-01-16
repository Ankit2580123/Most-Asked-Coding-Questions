#Reverese the string of each words
#eg--> My Name is Ankit--->output-->yM eame si tiknA

string="My Name is Ankit Kumar"
new = string.split()
print(new)
new_reversed=[]
def reverese_each_word(str_input):

    for word in new:
        new_reversed.append(word[::-1])

    ans=' '.join(new_reversed)
    print(ans)
    return ans
    

    # return str_input[::-1]

print("Reverse String words is: ",reverese_each_word(string))