# Dictionary 字典 {}

person = {"name": "Joe", "height": 175, "weight": 70}
print(person["name"])
print(person)
person["live"] = "Taipei"
print(person)

del person["weight"]
print(person)

for key in person:
    print(key, "=", person[key])
