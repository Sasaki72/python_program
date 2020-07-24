#【ヒット＆ブローの当たり判定を組み込もう】

#【入力されたテキストの値を取得する】
# はじめに知らないといけないのは、ウィンドウに配置したテキスト入力欄、つまりエントリーの部分に入力されたテキストを取得する方法
# 入力されたテキストは、「getメソッド」を使うと取得できる。
# ここまでのプログラムは次のテキスト入力欄を「editbox」という変数に代入してる

# editboxl = tk.Entry(wildth = 4, font=("Halvetica", 28))
# editboxl.place(x = 120, y = 60)
# だから次のようにeditboxlに対してgetメソッドを実行すると、この入力欄に入力されたテキストを取得できる

# editboxl.get()
# 実際にテストしてみる

# #coding:utf-8
# import tkinter as tk
# import tkinter.messagebox as tmsg

# # ボタンがクリックされたときの処理
# def ButtonClick():
#     # テキスト入力欄に入力された文字列を取得       #修正箇所
#     b = editboxl.get()                       #修正箇所
#     # メッセージとして表示する                   #修正箇所
#     tmsg.showinfo("入力されたテキスト", b)      #修正箇所

# # メインのプログラム
# # ウィンドウを作る                              #分かりやすくコメントを表示
# root = tk.Tk()
# root.geometry("400x150")  
# root.title("数当てゲーム")  

# # ラベルを作る                                  #分かりやすくコメントを表示
# labell = tk.Label(root, text="数を入力してね", font=("Helvetica",14))   
# labell.place(x = 20, y = 20)                   

# #テキストボックスを作る                           #分かりやすくコメントを表示
# editboxl = tk.Entry(width = 4, font=("Helvetica",28))                 
# editboxl.place(x = 120, y = 60)                                       

# #ボタンを作る                                   #分かりやすくコメントを表示
# button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14)
# , command = ButtonClick)                          # クリックされた時にこの関数を実行するための指定
# button1.place(x = 220, y = 60)                                         

# # ウィンドウを表示する                           　#分かりやすくコメントを表示
# root.mainloop()


#【ヒット＆ブローの値判定を作る】
#関数の処理のうち、以下の部分には「変数bにユーザーが入力した値」が格納されてる

# def ButtonClick():
#     テキスト入力欄に入力された文字列を取得
#     b = editboxl.get()
#これはLesson5-5で作成した時に、変数bに入れていたので、

# while True:
#     b = input("数を入れてね>")
#これをこのままコピー＄ペーストし、プログラムを調整すればいい

#ボタンがクリックされた時にヒット＆ブローの判定を追加する
#最初に「4桁のランダムな数を設定する」などの処理を加えたり、「当たった時に終了する」などの細かい修正を加えると、この時点で実際に当たるかどうかを判定してくれる


#coding:utf-8
import random
import tkinter as tk
import tkinter.messagebox as tmsg

# ボタンがクリックされたときの処理
def ButtonClick():
    # テキスト入力欄に入力された文字列を取得
    b = editboxl.get()

#   Lesson 5-4のプログラムから判定部分を拝借
#   4桁の数字かどうかを判定する
    isok = False
    if len(b) != 4:
        tmsg.showerror("エラー", "4桁の数字を入力してください")
    else:
          kazuok = True
          for i in range(4):
              if (b[i] < "0") or (b[i] > "9"):
                  tmsg.showerror("エラー", "数字ではありません")
                  kazuok = False
                  break
          if kazuok :
              isok = True

    if isok :
          #4桁の数字であったとき
          #ヒット判定
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

          #ヒットが4なら当たりで終了
          if hit == 4:
              tmsg.showinfo("当たり", "おめでとうございます。当たりです")
          #終了
          root.destroy()
    else:
          #ヒット数とブロー数を表示
          tmsg.showinfo("ヒット", "ヒット" + str(hit) + "/" + "ブロー" + str(blow))

# メインのプログラム
# 最初にランダムな４つの数字を作成しておく
a =[random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9)]

# ウィンドウを作る                              #分かりやすくコメントを表示
root = tk.Tk()
root.geometry("400x150")  
root.title("数当てゲーム")  

# ラベルを作る                                  #分かりやすくコメントを表示
labell = tk.Label(root, text="数を入力してね", font=("Helvetica",14))   
labell.place(x = 20, y = 20)                   

#テキストボックスを作る                           #分かりやすくコメントを表示
editboxl = tk.Entry(width = 4, font=("Helvetica",28))                 
editboxl.place(x = 120, y = 60)                                       

#ボタンを作る                                   #分かりやすくコメントを表示
button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14)
, command = ButtonClick)                          # クリックされた時にこの関数を実行するための指定
button1.place(x = 220, y = 60)                                         

# ウィンドウを表示する                           　#分かりやすくコメントを表示
root.mainloop()


#【ウィンドウを閉じる操作】
# ここでまだ入力できていないのが「ヒットが4なら当たりで終了」する操作です
#当たった時は次のようにする

#ヒットが4なら当たりで終了
# if hit == 4:
#     tmsg.showinfo("当たり", "おめでとうございます。当たりです")
#     # 終了
#     root.destroy()   ← プログラミングが終了する
# このようにdestroyメソッドを実行するとウィンドウが破棄されプログラムが終了する

