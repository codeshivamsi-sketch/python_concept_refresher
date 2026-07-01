print("1. str fns: ", dir("hello"), "\n]\n") # prints all functions of string
print("2. int fns: ", dir(11), "\n\n") 
print("3. open fns: ", dir(open), "\n\n")

# if u use "with" with open, its responsible to trigger __enter__ and __exit__ 
print("4. file fns: ", dir(open("file.txt")), "\n\n")