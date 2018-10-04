# List
name_list = ["RR", "GG", "QQ", "OO", "PP"]

print("first:", name_list[0])
print("last:", name_list[-1])
print(name_list[0:3])

del name_list[0]
name_list = name_list + ["WW"]

print(name_list)

name_list2 = ["RR", "GG", "QQ", "OO", "PP", "RR", "EE", "GG"]
name_list2 = [x for x in name_list2 if x != "GG"]

print(name_list2)

# for x in   x => 區域變數
for x in name_list:
    print(x)

# range(i, j) => 群集
list2 = range(0, 5)
for x in list2:
    print(x)