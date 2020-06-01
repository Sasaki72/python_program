#4桁の数字を正しく入力してもらう

#【文字は要素を指定する事で１つずつ取得できる】
#入力された4桁の文字も、それぞれの文字を４つに分けて管理すると処理が楽になる
#pythonは文字列はリストと同じ様に[]の添字を使って、先頭から順に一文字ずつ取り出せる
#例えば、ユーザーから「5329」と入力された時、「b[0]」を参照すると「5」と言う文字が、「b[1]」を参照すると「3」と言う文字が得られる

# coding:utf-8
import random

b = input("数を入れてね>")  #ユーザーに4桁の数字を入力してもらう
print(b[0])               #左から順に1文字目から4文字目まで入力してもらう
print(b[1])
print(b[2])
print(b[3])

#【応用】
# s = input("数を入れてね>")
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])

#【入力エラーをはじく】
# 入力の際に桁数が３桁や5桁、また数字でなくaやbなどの文字が入った時にエラーとしてはじく
#①4桁であるかチェックする
#pythonでは「len関数」を使って文字列の長さを求められる
# len(b)が4ではないーーすなわち、「if len(b)!4:」と言う条件を指定すると4桁で入力されたかどうか確認できる

# b = input("数を入れてね>")
# if len(b)! = 4:　　　「もし変数のbの文字が4桁でないなら」と言う意味
#     print("4桁の数字を入力してください")

#しかし実際は4桁の確認だけではなく、4桁でなければ4桁がきちんと入力されるまで、繰り返し入力する様に「while」を使ってループ処理する


#coding:utf-8
import random

isok = False
while isok == False:
    b = input("数を入れてね>")
    if len(b) != 4:
      print("4桁の数字を入力してください")
    else:
      isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])

# 【応用】
#coding:utf-8
# import random

# isok = False
# while isok == False:
#     p = input("数を入れてね>")
#     if len(p) != 4:
#       print("4桁の数字を入力してください")
#     else:
#       isok = True

# print(p[0])
# print(p[1])
# print(p[2])
# print(p[3])