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
