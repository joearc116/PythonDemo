# 引述random

import random

player = int(input("請輸入[0]棒[1]虎[2]雞[3]蟲"))

com = random.randint(0, 3)

trans = ["棒", "虎", "雞", "蟲"]

print("你的選擇", trans[player])
print("電腦選擇", trans[com])

# 取餘數 mod => %
if player == (com - 1) % 4:
    print("我贏了")
elif player == (com + 1) % 4:
    print("我輸了")
else:
    print("平手")