import enum
from traceback import print_tb


fruits = ["apple", "orange", "banana"]

# Without enumerate
for i in range(len(fruits)):
    print(i, fruits[i])




# With enumerate - cleaner
for i, fruit in enumerate(fruits):
    print(i, fruit)





for fruit in fruits:
    print(fruit)





for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)






