# coding:utf-8
import tkinter as tk

# 円の座標
x = 300
y = 200

def move():
    global x, y             # 増やしていくので右に動く
    # 今の円を消す
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill = "white", width = 0)
    # X座標を動かす
    x = x + 1
    # 次の位置に円を描く
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill = "red", width = 0)
    # 再びタイマー
    root.after(10, move)    # 次も実行されるようにするため再設定する

# ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

# キャンバスを置く
canvas =tk.Canvas(root, width =600, height =400, bg="white")
canvas.place(x = 0, y = 0)

# タイマーを設定する
root.after(10, move)        # 0.01秒後にmove関数が実行されるように設定する

root.mainloop()


# 今回はafterメソッドを使い、0.01秒 (=10ミリ秒)後に、move関数を実行するようにした
root.after(10, move)