#create a function to move all 0's elements of array in last 
#create a function to move all 0's elements of array in front 


array=[10,0,6,0,8,0,2,0]

# def move_last(array):
#     for i in array:
#         if i==0:
#             array.append(i)
#             array.remove(i)

def move_front(array):
    for i in array:
        if not i==0:
            array.append(i)
            array.remove(i)
# move_last(array)
move_front(array)
print(array)
