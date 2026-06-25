count = 0

def inc():
    global count        # global tells Python to use the outer variable, not create a new one
    count = count + 1   # Without gobal this line will throw ERROR — Python treats this as a new local variable
    return count

print(inc())

