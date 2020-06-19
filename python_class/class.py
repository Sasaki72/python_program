クラスを学ぼう
今回は「MenuItem」を参考に考える

それぞれのメニューには「値段」と「値段」という情報を持っている

【「もの」を生成する仕組み】
プログラミングでメニューという「もの」を生成するには、まずその「設計図」を用意する必要があります。
設計図のことを『クラス』、「もの」のことを『インスタンス』と呼びますので、覚えておきましょう。

MenuItem(設計図(クラス))　、　メニュー表(インスタンス)


【インスタンスを生成するステップ】
インスタンスは、流れに沿って生成していきます。
まずは、step1の「クラスを用意する」から順番に進めていきましょう。

①クラス(設計図(クラス))を用意する
②クラスからインスタンスを生成する　　
MenuItem ➡️　「もの(MenuItem)」(空のインスタンス)
③インスタンスに情報を追加する　　　 
「もの(MenuItem)」(空のインスタンス) + 名前：サンドイッチ、値段：500円 (情報) = 情報が追加されたインスタンス


【クラスの定義】
まずは左の図のクラス（設計図）を用意していきます。
クラスは「class クラス名:」とすることで定義できます。
また、クラス名の単語の最初は「MenuItem」のように大文字で始めるようにしましょう。

class MenuItem:  行末にコロンを入れる！
　　　 ↑   ↑
クラス名の単語の最初は『大文字』で始める


【クラスの中身】
クラスの中身（設計図の内容）は「class MenuItem:」より後の行で、『インデント』をして書いていきます。
今回はまだ処理を追加する必要がないので、右の図のように「pass」と書きましょう（これは何も処理がないことを表しています）。

class MenuItem:
----# 処理
インデントをそろえる(半角スペース４つ分)

class MenuItem:
    pass ← 「何も処理がない」ことを表す


【クラスからインスタンスを生成する】
【インスタンスの生成】
「クラス名()」とそのクラスを呼び出すことで、クラス（設計図）を用いて新しくインスタンスを生成することができます。
また、「変数名 = クラス名()」とすることで、生成したインスタンスを変数に代入することができます。

『インスタンスの生成』
class MenuItem:
    pass
#　        ⬅️ MenuItem()を変数menu_item1に代入
menu_item1 = MenuItem() # MenuItemクラスからインスタンスを生成

『インスタンスの生成のイメージ図』
MenuItemクラス(設計図)  ➡️  空のインスタンス(もの)
#                    生成！


【インスタンスに情報を追加しよう】
【インスタンスと情報】

それぞれのインスタンス（メニュー）には、自由に様々な情報を追加することができます。
name（名前）が「サンドイッチ」、price（値段）が「500」という情報を持っている。


【インスタンス変数】
『menu_item1.name = 'サンドイッチ'』とすることで、menu_item1に「name」が「サンドイッチ」であるという情報を追加することができます。
この時、「name」のことを『インスタンス変数』と呼ぶ

class MenuItem:
    pass

#          ⬅️ 値を代入
menu_item1 = MenuItem()
menu_item.name = 'サンドイッチ'
#          ⬇️
#      インスタンス変数


【インスタンス変数を用いる】
また、『インスタンス.インスタンス変数名』とすることで、そのインスタンス変数の値を用いることができます。

class MenuItem:
    pass
menu_item = MenuItem()
menu_item1.name = 'サンドイッチ'
print(menu_item1.name)
#           ⬇️
#     インスタンス変数の値を用いる

《実行結果》
サンドイッチ



【インスタンスごとに情報を持つことを確認しよう】
#                               生成！
#                          ｜ーーーーーー サンドイッチ ¥ 500 (税込)          
#                          ｜ 　 生成！        
#                          ｜ーーーーーー チョコケーキ ¥ 400 (税込)          
# MenuItem(設計図(クラス)) ーー        
#                          ｜ーーーーーー コーヒー ¥ 300 (税込)            
#                          ｜ 　 生成！       
#                          ｜ーーーーーー オレンジジュース ¥ 200 (税込)          
#                               生成！

class MenuItem:
    pass

menu_item1 = MenuItem()

menu_item1.name = 'サンドイッチ'
print(menu_item1.name)

menu_item1.price = 500
print(menu_item1.price)

# MenuItemクラスのインスタンスを生成してください
menu_item2 = MenuItem()
# menu_item2のnameに「チョコケーキ」を代入してください
menu_item2.name = 'チョコケーキ'
# menu_item2のnameを出力してください
print(menu_item2.name)
# menu_item2のpriceに「400」を代入してください
menu_item2.price = 400
# menu_item2のpriceを出力してください
print(menu_item2.price)

と他の商品も生成方法は同じく続く！



【料理注文システムを作っていこう】
【クラスの中に処理を追加する】
クラスの中では関数を定義することができます。クラスの中で定義した関数のことを『メソッド』と呼びます。
メソッドの定義の方法は通常の関数と同じですが、『第1引数にselfを追加する』必要があることに注意しましょう。

class MenuItem:
 |ーーーーーーーーーーーーーー|
 |   def hello(self):ーー |ー➡️ 必ず第１引数に『self』を追加する 
 |     print('こんにちは') |
 |ーーーーーーーーーーーーーー|
 クラスの中でメソッド(関数)を定義



【クラスの中で定義したメソッドを呼び出す】
クラスの中で定義したメソッドは、インスタンスに対して使うように呼び出します。
具体的には、『インスタンス.メソッド名()』とすることで、そのメソッドを呼び出すことができる。

