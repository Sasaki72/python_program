# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a = input()
li = []
for i in range(int(a)):
    b = input()
    li.append(b)
print("Hello " + ",".join(li) + ".")