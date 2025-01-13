#Write a program to check the number is armstrong or not

def armstrong_number(input):
    length=len(str(input))
    digit=0
    original_num=input
    output=0
    while input>0:
        digit=input%10
        output+=(digit**length)
        input=input//10

    
    if original_num==output:
        return True
    else:
        return False

    


print(armstrong_number(407))