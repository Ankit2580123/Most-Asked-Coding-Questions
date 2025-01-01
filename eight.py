#fizzy buzz program when number is divisible by 3 then print Fizz
# When number is divisible by 5 then print Buzz
# when number is divisible by 3 and 5 both then print Fizzy Buzz

def fizzy_buzz(num1,num2):
    if num1%3==0 and num2%5==0:
        return "Fizzy Buzz"
    elif num1%3==0:
        return "Fizzy"
    elif num2%5==0:
        return "Buzz"
    else:
        return "Not Divisible by Both"

output=fizzy_buzz(29,19)
print(output)
