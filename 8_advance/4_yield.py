def count_up():
    yield 1 # Produces one value and pause.
    yield 2 # Resumes, produces next
    yield 3

for n in count_up():
    print(n)






# Create whole list in memory
def with_return():
    return [1,2,3]

for n in with_return():
    print(n)