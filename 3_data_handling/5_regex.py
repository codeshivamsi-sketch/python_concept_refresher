# Use to find, split, replace
import re

# split on one or more new lines
text = "hello world\n\npython"
chunks = re.split(r'\n\n+', text)
print(chunks)



# find and replace using pattern
text2 = "hello    world"
# replace multiple spaces with one
clean = re.sub(r'\s+', ' ', text2)
print(clean)




 # extract all matches
text3 = "price is $10 and $25"
prices = re.findall(r'\$\d+', text3)
print(prices)


