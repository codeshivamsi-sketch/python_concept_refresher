# A concise way to create list from another list
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n*n)
print(squares)




# With comprehension
squares2 = [n * n for n in numbers]
print(squares2)




# With a condition, only even no.
evens = [n for n in numbers if n % 2 == 0]
print(evens)




names = ["tom", "harry", "bruke"]
upper = [name.upper() for name in names]
print(upper)

