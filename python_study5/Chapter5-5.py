# 【ヒットとブローを判定しよう】
# これまでは、変数aには4桁のランダムな数字が、変数bにはユーザーが入力した4桁の数字が入力されるところまできた。あとは、両者を判定してヒットかブローかを判定する

#【ヒットを判定しよう】
# hit = 0                 ヒットした数
# if a[0] == int(b[0]):   1桁目
#   hit = hit + 1
# if a[1] == int(b[1]):   2桁目
#   hit = hit + 1
# if a[2] == int(b[2]):   3桁目
#   hit = hit + 1
# if a[3] == int(b[3]):   4桁目
#   hit = hit + 1
#実は、これはforループでも書くことができる。
# ↓

# hit = 0
# for i in range(4)
#   if a[i] == int(b[i]):
#     hit = hit + 1
#この様にforループでまとめる事ができる

#【ブローを判定しよう】
# ブローは「位置は正しくないが、その数字が含まれている」という状況
#これを判定するには、変数bの各桁の値と合致するかを確かめる操作となる

#   4    1    1    9
# a[0]  [1]  [2]  [3]
#   ↑① ↗︎② ↗︎③ ↗︎④
#  "1"  "4"  "3"  "9"
# b[0]  [1]  [2]  [3]  
# ブロー

# ①b[0]がa[0]と合致しているかを調べる → していない 
# ②b[0]がa[1]と合致しているかを調べる → している → ブロー
# ③すでに②でブローと分かっているので判定不要
# ④すでに②でブローと分かっているので判定不要
# ということになり、一番左の桁は「ブローしている」となる
# 実際にこの判定プログラムで記述すると、b[0]に対して、a[0],a[1],a[2],a[3]を比較すれば良い

#blow = 0 
#for i in range(4):
#  if int(b[0]) == a[i]:    b[0]がa[0],a[1],a[2],a[3]と合致するかをループで順に調べる
#    blow = blow + 1
#    break                  合致したらそこで終了
#ブローだと分かっ時にbreakして、そこで判定をやめるのはブローを重複して数えないため。
#breakしないと③でもう一度合致してしまうので、ブローの数が２になってしまう

#【重複した判定を除外する】
# ヒットとブローの判定は良いが、「ブローかつヒット」の場合があるので、ifに指定した条件が実は不十分
#例えばユーザーが入力した値が「9439」であるとします。この時、b[0]のa[3]の「9」に合致するのでブローと思いきや、a[3]はb[3]に合致しており「ヒット」です。このままだと、ヒットとブローで重複して数えてしまうので、「除外する必要がある。」

#   4    1    1    9
# a[0]  [1]  [2]  [3] 　　　
#  ↑① ↗︎② ↗︎③ ↗︎④  ↕︎(ヒットしているのでブローにしない)　
#  "9"  "4"  "3"  "9"
# b[0]  [1]  [2]  [3]     (ユーザー側)
# ブロー
#そこで、これを除外するよう、「ブロー判定のifの条件を次のように変更」する

#if (int(b[0]) == a[i]) and (a[i] != int(b[i])) and (a[0] != int(b[0])):
#「nd (a[i] != int(b[i])) and (a[0] != int(b[0])):」 が除外する条件
# これは2桁目以降も同様にチェックしていく

#for i in range(4):
#if (int(b[1]) == a[i]) and (a[i] != int(b[i])) and (a[1] != int(b[1])):
#b[1]　入力した2桁目
#同様に3桁目と4桁目もチェックすると

#blow = 0
#for i in range(4):
#  if (int(b[0]) == a[i]) and (a[i] != int(b[i])) and (a[0] != int(b[0])):
#     blow = blow + 1
#     break
#for i in range(4):
#  if (int(b[1]) == a[i]) and (a[i] != int(b[i])) and (a[1] != int(b[1])):
#     blow = blow + 1
#     break
#for i in range(4):
#  if (int(b[2]) == a[i]) and (a[i] != int(b[i])) and (a[2] != int(b[2])):
#     blow = blow + 1
#     break
#for i in range(4):
#  if (int(b[3]) == a[i]) and (a[i] != int(b[i])) and (a[3] != int(b[3])):
#     blow = blow + 1
#     break
#となるが長すぎるので、ループを使って短く書く

#biow = 0
#for j in range(4):
#  for i in range(4): 0,1,2,3とユーザーの入力欄をずらしてループする
#    if(int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
#      blow = blow + 1
#      break
#b[j]はユーザーが入力したj桁目
#少し複雑だが今回は「j」という変数を使いましたが、もちろん変数名は何でも構わない


#【ヒットが4になるまで繰り返す】


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

#「print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))」
# この部分を「#」でコメントアウトする事によって、答えを表示しないようにできる
# 再度、答えを見たいときは「#」を外せば見れるようになる