class MenuItem:
    def hello(self):
        print('こんにちは！')

menu_item1 = MenuItem()
menu_item1.hello()　# クラスの中で定義したメソッドを呼び出す

《実行結果》
こんにちは！


class MenuItem:
    # infoメソッドを定義してください
    def info(self):
        print('メニューの名前と値段が表示されます')

menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500
menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400
menu_item2.info()

《実行結果》
メニューの名前と値段が表示されます
メニューの名前と値段が表示されます


【インスタンスメソッド】
さっき作ったクラスの中で定義しインスタンスに対して呼び出すメソッドのことを
『インスタンスメソッド』と呼ぶ。

【メニューの内容を出力する機能】
インスタンスメソッドでは、引数に指定した『self』に、呼び出したインスタンス自身が代入されている

class MenuItem:
    def info(self):
#          　　⬇️
#　呼び出したインスタンスが代入されている
      print('メニューの情報が表示されます')
・
・
・
menu_item1.info()



【インスタンスメソッドのselfの正体】
インスタンスメソッドの第1引数に指定した『self』には、そのメソッドを呼び出したインスタンス自身が代入されている。
そのため、メソッド内で『self.name』とすることで、そのメソッドを呼び出している「menu_item1」の「name」の値を取得することができる。

class MenuItem:
#                       menu_item1 が代入される
    def info(self): # ⬅️ーーーーーーー
#            ----                 |
      print(self.name)           #|
#           ---------             |
menu_item1 = MenuItem()          #|
menu_item1.name = 'サンドイッチ'   #|
menu_item1.info()                #|
#ーーーーーーーーー                  |
#       ｜ーーーーーーーーーーーーーーー

《実行結果》
サンドイッチ
#menu_item1.name の値


【型変換の復習】
「name」と「price」の値を用いて、「サンドイッチ: ¥500」と出力する。
この時、「price」の値は数値型であるため、文字列と結合するためには文字列型に変換する必要がある。
数値を文字列に変換する方法を確認。

age = 21
print(str(age) + '歳です')
#     --------
#     文字列に変換

《実行結果》
21歳です

class MenuItem:
    def info(self):
        # 「○○: ¥□□」となるように出力してください
        print(self.name + ': ¥' + str(self.price))

menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500
menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400
menu_item2.info()

《実効結果》
サンドイッチ：¥ 500
チョコケーキ：¥ 400


【インスタンスメソッドの活用】
インスタンスメソッドは通常の関数と同様に『戻り値』を返すようにすることもできる
『return』を使う
今回はinfoメソッドが戻り値を返すようにしてみる

class MenuItem:
    def info(self):
        # print()の中身を戻り値として返してください
        return self.name + ': ¥' + str(self.price)

menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500
print(menu_item1.info())


menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400
print(menu_item2.info())

《実効結果》
サンドイッチ：¥ 500
チョコケーキ：¥ 400



【クラスとインスタンスの復習】
クラスは設計図のようなもので、その設計図からつくる実際の「もの」にあたるものがインスタンスです。
インスタンスは情報として「インスタンス変数」を、処理として「インスタンスメソッド」を持っています。

#                               生成！
#                          ｜ーーーーーー サンドイッチ ¥ 500 (税込)          
#                          ｜ 　 生成！        
#                          ｜ーーーーーー チョコケーキ ¥ 400 (税込)          
# MenuItem(設計図(クラス)) ーー        
#                          ｜ーーーーーー コーヒー ¥ 300 (税込)            
#                          ｜ 　 生成！       
#                          ｜ーーーーーー オレンジジュース ¥ 200 (税込)          
#                               生成！

# サンドイッチ ¥ 500 (税込)
# 「情報」
#・名前：サンドイッチ
#・値段：¥ 500
# 「メソッド」
#・infoメソッド



【合計金額を求めるメソッド】
メニューの合計金額を求めるメソッドをつくってみましょう。
インスタンスメソッドに引数を渡す場合、メソッドの定義側では「self」の分だけ引数の順番がずれることに注意

class MenuItem:
  ・
  ・                             #｜ーーーーーーー
  ・                             #⬇️        　 |
      def get_total_price(self, count): #     |
  ・                        #   ------    　　 |      
  ・                       #「4」が代入される    |              
  ・                                      　　#|
menu_item1.get_total_price(4)        　　　   #|
#                         ---                 |
#                          |ーーーーーーーーーーー


class MenuItem:
    def info(self):
        return self.name + ': ¥' + str(self.price)

    # get_total_priceメソッドを定義してください
    def get_total_price(self, count):
        total_price = self.price * count
        return total_price

menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500
print(menu_item1.info())

result = menu_item1.get_total_price(4)

print('合計は' + str(result) + '円です')



【特殊なインスタンスメソッド】
『__init__』 という名前のインスタンスメソッドは、そのインスタンスが生成された時に必ず呼び出される

【__init__メソッド】
インスタンスを生成した直後に処理を実行することができる、__init__メソッド
__init__メソッドは、「クラス名()」でインスタンスを生成した直後に『自動で』呼び出される。

「MenuItem()」が実行される
          ⬇️
MenuItemクラスのインスタンスが生成される
          ⬇️　__init__　メソッドがあれば、、、
『生成されたインスタンスに対して __init__ メソッドが自動で呼び出される！』

【__init__メソッドを用いる】
__init__メソッドは、他のインスタンスメソッドと同じように定義することができます。
以下の例では、「menu_item1 = MenuItem()」でMenuItemクラスのインスタンスが生成された直後に__init__メソッドが呼び出され、その中の処理が実行されます。
