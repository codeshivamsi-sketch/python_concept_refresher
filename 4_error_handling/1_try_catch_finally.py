from typing import final


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")





try:
    result = int("abc")
except Exception as e:
    print(f"Error: {e}")




try:
    f = open("file.txt") # additional info: if "with" is not used, must close f.
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("This always run")





# multiple except blocks
try:
    x = int(input("Enter number: "))
    result = 10 / x
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("Can't divide by zero")




