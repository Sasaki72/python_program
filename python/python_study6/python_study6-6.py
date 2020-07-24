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

