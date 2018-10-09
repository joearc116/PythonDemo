# 讀檔/寫檔
print("UTF-8", "測試".encode("utf-8"))

f = open("in.txt", "r", encoding="utf-8")
s = f.read()
f.close()

print(s)

f2 = open("out2.txt", "w", encoding="utf-8")
f2.write("123456789")
f2.close()
