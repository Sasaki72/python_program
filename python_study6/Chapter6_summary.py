# Chapter６ 「数当てゲームをグラフィカルにしよう」
#【ゲームの見た目をどう設計するか】
#Chapter5では画面上でしたが、今回はウィンドウ表示された画面上で数当てゲームを遊べるように改造する
#具体的には、ウィンドウ画面内に4桁の数字を入力し、「チェック」ボタンをクリックするとヒットとブローの数を表示するプログラムを作る
#今回のプログラミングのポイントは、
# ①ボタンがクリックされた時にテキストボックスに入力された文字をどのようにして読み込むのか　
# ②ゲームを円滑に進めるためにユーザーに対するメッセージをどのように表示するのか
#この2点です。
#【ゲームらしく設計するには】
# ポイントは「入力履歴」を残してあげること
#履歴で「H」がヒット、「B」がブローの数を表示する
#このように「入力した数字、当たり、外れ履歴」を作ることでユーザーが考えやすく、見た目もゲームらしくなる


#「Python」でウィンドウを表示してみよう
#【ウィンドウを表示させる】
# ウィンドウ、入力用のテキストボックス、ボタンなど、グラフィカルな画面で操作するための部分群を集めたものを「GUIツールキット」と呼ぶ
#GUIツールキットにはいくつかありますが、Pythonには標準で「tkinter(ティーケイ・インター)」と言うGUIツールキットが付属してるので今回はこれを使う
#《MEMO》
#他に有名なGUIツールキットとして「wxPython」がある
# Macで「tkinter」を使うには「Tcl/Tk」のインストールが必要
#coding:utf-8
import tkinter as tk
root = tk.Tk()    #ウィンドウを作る   #「as」を使わないと「root = tkinter.Tk()」となる
root.mainloop()   #ウィンドウを表示する
#「as tk」としたのは、これ以降tkinterを省略表示するため。
# 「as」というのは、それを「指定した別名で使う」という意味。
# もちろん、上記以外でも別名は何でもいい「import tkinter as t」とすれば「root = t.Tk()」ともっと短くできる
# 上記の例だと、これ以降「tk」という表記で「tkinter」を使っていく、という意味になる
# tkinterは「オブジェクト」という仕組みを使ってウィンドウを操作する
# 「オブジェクト」= 部品のこと　
# 「オブジェクト」には「メソッド(method)」と呼ばれる関数があり、それを実行することで、様々な操作ができる
#上記で書いたコード、
#「root = tk.Tk()」の通り、ウィンドウを操作するにはオブジェクトを作るところから始める
#こうすることでオブジェクトが変数rootに代入され、変数rootを通じて様々なウィンドウを操作できる
#作成したウィンドウを表示するには「mainloop」のメソッドを実行する
#「root.mainloop()」
# 《MEM0》
#上記では「root = tk.Tk()」として「root.mainloop()」としたが、
#変数名は任意なので、例えば「r = tk.Tk()」として「r.mainloop()」と短くすることもできる
#分かりにくいかもしれないが、
# root = tk.Tk()
# root.mainloop()  
#この2行は、tkinterで「ウィンドウを表示するときの決まり文句」です
#《ウィンドウに命令を与える》
#「root.やりたい操作()」
#【ウィンドウサイズを変更する】
# ウィンドウサイズを変更するには「geometry」メソッドを使う
#「横の幅 × 高さ」で設定する。
# 例えば、「400 × 150(ピクセル)」に変更するときは
# 「root.geometry("400x150")」
#ここでの注意は「x」は×(かける)ではなく小文字のx(エックス)
#coding:utf-8
import tkinter as tk
root = tk.Tk()
root.geometry("400x150")  #修正箇所
root.mainloop()  
#【ウィンドウのタイトルを設定する】
#タイトル変更には「titleメソッド」を使う
#「root.title("数当てゲーム")」と入力する
#coding:utf-8
import tkinter as tk
root = tk.Tk()
root.geometry("400x150")  #修正箇所
root.title("数当てゲーム")  #修正箇所
root.mainloop()  


