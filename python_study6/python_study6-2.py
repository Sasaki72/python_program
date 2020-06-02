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

