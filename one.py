"""You Have Given Input and input should be any number or strings you to check the input is Palindrome or not"""
#input1=121 
#input2="aba"

#Check for both and create only one functions


##First and Simple Approach
def palindrome_approach(input):
     final_input=str(input)
     return final_input==final_input[::-1]

#Note--> Used isinstance to differentiate between int and str
def palindrome(input):
    if isinstance(input, str):  # Check if the input is a string
        return input == input[::-1]
    elif isinstance(input, int):  # Check if the input is an integer
        temp = input
        ans = 0
        while input > 0:
            rem = input % 10
            ans = ans * 10 + rem
            input //= 10  # Use integer division
        return temp == ans
    else:
        raise ValueError("Input must be either a string or an integer.")




input1 = 121
input2 = "aba"
print(palindrome(input1))  # Should print True
print(palindrome(input2))  # Should print True