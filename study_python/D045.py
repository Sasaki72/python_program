# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a = int(input())
if a == 5:
    print("A")
elif a == 4:
    print("B")
elif a == 3:
    print("C")
elif a == 2:
    print("D")
elif a == 1:
    print("E")


# 解答②
a = input()
a = a.replace("5", "A")
a = a.replace("4", "B")
a = a.replace("3", "C")
a = a.replace("2", "D")
a = a.replace("1", "E")
print(a)

# ※【replace】
# 　文字列の中の指定した文字列を別の文字列に置換する
# (例)
# Apple.replace("PP", "oo")
# Apple