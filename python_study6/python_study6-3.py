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

