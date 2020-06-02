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

#coding:utf-8
import tkinter as tk
import tkinter.messagebox as tmsg

# ボタンがクリックされたときの処理
def ButtonCilck():
    # テキスト入力欄に入力された文字列を取得
    b = editboxl.get()
    # メッセージとして表示する
    tmsg.showinfo("入力されたテキスト", b)

# メインのプログラム
# ウィンドウを作る
root = tk.Tk()
root.geometry("400x150")  
root.title("数当てゲーム")  

# ラベルを作る
labell = tk.Label(root, text="数を入力してね", font=("Helvetica",14))   
labell.place(x = 20, y = 20)                   

#テキストボックスを作る
editboxl = tk.Entry(width = 4, font=("Helvetica",28))                 
editboxl.place(x = 120, y = 60)                                       

#ボタンを作る
button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14)
, command = ButtonCilck)                          # クリックされた時にこの関数を実行するための指定
button1.place(x = 220, y = 60)                                         

# ウィンドウを表示する
root.mainloop()


#【ヒット＆ブローの値判定を作る】
