from urllib.request import urlopen, urlretrieve
import json
import os

for m in range(1, 13):
    print("處裡月份:", m)
    url = "https://www.google.com/doodles/json/2018/" + str(m) + "?hl=zh_TW"
    rep = urlopen(url)
    doodles = json.load(rep)

    for d in doodles:
        url = "https:" + d["url"]
        print(d["title"], url)
        base = "doodles/" + str(m)

        if not os.path.exists(base):
            os.mkdir(base)
        fname = base + "/" + url.split("/")[-1]

        urlretrieve(url, fname)
        # 等於下方程式
        # resp = urlopen(url)
        # img = resp.read()
        # f = open(fname, "wb")
        # f.write(img)
        # f.close()