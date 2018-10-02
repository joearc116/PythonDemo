# For Loops

i = 0

while i < 10:
    print("Hello", i + 1)
    i = i + 1

j = 0
k = 0
while j < 10:
    k = k + (j + 1)
    j = j + 1
    print(k)

# 費式數列

lasttwo = 0
lastone = 0
times = 0
while times < 10:
    if times == 0:
        lasttwo = 0
        ans = 0
    elif times == 1:
        lastone = 1
        ans = 1
    else:
        ans = lasttwo + lastone
        lasttwo = lastone
        lastone = ans
    print("第", times + 1, "項:", ans)
    times = times + 1

#

r = 0
h = 0

while r <= 50:
    r = r + (h + 1)
    h = h + 1
print("最後加的 =", h)

