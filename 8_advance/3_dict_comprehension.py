# without comprehension
names = ["tom", "bob", "jerry"]
lengths = {}
for name in names:
    lengths[name] = len(name)
print(lengths)




# with comprehension
lengths2 = {name: len(name) for name in names}
print(lengths2)






# without comprehension
scores = {"tom": 87, "harry": 40, "jerry": 70}

# .items() -> returns key, value pair as tuple so we can pack both in loop.
print('score.items: ', scores.items()) 

passed = {}
for name, score in scores.items():
    if score >= 50:
        passed[name] = score

print(passed)




# with compreshension
passed2 = {name: score for name, score in scores.items() if score > 50}
print(passed2)
