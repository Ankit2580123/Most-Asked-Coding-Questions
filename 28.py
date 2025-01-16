#Tricky Interview Questions--01
a = [1, 2, 3]
b = a  #[1,2,3]
# print(a is b)
b.append(4) #[1,2,3,4]
print(a)  #[1,2,3,4]
print(b)  #[1,2,3,4]


#Tricky Interview Questions--02
x = 10
def modify_var():
    global x
    #x=0 ##local
    x += 5
modify_var()
print(x)  ##Output-->15


#Tricky Interview Questions--03
list = ['a', 'b', 'c', 'd', 'e']
print(list[10:])   #print empty because starting point not available

#Tricky Interview Questions--04
list = [ [ ] ] * 5 
print(list)  # output?  #-->[[],[],[],[],[]]
list[0].append(10)
print(list)  # output?  [[10], [10], [10], [10], [10]]
list[1].append(20)
print(list)  # output?  [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
list.append(30)
print(list)  # output?  [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]

#Tricky Interview Questions--05
def main(a):
    a = a + '2'  #byte2
    a = a * 2    #byte2byte2
    return a
print(main("byte"))

#Tricky Interview Questions--06
i = 1
while True:
    if i % 3 == 0:
        break
    print(i)  # 1,2
    i += 1    # 2,3

#Tricky Interview Questions--07
ans=min(max(False, -7.5, -7), 2, 1, 9)
print(ans)

#Tricky Interview Questions--08
text = 'hello world'
x = [i for i in text if i not in "aeiou"]   #output--> ['h','l', 'l',' ','w', 'r', 'l', 'd']
print(x)

#Tricky Interview Questions--09
d = {1 : "A", 2 : "B", 3 : "C"}
print(d.get(1, 4)) #output--> A


#Tricky Interview Questions--10
print(2**(3**2))  #512
print((2**3)**2)  #64
print(2**3**2)    #512  it starts from right side as a precedence

# mixed_list = [1, "two", 3.0, True]
# print(mixed_list)


#Tricky Interview Questions--011
a = 10
b = 10.0
c = "10"
print(a is b)  #False
print(a is int(b))  #True
print(c is str(a)) #False

#Tricky Interview Questions--012
a = True #1
b = False #0
print(a + 1) #2
print(b * 10) #0

#Tricky Interview Questions--013
# a=10
# b=5
# d=9.5
# c='a'
# print(a+b+c)  # In Python, you cannot directly concatenate a string with an integer or a float without explicitly converting one type to match the other.

#Tricky Interview Questions--014
string = "interview"
print(string[0:5])  #inter
print(string[::-1]) #weivretni

#Tricky Interview Questions--015
numbers = [x**2 for x in range(5)]
print(numbers)  #[0,1,4,9,16]

#Tricky Interview Questions--015
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)  #3
print(set1 | set2)  #1,2,3,4,5

#Tricky Interview Questions--016
lst = [1, 2, 3]
lst.append(4)  #[1,2,3,4]
lst.insert(1, 5) #[1,5,2,3,4]
lst.pop()       #[1,5,2,3]
print(lst)

#Tricky Interview Questions--017
s = "Python"
print(s[:3] * 2)  #pytpyt


#Tricky Interview Questions--018
nums = [1, 2, 2, 3, 4, 4]
unique_squares = {x**2 for x in nums}  #{1,4,4,9,16,16 } SET Does not contain duplicates
print(unique_squares)  #{1,4,9,16} Final answer

#Tricky Interview Questions--019
import copy
arr=[[1,2,3],[4,5,6]]
shallow_copied=copy.copy(arr)
deep_copied=copy.deepcopy(arr)
arr[1][1]=100
print(arr)
print(shallow_copied)
# print(deep_copied)

#Tricky Interview Questions--20 What is the purpose of zip function
a=[1,2,3,4]
b=['a','b','c','d']
zipped=[]
for i in zip(a,b):
    zipped.append(i)
print(zipped)

##Tricky Interview Questions--21 How do you merged two dict in python
dict1={'a':1,'b':2}
dict2={'c':1,'d':5}
merged=dict1 | dict2
print(merged)

##Tricky Interview Questions--22 Sort the dict based on the values

obj={
    'a':1,
    'b':5,
    'c':4,
    'd':10,
    'e':8
}
sort_dict_values=dict(sorted(obj.items(),key=lambda item: item[1]))
sort_dict_keys=dict(sorted(obj.items(),key=lambda item: item[0]))

print(sort_dict_values)
print(sort_dict_keys)

##Tricky Interview Questions--23 difference between is vs ==
a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=5
d=5
print(c is d)  #True  #return true because c and is literal and they creates only ones in memory
print(c==d)     #True
print(a is b) #False return false because list is mutable types
print(a==b)   #True


##Tricky Interview Questions--24
# you need to shuffle the list items and also return random items in each functions calls
from random import shuffle
import random
city=['Goa','Chandigarh','Jamshedpur','Patna','Ranchi','Bangalore','Pune','Hyderabad','Gurugram']

def shuffle_city_names(city):
    shuffle(city)  
    return city

def return_one_city_in_each_call(city):
    ans=random.choices(city) #randomly selected one city and return list
    return ''.join(ans)  #Converted list into string
print(shuffle_city_names(city))
print(f"City Name Randomly Selected: {return_one_city_in_each_call(city)}")