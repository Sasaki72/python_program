# coding:utf-8
import tkinter as tk

# 円の座標と半径
x = 400
y = 300
# 移動量
dx = 1              
dy = 1

def move():
    global x, y, dx, dy
    # 今の円を消す
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill = "white", width = 0)
    # X座標を動かす
    x = x + dx
    # Y座標も動かす
    y = y + dy
    # 次の位置に円を描く
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill = "red", width = 0)
    # 端を超えていたら反対向きにする
    if x >= canvas.winfo_width():           # 右辺を越えた時
      dx = -1                               # 左方向へ
    if x <= 0:                              # 左辺を越えた時
      dx = +1                               # 右方向へ
    # Y座標についても同様
    if y >= canvas.winfo_width():           # 下辺を越えた時
      dy = -1                               # 上方向へ
    if y <= 0:                              # 上辺を越えた時
      dy = +1                               # 下方向へ
    #　再びタイマー
    root.after(10, move)


# ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

# キャンバスを置く
canvas =tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x = 0, y = 0)

# タイマーを設定する
root.after(10, move) 

root.mainloop()