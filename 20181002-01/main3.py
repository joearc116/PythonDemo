# String API : replace

a = "hello\npython\n3"

b = a.replace("python", "world")
print(b)

# replace(old, new, max) => max 取代個數
a = a.replace("\n", "", 1)
print(a)

# upper() & lower
if "abc" == "ABC".lower():
    print("case1")
elif "abc" == "ABC".lower():
    print("case2")
elif "fff" == "ABC":
    print("case3")
