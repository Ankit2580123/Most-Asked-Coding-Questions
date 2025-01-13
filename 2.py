""" You have a range between 1-100 and you need to print even numbers that comes between 1-10 then 20-30 
then 40-50 then 60-70 and so on and 11-20,31-40 skips alternatively"""

#simpler approach to solve the problem:

for i in range(1, 101):
    if (1 <= i <= 10 or 20 <= i <= 30 or 40 <= i <= 50 or 60 <= i <= 70 or 80 <= i <= 90) and i % 2 == 0:
        print(i, end=" ")

print("\n")
# 2nd approach
ranges = [(1, 10), (20, 30), (40, 50), (60, 70), (80, 90)]

for start, end in ranges:
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=" ")