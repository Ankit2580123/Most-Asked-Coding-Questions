#Write a Python code to merge two dictionaries

#Approach1-->Unpacking Method **
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print(merged) #{'a': 1, 'b': 3, 'c': 4}

#Approach2-->Using Update method
dict1.update(dict2)
print(dict1)

#Approach3-->Using | Operator
merged_dict = dict1 | dict2
print(merged_dict)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

#Using Dictionary Comprehensions
merged_dict = {key: value for d in (dict1, dict2) for key, value in d.items()}
print(merged_dict)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

