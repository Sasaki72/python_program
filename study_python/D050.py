# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a = list(map(int,input().split()))

if a[0] >= 5:
    a[0] = 5
if a[1] >= 5:
    a[1] = 5
print(a[0] + a[1])

# ifで定義することができて、それを使って処理ができる