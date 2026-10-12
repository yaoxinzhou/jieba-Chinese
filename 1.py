import jieba
import jieba.posseg as pseg
with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()
print("原文：")
print(text)
print("=" * 50)
words = jieba.lcut(text)
print("分词结果：")
print("/".join(words))
print("=" * 50)
print("词性标注结果：")
for word, flag in pseg.cut(text):
    print(f"{word}({flag})", end=" ")
