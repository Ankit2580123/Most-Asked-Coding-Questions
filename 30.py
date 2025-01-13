#filter out the palindrome word from odd index
input=['Hi','oyo','buzz','radar','civic','fizz','stats','refer','defined','121'] #[]


def is_palindrome(input):
       return input==input[::-1]  

print(len(input))
def filter_out_odd_index(input):
        length=len(input)
        # print(length)
        result=[]
        for i in range(length):
                if i%2!=0 and is_palindrome(input[i]):
                        result.append(input[i])
                    
        return result

ans=filter_out_odd_index(input)
print(ans)