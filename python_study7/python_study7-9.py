#【円だけでなく、四角、三角を混ぜて見よう】
# クラスやオブジェクトのメリットは、作った処理の一部だけを変更しやすい点
# ここでは、その性質を利用して、「四角」と「三角」を混ぜて描画する
# 
# 【機能の違いは描画する所だけ】
# これまで「円」を動かすプログラムでしたが、「四角」と「三角」を混ぜて動かしていく
# 四角と三角の違いは、「描画する形状」だけで、X座標やY座標は増減したり、キャンパスの端に達した時に向きを変えたりする処理はまったく同じ
# なので、描画する所だけを切り替えれば、同じプログラムで実現できる
# 四角形を扱うクラスをRectangle、三角形を扱うクラスをTriangleとして、これから作っていくと、その違いは牡蠣の図になる

# 図7-9-1
# 『円、四角形、三角形の処理の違い 』
#  【Ballクラス】            【Rectangleクラス】              【Triangleクラス】
#  《moveメソッド》           《moveメソッド》                《moveメソッド》
#  「円を消す」               「四角形を消す」                 「三角形を消す」
#   動かす                    動かす                         動かす      
#  「円を描く」                「四角形を描く」                「三角形を描く」
#   端で反対向きにする          端で反対向きにする               端で反対向きにする
# 
# 【図形を消す処理と描く処理を別のメソッドにする】
# クラスには、メソッド単位で処理を変更する機能がある
# この機能は「オーバーライド(override)」と呼ばれ、既存のクラスを改良して、別のクラスを作る基本となる
# 繰り返すが、この機能が使えるのは「メソッド単位」。上記の図7-9-1に示したように違うところは「消す」と「描く」ところです、ここを差し替えるには、それぞれ別のメソッドとして実装する必要がある
# そこでこれまで作ったBallクラスのmoveメソッドを図7-9-2のように変更する
# 
# def move(self, canvas):                               ｜      
#     # 今の円を消す                                      ｜
#     self.erase(canvas)                                ｜
#     # X座標、Y座標をを動かす                            　｜
#     self.x = self.x + self.dx                         ｜
#     self.y = self.y + self.dy                         ｜
#     # 次の位置に円を描く                                 ｜
#     self.draw(canvas)                                 ｜      このmoveメソッドの処理は
#     # 端を超えていたら反対向きにする                       ｜      「円」「四角形」「三角形」の
#     if (self.x >= canvas.winfo_width()):              ｜       どれでも同じ
#         self.dx = -1                                  ｜
#     if (self.x <= 0:)                                 ｜
#         self.dx = +1                                  ｜
#     if (self.y >= canvas.winfo_height()):             ｜
#         self.dy = -1                                  ｜
#     if (self.y <= 0:)                                 ｜
#         self.dy = +1                                  ｜
# def erase(self, canvas):     # 円を消す処理
#     canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = "white", width = 0)
# def draw(self, canvas):      # 円を描く処理
#       canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = self.color, width = 0)
# 
# ここでは、消す処理を「eraseメソッド」、描画する処理を「drawメソッド」に分離した
# 
# 【継承して四角形の描画クラスを作る】
# このようにBallクラスを改良しておくと、このクラスを基に、四角形を描画するRectangeクラスを作るのは簡単
# 既存のクラスを基に、新しいクラスを作ることを「継承」と言う
# 
# 継承するクラスの定義
# class新しいクラス名(基のクラス名)：
# 
# とすればよく、同名で同じ動作をするメソッドの記載は省略できる
# そこで、Ballクラスを継承させ、四角形を描画するRectangeクラスを作ると、次のようになる
# class Rectangle(Ball):
#     def erase(self, canvas):  # 四角形を消す
#         canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = "white", width = 0)
#     def draw(self, canvas):   # 四角形を描く
#         canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = self.color, width = 0)
#《MEMO》RectangeはBallクラスを継承しているため、この定義よりも前にBallクラスが定義されていなければならない。すなわちBallクラスの定義(「class Ball」)よりも後ろで、Rectangeクラスを定義しないとエラーになるLesson7-9-1を参照
# 
# 四角形を描画するには、「create_rectangleメソッド」を使う(P186：表7-2-1参照) 
# ここに示したように、このRectangeクラスでは、処理が異なるeraseメソッドとdrawメソッドだけを作り、他は省略してる
# つまり、moveメソッドはBallクラスに実装されたものと同じものが使われる
# これは図7-9-3のように、「Ballクラスの一部のメソッドが上書きされている」を考えると分かりやすい。クラスでは、「オーバーライト」という言葉が出てきますが、このような「処理は上書き」こそが、オーバーライドの実体です
# 
# 図7-9-3 「オーバーライト」
# 
#     【Rectangeクラス】　　　　　　　    【Ballクラス】
#     《moveメソッド》                  《moveメソッド》
#      そのまま  ⬅️ moveメソッドは書いていなくても、基のBallクラスのものが存在する
#                           継承
#     《eraseメソッド》   ⬅️＝＝＝＝＝    《eraseメソッド》
#      四角形を消す ⬅️ーーーーーーーーーーー ×円を消す×
#                         上書き
#     《drawメソッド》                  《drawメソッド》
#      四角形を描く ⬅️ーーーーーーーーーーー ×円を描く×
#                         上書き
# 
# 
# 《四角形を描画する》
# 作成したRectangeクラスを使って四角形を描画する場合、その処理は、次のように記述する
# b = Rectangle(400, 300, 1, 1, "red")
# 
# def loop():
#   動かす
#   b.move(canvas)
#   もう一回
#   root.after(10, loop)

