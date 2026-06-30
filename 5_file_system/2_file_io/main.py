# Write a file
with open("notes.txt", "w") as f:
    f.write("hello world\nbye world")

# Read from a file
with open("notes.txt", "r") as f:
    data = f.read()
    print("data: ", data)





# "r" -> read
# "w" -> write
# "a" -> append

# "rb" -> read binary
# "wb" -> write binary






# Read line by line
with open("notes.txt") as f:
    for line in f:
        print(line.strip()) # strip remove \n extra whitespaces.