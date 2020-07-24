# coding:utf-8
import random

isok = False
while isok == False:
  b = input("数を入れてね>")
  if len(b) != 4:
    print("4桁の数字を入力してください")
  else:
    if (b[0] < "0") or (b[0] > "9"):
        print("数字ではありません")
    elif (b[1] < "0") or (b[1] > "9"):
        print("数字ではありません")
    elif (b[2] < "0") or (b[1] > "9"):
        print("数字ではありません")
    elif (b[3] < "0") or (b[1] > "9"):
        print("数字ではありません")
    else:
        isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])



#coding:utf-8
import re

isok = False
while isok == False:
    b = input("数を入れてね>")
    if not re.match(r"^\d\d\d\d$",b):
        print("4桁の数字を入力してください")
    else:
        isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])


#【完成版】

#coding:utf-8
import random

a =[random.randint(0 , 9),
    random.randint(0 , 9),
    random.randint(0 , 9),
    random.randint(0 , 9)]

#テストのため答えを表示
print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))

while True :
    #Lesson 5-4のプログラム
    #4桁の数字かどうかを判断する
    isok = False
    while isok == False:
        b = input("数を入れてね>")
        if len(b) != 4:
            print("4桁の数字を入力してください")
        else:
            kazuok = True
            for i in range(4):
                if (b[i] <"0") or (b[i] >"9"):
                    print("数字ではありません")
                    kazuok = False
                    break
            if kazuok :
                isok = True

    #4桁の数字であったとき
    #ヒットを判定
    hit = 0
    for i in range(4):
      if a[i] == int(b[i]):
        hit = hit + 1

    #ブローを判定
    blow = 0
    for j in range(4):
      for i in range(4):
        if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
          blow = blow + 1
          break

    #ヒット数とブロー数を表示
    print("ヒット" + str(hit))
    print("ブロー" + str(blow))

    #ヒットが４なら当たりで終了
    if hit == 4:
        print("当たり！")
        break