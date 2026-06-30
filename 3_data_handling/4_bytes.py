data = b"hello"
print(type(data))
print(data)

data2 = "hello"
print(type(data2))
print(data2)



# Covert between them
# str -> bytes
encoded = "hello".encode("utf-8")
print("encoded: ", encoded)

# bytes -> str
decoded = b"hello".decode("utf-8")
print("decoded: ", decoded)


