##Implement shallow copy and deep copy

import copy
original=[[1,2,3], [4,5,6]]

copied=copy.copy(original)  #create a new objects but does not create the copies of nested objects
                        #  if we do any change in original objects its also reflects in nested objects


deep_copied=copy.deepcopy(original)
#update
original[0][0]=10
print(original)
print(copied)
print(deep_copied)