#【メッセージと入力欄を配置する】
#《メッセージを配置する》　
# まずは「数を入力してね」のメッセージをウィンドウに貼り付ける
#このメッセージを「ラベル(label)」と言う
#Labelメソッドを使うことで実行する
# labell = tk.Label(root, text="数を入力してね")　　#tkは先ほどのtkintreの省略
#カッコの中に指定している１つめの値「root」は、ラベルを貼り付ける対象となるウィンドウで、「text=""」の部分が表示したいメッセージ
#ラベルを作成したら、ウィンドウに配置する。
# 配置方法はいくつかあるが、比較的分かりやすい「placeメソッド」を使う
# labrll.place(x = 20 , y = 20)
#placeメソッドではカッコの中に「(x = x座標 、 y = y座標)」と言う形で配置する座標を決める
#なお、pythonのtkintreは、ウィンドウの表示エリアの左上が、「(0,0)」で右下に向けて伸びる座標
#coding:utf-8
import tkinter as tk
root = tk.Tk()
root.geometry("400x150")  
root.title("数当てゲーム")  
labell = tk.Label(root, text="数を入力してね")   #修正箇所
labell.place(x = 20, y = 20)                   #修正箇所
root.mainloop()  
#テキストの入力欄もウィンドウに配置する　
#テキストの入力欄は、tkinterでは「エントリー(Entry)」と呼ぶ
#Entryメソッドを実行するとテキストの入力欄を作れる
# editboxl = tk.Entry(width = 4)
#カッコに指定している「(width = 4)」はこのテキストの入力欄の幅です。
#今回は数字を４つ入力するので、４文字分の入力欄を指定
#ここでは、作成したEntryを「editboxl」と言う変数に代入している
#《MEMO》Entryメソッドには他にもフォントなど指定できるが、ここでは省略
# 作成したらplaceメソッドを使って配置する
# editboxl.place(x = 120, y = 20)
#coding:utf-8
import tkinter as tk
root = tk.Tk()
root.geometry("400x150")  
root.title("数当てゲーム")  
labell = tk.Label(root, text="数を入力してね")   
labell.place(x = 20, y = 20)                   
editboxl = tk.Entry(width = 4)    #修正箇所
editboxl.place(x = 120, y = 20)   #修正箇所
root.mainloop()  
#フォントの種類とサイズを変える
# やり方は、Labelメソッドの一番後ろに「font=("フォント名",フォントサイズ)」と言う引数を追加する
# labell = tk.Label(root, text="数を入力してね", font=("Helvetica",14)) 
#この例だと、「Helvetica」と言うフォントで「14ポイント」と言うサイズを指定したことになる
# 《MEMO》 ポイントのサイズは単位で「１ポイントは約0.35mm」
#【指定できるフォントは、標準で次の3種類】
#・Times(明朝体っぽいもの)
#・Helvetica(ゴシック体っぽいもの)
#・Courier(等幅のタイプライタのようなもの)
#これ以外に、「MSゴシック」などパソコンにインストールされているフォントを指定することもできる
# 《MEMO》フォント名は大文字、小文字、全角、半角、空白の有無などを区別するので注意
#今回はエントリー(テキスト入力欄)も、次のように変更した
# editboxl = tk.Entry(width = 4, font=("Helvetica",28))
#「フォントサイズを変更した場合、そのままの位置だと文字同士が重なるのでplaceメソッドで指定するX座標、Y座標も変更する」
#coding:utf-8
import tkinter as tk
root = tk.Tk()
root.geometry("400x150")  
root.title("数当てゲーム")  
labell = tk.Label(root, text="数を入力してね", font=("Helvetica",14))   #修正箇所
labell.place(x = 20, y = 20)                   
editboxl = tk.Entry(width = 4, font=("Helvetica",28))                 #修正箇所
editboxl.place(x = 120, y = 60)                                       #修正箇所
root.mainloop()  
#《COLUMN》
# 利用できるフォント一覧を取得する
# import tkinter as tk
# for f in tk.Tk().call("font", "families")
#     print(f)


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
# def ButtonClick()
#  ・・ここに好きな処理を書く・・
# ②ボタンがクリックされた時に①の関数を実行するように結びつける
# それには、ボタンを作るときのButtonメソッドに「command=関数名」の引数を追加する
# button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14), command = ButtonClick)  #実行したい関数名を書く
#クリックされた時に「ButtonCilck」という関数が実行されるようになる
# button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14), command = ButtonClick) 
#                                                                                  ↓クリック後の関数実行の指定
#                                                                             def ButtonClick()
#                                                                           クリックされたときの処理を書いておく
#上記の様に「指定した動作」と「実行するプログラム」を結びつけるプログラミング手法を「イベントドリブン(event-driven)」と言う
#「イベント」は「動作」や「事象」のことで、「何か事象が起きた」ことを示す。ここでは代表的な「クリック」だが、他には「ダブルクリック」「右クリック」「キーの入力」「マウスが動いた」「一定時間が経過した」など様々なイベントがある
#【メッセージを表示してみよう】
# def ButtonClick()
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
# def ButtonClick():
#     tmsg.showinfo("テスト", "クリックされたよ")
#これまで作成した関数に修正箇所として追加し、実行すると、ボタンをクリックした時に「テスト」というタイトルで「クリックされたよ」というメッセージが表示される
#coding:utf-8
import tkinter as tk
import tkinter.messagebox as tmsg               # messageboxパッケージを読み込む
# ボタンがクリックされたときの処理
def ButtonClick():                              # クリックされた時にメッセージを表示
    tmsg.showinfo("テスト", "クリックされたよ")     # クリックされた時にメッセージを表示
