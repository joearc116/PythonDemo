# 終極密碼
import random

low = 1
h = 100
ans = random.randint(low, h)
while True:

    msg = "輸入:" + str(low) + "~" + str(h)

    guess = int(input(msg))

    if ans == guess:
        print("猜中了", ans)
        break
    elif guess > ans:
        h = guess
        print("請選擇", low, "-", h)
    else:
        low = guess
        print("請選擇", low, "-", h)








