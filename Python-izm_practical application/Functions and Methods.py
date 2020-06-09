# 【関数・メソッド】
# まずはプログラミングを行う上で、初心者・上級者問わず重要な関数の作成です。
# 
# 1 関数の基礎
# 2 引数の基礎
# 3 引数の初期値
# 4 関数とメソッド
# 
# 
# １ 関数の基礎
# Pythonの関数の最も簡単な例は下記の通りとなります。
# 
# def test_func():
#     print('call test_func')
# 
# test_func()
# 
# 
# 《実行結果》
# call test_func
# 
# defで関数を宣言し、インデントによってブロック化された配下の処理を実行します。上記の例ではtest_funcが関数の名前で「（）」（カッコ）の中に引数を指定します。関数の最後には必ず「 : 」（コロン）を付けましょう。
# 
# 
# ２ 引数の基礎
# 先程の関数には引数がありませんでした。今回は引数を設定してみましょう。第一引数と第二引数に数値を、第三引数に四則演算の識別子を指定し、二つの数値を計算させます。
# 
# def test_func(num_1, num_2, oprn):
# 
#     if oprn == 1:
#         print('足し算開始')
#         print(num_1 + num_2)
# 
#     elif oprn == 2:
#         print('引き算開始')
#         print(num_1 - num_2)
# 
#     elif oprn == 3:
#         print('掛け算開始')
#         print(num_1 * num_2)
# 
#     elif oprn == 4:
#         print('割り算開始')
#         print(num_1 / num_2)
# 
#     else:
#         print('不明なオペレーション指定です')
# 
# 
# test_func(100, 10, 3)
# 
# 
# 《実行結果》
# 掛け算開始
# 1000
# 
# 複数の引数を設定する場合は「 , 」（カンマ）で区切ります。上記の例では100と10の掛け算を行うというものでした。
# 
# 
# ３ 引数の初期値
# 引数は初期値を指定すると、関数を呼び出す際に省略する事が可能です。今回は第三引数の初期値を1と設定し、第三引数の指定無しで呼び出された場合は足し算をするようにしました。
# 
# def test_func(num_1, num_2, oprn=1):
# 
#     if oprn == 1:
#         print('足し算開始')
#         print(num_1 + num_2)
# 
#     elif oprn == 2:
#         print('引き算開始')
#         print(num_1 - num_2)
# 
#     elif oprn == 3:
#         print('掛け算開始')
#         print(num_1 * num_2)
# 
#     elif oprn == 4:
#         print('割り算開始')
#         print(num_1 / num_2)
# 
#     else:
#         print('不明なオペレーション指定です')
# 
# test_func(100, 10)
# 
# 
# 《実行結果》
# 足し算開始
# 110
# 
# 
# もちろん第三引数の指定を行えば、その通りの処理をしてくれます。
# 
# def test_func(num_1, num_2, oprn=1):
# 
#     if oprn == 1:
#         print('足し算開始')
#         print(num_1 + num_2)
# 
#     elif oprn == 2:
#         print('引き算開始')
#         print(num_1 - num_2)
# 
#     elif oprn == 3:
#         print('掛け算開始')
#         print(num_1 * num_2)
# 
#     elif oprn == 4:
#         print('割り算開始')
#         print(num_1 / num_2)
# 
#     else:
#         print('不明なオペレーション指定です')
# 
# test_func(100, 10, 4)
# 
# 
# 《実験結果》
# 割り算開始
# 10
# 
# 
# ４ 関数とメソッド
# Pythonでは関数（function）とメソッド（method）があります。特に意識する必要はありませんが、モジュール内にdefで定義されているものが関数、クラス内にdefで定義されているものがメソッドになります（正確にはクラスがインスタンス化されてからメソッドになります）。
# 
# 関数
# def test_func():
#     print('call test_func')
  
  
# class TestClass:
#     # メソッド
#     def test_method():
#         print('call test_method')

# print('------------------------')
# print(test_func)
# print(TestClass.test_method)

# print('------------------------')
# print(type(test_func))
# print(type(TestClass.test_method))

# print('------------------------')
# t = TestClass()
# print(test_func)
# print(t.test_method)
# 
# 
# 《実験結果》
# ------------------------
# <function test_func at 0x0000022A9E2E3E18>
# <function TestClass.test_method at 0x0000022A9E82BAE8>
# ------------------------
# <class 'function'>
# <class 'function'>
# ------------------------
# <function test_func at 0x0000022A9E2E3E18>
# <bound method TestClass.test_method of <__main__.TestClass object at 0x0000022A9E82A0F0>>
# 
# 
