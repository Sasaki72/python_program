# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

test = input()
test1 = test.split()
li = [test1[0]]
a = int(test1[0])
for i in range(1,10):
    a = a + int(test1[1])
    li.append(str(a))
print(" ".join(li))