# メインのプログラム
root = tk.Tk()
root.geometry("400x150")  
root.title("数当てゲーム")  
labell = tk.Label(root, text="数を入力してね", font=("Helvetica",14))   
labell.place(x = 20, y = 20)                   
editboxl = tk.Entry(width = 4, font=("Helvetica",28))                 
editboxl.place(x = 120, y = 60)                                       
button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14), command = ButtonClick)                          # クリックされた時にこの関数を実行するための指定
button1.place(x = 220, y = 60)                                         
root.mainloop()


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


#【履歴を表示しよう】
#《履歴を表示するテキストボックスを付ける》
# 履歴の表示には、テキストボックスという部品を使う
# しかし、今のウィンドウサイズでは、テキストボックスを入れるスペースがないのでウィンドウサイズを大きくする
# root.geometry("400x150") → root.geometry("600x400") に変更
# そして広がった場所にテキストボックスを配置する
# 引数には「配置先のウィンドウ」と「フォント」を指定する
# テキストボックスには、「Textメソッド」を実行する
#　フォントサイズを14に変更して「rirekibox」という変数に代入した
#rirekibox = tk.Text(root, font("Helvetica", 14))
#《MEMO》 Textメソッドには、他にも色や余白、折り返し幅などを指定できるが今回は省略
# 作成したら「# ウィンドウを作る」の命令群の下に「# 履歴表示のテキストボックスを作る」とコメントを追記する
# さらに、これまで使ってきたラベルやエントリー、ボタンなどと同様に、placeメソッド使って、今回は(400,0)の位置に、幅200、高さ400で追記する
# rirekibox.place(x=400, y=0, width=200, height=400)
#                                 幅        高さ
#【履歴を表示する】
# 最後に、ヒット＆ブローの判定結果をメッセージとしてではなく、テキストボックスに表示し、履歴として残るようにする
#今までは判定結果を以下のように表示
#「ヒット数とブロー数を表示」
#tmsg.showinfo("ヒット", "ヒット" + str(hit) + "/" + "ブロー" + str(blow))
# この部分を変更する
# テキストボックスに文字を追加するには、「insertメソッド」を使う
# 最初の引数に「tk.END」を指定すると、「末尾」に挿入できる。
# 書き換えは以下のようになる(全部書き換える)
# rirekibox.insert(tk.END, b + " / H:" + str(hit) + "B:" + ste(blow) + "\n")
#《MEMO》ここでは tkinterを「import tkinter as tk」のように「tk」と言う名前でインポートしているので「tk.END」です
# もし他の名前でインポートした場合は「その名前.END」となる
#今回はヒットは「H:」、ブローは「B:」で表示するようにした
# coding:utf-8
import random
import tkinter as tk
import tkinter.messagebox as tmsg
# ボタンがクリックされた時の処理
def ButtonClick():
    # テキスト入力欄に入力された文字列を取得
    b = editbox1.get()
    # Lesson 5-4のプログラムから判定部分を拝借
    #4桁の数字かどうかを判断する
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
      # 4桁の数字であった時
      # ヒット判定
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
      # ヒットが4なら当たりで終了
      if hit == 4:
          tmsg.showinfo("当たり", "おめでとう御座います。当たりです")
          # 終了
          root.destroy()
      else:
          # ヒット数とブロー数を表示
          rirekibox.insert(tk.END, b + " /H:" + str(hit) + "B:" + str(blow) + "\n")
# メインのプログラム
# 最初にランダムな4つの数字を作成しておく
a =[random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9)]
# ウィンドウを作る
root = tk.Tk()
root.geometry("600x400")
root.title("数当てゲーム")
# 履歴表示のテキストボックスを作る
rirekibox = tk.Text(root, font=("Helvetica", 14))
rirekibox.place(x=400, y=0, width=200, height=400)
# ラベルを作る
labell = tk.Label(root, text="数を入力してね", font=("Helvetica", 14))
labell.place(x = 20, y = 20)
# テキストボックスを作る
editbox1 = tk.Entry(width = 4, font=("Helvetica", 28))
editbox1.place(x = 120, y = 60)
# ボタンを作る
button1 = tk.Button(root, text = "チェック", font=("Helvetica", 14), command=ButtonClick)
button1.place(x = 220, y = 60)
# ウィンドウを表示する
root.mainloop()

