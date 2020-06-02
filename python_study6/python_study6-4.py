#【ボタンが押された時にメッセージを表示しよう】
#入力された数字をチェックするためのボタンを配置して、さらに、ボタンがクリックされた時にメッセージを表示できるようにする

#【ボタンを配置する】
#ボタンを配置する方法はラベルやエントリーと同様
#Buttonメソッドを利用して次のようなプログラムを作る
#カッコの中の引数「root」はボタンを配置する対象となるウィンドウ、「text = ""」はボタンに表示する文字、つまりボタン名
#「font」以下の引数で、フォントを「Helvetica」に、サイズを14ポイントとした。
#また、作成したボタンを「button1」と言う変数に代入している

#button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14))
#作成したら「placeメソッド」を使って、指定した座標に配置する

#ここでは、x座標が220, y座標が60の位置に配置してみる
#button1.place(x = 220, y = 60)

#coding:utf-8
import tkinter as tk

root = tk.Tk()
root.geometry("400x150")  
root.title("数当てゲーム")  

labell = tk.Label(root, text="数を入力してね", font=("Helvetica",14))   
labell.place(x = 20, y = 20)                   

editboxl = tk.Entry(width = 4, font=("Helvetica",28))                 
editboxl.place(x = 120, y = 60)                                       

button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14))    #修正箇所
button1.place(x = 220, y = 60)                                         #修正箇所

root.mainloop()  

#【クリックされた時に実行される関数を結びつける】
# 現状ではチェックボタンを押しても何も起こらない
# ①クリックされた時に実行する関数を作る
# 例えば、「ButtonCilck」という名前の関数を作る

# def ButtonCilck()
#  ・・ここに好きな処理を書く・・

# ②ボタンがクリックされた時に①の関数を実行するように結びつける
# それには、ボタンを作るときのButtonメソッドに「command=関数名」の引数を追加する

# button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14), command = ButtonCilck)  #実行したい関数名を書く
#クリックされた時に「ButtonCilck」という関数が実行されるようになる

# button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14), command = ButtonCilck) 
#                                                                                  ↓クリック後の関数実行の指定
#                                                                             def ButtonCilck()
#                                                                           クリックされたときの処理を書いておく
#上記の様に「指定した動作」と「実行するプログラム」を結びつけるプログラミング手法を「イベントドリブン(event-driven)」と言う
#「イベント」は「動作」や「事象」のことで、「何か事象が起きた」ことを示す。ここでは代表的な「クリック」だが、他には「ダブルクリック」「右クリック」「キーの入力」「マウスが動いた」「一定時間が経過した」など様々なイベントがある

#【メッセージを表示してみよう】
# def ButtonCilck()
#  ・・ここに好きな処理を書く・・

#これで、ボタンがクリックされた時に、ButtonCilck関数が実行される様になったので画面にメッセージを表示してみる
#メッセージを表示するには「tkinter」の「messagebox」と言うパッケージに含まれる関数を使う。
#まず次の様に記述して、「tkinter.messagebox」を読み込む
#「messagebox」の名前は長いので、ここでは「as」を使って、「tmsg」と言う短い名前にした。もちろん、名前は何でもOK

# 「import tkinter.messagebox as tmsg」
#「tkinter」の「messagebox」には色々な関数があり様々な方法でメッセージを表示できる。ここでは、情報を表示するためのshowinfo関数を使ってメッセージを表示する

#【tkinter.messageboxの関数】
# showinfo          情報を表示する
# showwarning       警告を表示する
# showerror         エラーを表示する
# askquestion       テキストボックスを持つメッセージを表示し、文字入力できる
# askokcancel       [OK]と[キャンセル]の２つのボタンを持つメッセージを表示する
# askyesno          [はい]と[いいえ]の２つのボタンを持つメッセージを表示する
# askretrycancel    [再試行]と[キャンセル]の２つのボタンを持つメッセージを表示する
#《MEMO》「showinfo」と「showwarning」と「showerror」の違いは画面に表示されるときのアイコンの違い

# tmsg.showinfo("タイトル","表示したい文字")
#そこで、ButtonCilck関数を次の様に定義する

# def ButtonCilck():
#     tmsg.showinfo("テスト", "クリックされたよ")
#これまで作成した関数に修正箇所として追加し、実行すると、ボタンをクリックした時に「テスト」というタイトルで「クリックされたよ」というメッセージが表示される


#coding:utf-8
import tkinter as tk
import tkinter.messagebox as tmsg               # messageboxパッケージを読み込む

# ボタンがクリックされたときの処理
def ButtonCilck():                              # クリックされた時にメッセージを表示
    tmsg.showinfo("テスト", "クリックされたよ")     # クリックされた時にメッセージを表示

# メインのプログラム
root = tk.Tk()
root.geometry("400x150")  
root.title("数当てゲーム")  

labell = tk.Label(root, text="数を入力してね", font=("Helvetica",14))   
labell.place(x = 20, y = 20)                   

editboxl = tk.Entry(width = 4, font=("Helvetica",28))                 
editboxl.place(x = 120, y = 60)                                       

button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14)
, command = ButtonCilck)                          # クリックされた時にこの関数を実行するための指定
button1.place(x = 220, y = 60)                                         

root.mainloop()
