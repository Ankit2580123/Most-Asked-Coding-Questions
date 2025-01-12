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
