# 引述random

import random

player = int(input("請輸入[0]剪刀[1]石頭[2]布"))

com = random.randint(0, 2)

trans = ["剪刀", "石頭", "布"]

print("你的選擇", trans[player])
print("電腦選擇", trans[com])

# 取餘數 mod => %
if player == com:
    print("平手")
elif player == (com + 1) % 3:
    print("我贏了")
else:
    print("我輸了")
