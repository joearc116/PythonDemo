# 鴨子型別
def add(n1, n2):
    return n1 + n2

print(add(2, 3))
print(add("Hello", "World"))

# 不定參數 *args
def add_multiple(*nlist):
    r = 0
    for n in nlist:
        r = r + n
    return r

# print(add_multiple([1, 2, 3, 8]))
print(add_multiple(1, 2, 3, 8))

# ex:open()
def score(s, div=1, permu=0):
    return s/div + permu

print(score(9, 2, 20))
print(score(9, 2))
print(score(9))
print(score(10, permu=10))
