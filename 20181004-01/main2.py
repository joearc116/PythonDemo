# 三門問題
import random

win = 0
lose = 0

for i in range(1000000):
    # 準備門
    doors = ["羊", "羊"]
    c = random.randint(0, 2)
    doors.insert(c, "車")

    # 選門
    c = random.randint(0, 2)
    del doors[c]

    # 開一道羊的門
    doors.remove("羊")
    if doors[0] == "車":
        win = win + 1
    else:
        lose = lose + 1

print("WIN times", win)
print("LOSE times", lose)
total = win + lose
print("WIN ration", win / total * 100, "%")
print("WIN ration", lose / total * 100, "%")
