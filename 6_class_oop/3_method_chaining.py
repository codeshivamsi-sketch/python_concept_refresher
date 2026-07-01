text = "   Hello Shivam    "


# Without chaining
text = text.strip()
text = text.lower()
text = text.replace("shivam", "world")
print(text)


# With chaining
print(text.strip().lower().replace("shivam", "world"))