# 円を扱ってきたBallクラスとの違いは
# b = Rectangle(400, 300, 1, 1, "red")
# の1行だけで、「BallクラスではなくRectangleクラスを使うようにする」ことだけ
# 
# 【継承して三角形の描画クラスを作る】
# 同様にして三角形を描画する、Triangleクラスを作る
# 三角形を描画するには、「create_ploygonメソッド」を使う。create_ploygonメソッドは多角形を描画する機能を持つ。
# ３点の座標を指定することで、三角形を描画できる
# 先の四角形と同様に、eraseメソッドとdrawメソッドをオーバーライトすればよく、次のようにして作れる
# 
# class Triangle(Ball):
#     def erase(self, canvas):    # 三角形を消す
#         canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = "white", width = 0)
# 
#     def draw(self, canvas):     # 三角形を描く
#         canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = self.color, width = 0)
# 
# 【三角形を描画する】
# このTriangleクラスを使って三角形を描画する場合は、次のようになる

# b = Triangle(400, 300, 1, 1, "erd")
# 
# def loop():
#   動かす
#   b.move(canvas)
#   もう一回
#   root.after(10, loop)
# 
# 違いは以下の1桁だけ
# b = Triangle(400, 300, 1, 1, "red")
# 
# 
#【混ぜて描く】
# ここまで「円(Ball)」「四角形(Rectangle)」「三角形(Triangle)」の３つのクラスを使い、それぞれ描画する方法を説明してきた
# これらを混ぜて描画するには、どうすればいいか？
# このプログラムではまず、次のようにして一緒に「円」「四角形」「三角形」を作り。それをリストとして構成する
# balls =[
#     Ball(400, 300, 1, 1, "red"),
#     Rectangle(200, 100, -1, 1, "green"),
#     Triangle(100, 200, 1, -1, "blue")
# ]
# 
# そしてこのballs変数をループ処理することで描画していく
# for b in balls:
#     b.move(canvas)
# 
# ここでのポイントとなるのが、どのクラスもBallクラスから継承していて、すべて「moveメソッド」を持っているという点
# このループで実行しているのは、そのオブジェクトの「moveメソッド」です。それが「円(Ballオブジェクト)」「四角形(Rectangleオブジェクト)」「三角形(Triangleオブジェクト)」のどれかであるかは関係ない
# どのオブジェクトかに関係なく、ただ「moveメソッドさえあれば、同じようにループ処理ができる」のである
# 
# 
# coding:utf-8
import tkinter as tk
class Ball:       #円を描くクラスーーーーーーーーーーーーーーーーーーーーーーーー
    def __init__(self, x, y, dx, dy, color):                         #｜
        self.x = x                                                   #｜
        self.y = y                                                   #｜
        self.dx = dx                                                 #｜
        self.dy = dy                                                 #｜  
        self.color = color                                           #｜
#                                                                    #｜
    def move(self, canvas):                                          #｜
        #いまの円を消す                                           　　  #｜ 
        self.erase(canvas)                                           #｜
        #X座標、Y座標を動かす                                           #｜ 
        self.x = self.x + self.dx                            # オーバーライトしてないから、   
        self.y = self.y + self.dy                            # この２つのメソッドはRectangleでも   
        #次の位置に円を描画する                              　  # Triangleでも同じものが使われる
        self.draw(canvas)                                            #｜
        #端を超えていたら反対向きにする                                   #｜   
        if (self.x >= canvas.winfo_width()):                         #｜
            self.dx = -1                                             #｜ 
        if (self.x <= 0):                                            #｜
            self.dx = 1                                              #｜
        if (self.y >= canvas.winfo_height()):                        #｜
            self.dy = -1                                             #｜ 
        if (self.y <= 0):                                            #｜
            self.dy = 1  #ーーーーーーーーーーーーーーーーーーーーーーーーーーー

    def erase(self, canvas):
        canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = "white", width = 0)

    def draw(self, canvas):
        canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = self.color, width = 0)

class Rectangle(Ball):      # 四角形を描くクラス
    def erase(self, canvas):
        canvas.create_rectangle(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = "white", width = 0)
    def draw(self, canvas):
        canvas.create_rectangle(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill = self.color, width = 0)

class Triangle(Ball):       # 三角形を描くクラス
    def erase(self, canvas):
        canvas.create_polygon(self.x, self.y - 20, self.x + 20, self.y + 20, self.x - 20, self.y + 20, fill = "white", width = 0)
    def draw(self, canvas):
        canvas.create_polygon(self.x, self.y - 20, self.x + 20, self.y + 20, self.x - 20, self.y + 20, fill = self.color, width = 0)

# 円、四角形、三角形をまとめて用意する
balls =[
    Ball(400, 300, 1, 1, "red"),
    Rectangle(200, 100, -1, 1, "green"),
    Triangle(100, 200, 1, -1, "blue")
]
def loop():
    #動かす
    for b in balls:
        b.move(canvas)
    #もう1回
    root.after(10, loop)

# ウィンドウを描く
root = tk.Tk()
root.geometry("800x600")

# Canvasを置く
canvas =tk.Canvas(root, width = 800, height = 600, bg = "#fff")
canvas.place(x = 0, y = 0)

#タイマーをセット
root.after(10, loop)

root.mainloop()


# 【プログラミング】に慣れたら立ち戻る
# クラスとオブジェクトは、難しい概念、身につけて活用するまでには時間がかかる 
# 焦らずじっくり進める
# クラスとオブジェクトはプログラミングの考え方や設計の問題も含むので最初はピンと来ないかも
# 最初のうちはクラスとオブジェクトを使わず、じばらくプロブラミングを進め、改めてクラスとオブジェクトを学ぶと、
# 「こう言う時にクラスとオブジェクトが使えそうだな」という、使い場所が見えてくる
