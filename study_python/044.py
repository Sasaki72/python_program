# 解答①
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a = input()
b = a.split()
if b[1][0] == "F":
    print("Hi, Ms. " + b[0])
elif b[1][0] == "M":
    print("Hi, Mr. " + b[0])


# 解答②
a = list(map(str,input().split()))
if a[1][0] == "F":
    print("Hi, Ms. " + a[0])
elif a[1][0] == "M":
    print("Hi, Mr. " + a[0])


# 解答③
a = list(map(str,input().split()))
if a[1][0] == "F":
    print("Hi, Ms. " + a[0])
else:
    print("Hi, Mr. " + a[0])