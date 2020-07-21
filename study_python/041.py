#【参考解答】
num = list(map(int, input().split()))
if num[0] < num[1] * num[2]: 
    print("OK")
else:
    print("NG")


# 解答①
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a = input()
b = a.split()
if int(b[0]) < int(b[1]) * int(b[2]):
    print("OK")
else:
    print("NG")

# 解答②
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a = input()
b = a.split()
if int(b[0]) <= int(b[1]) * int(b[2]):
    print("OK")
else:
    print("NG")

# 解答③
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a = input()
b = a.split()
if int(b[0]) <= int(b[1]) * int(b[2]):
    print("OK")
if int(b[0]) > int(b[1]) * int(b[2]):
    print("NG")