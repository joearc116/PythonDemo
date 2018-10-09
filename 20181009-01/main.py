import jieba

f = open("a.txt", "r", encoding="utf-8")
article = f.read()
f.close()

jieba.load_userdict("dict.txt")
# ["word", "word", .....]
sep = jieba.cut(article)
print(" ".join(sep))

# from jieba import analyse
from jieba.analyse import extract_tags

keywords = extract_tags(article, 5)
print("關鍵字", keywords)