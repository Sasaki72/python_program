# 【例外処理】
# アプリケーションを作成する上で例外処理は欠かせません。処理方法や例外送出時の情報取得方法などは是非ともおさえておきましょう。
# 
# 1 try, except, finally
# 2 raise
# 3 エラー内容（スタックトレース）の取得
# 
# 
# １ try, except, finally
# 簡単な使用例です。足し算を行うexception_test関数を用意し、それを呼び出しています。
# ※関数(https://www.python-izm.com/advanced/function_method/)の詳細は応用編(https://www.python-izm.com/advanced/)で解説します。
# 
# def exception_test(value_1, value_2):
# 
#     print('＝＝＝＝計算開始＝＝＝＝')
# 
#     result = 0
# 
#     try:
#         result = value_1 + value_2
#     except:
#         print('計算出来ませんでした！')
#     finally:
#         print('計算終了')
# 
#     return result
# 
# 
# print(exception_test(100, 200))
# print(exception_test(100, '200'))
# 
# 
# 《実行結果》
# ＝＝＝＝計算開始＝＝＝＝
# 計算終了
# 300
# ＝＝＝＝計算開始＝＝＝＝
# 計算出来ませんでした！
# 計算終了
# 0
# 
# 関数が呼び出された後try配下の処理を行っています。その処理中に例外（エラー）が発生しなければexcept配下の処理は実行されません。例外が発生した時には必ず実行されるので、発生時の制御を細かく設定することもできます。
# 一回目の呼び出しの時の引数は両者ともに数値なので、except配下の処理は実行されていません。二回目の呼び出しの際の引数は片方が文字列ですので、足し算を実行することができずexcept配下の処理が実行される流れです。最後のfinallyは例外の有無に関わらず必ず実行されるので、本来の使い方としてはオープンしたオブジェクトをクローズする処理などを記述すると良いでしょう。
# 
# 
# ２ raise
# 規模が大きめアプリケーションを作成している場合、他のプログラマが作成した便利な関数を利用する機会は多々あると思います。その関数内で処理が収束してもよいのなら必要はありませんが、場合によっては呼び出し元にエラーを上げ、そのエラー処理を任せた方が良いケースもあります。それを実現するのがraiseです。
# 
# def exception_test(value_1, value_2):
# 
#     print('＝＝＝＝計算開始＝＝＝＝')
# 
#     result = 0
# 
#     try:
#         result = value_1 + value_2
#     except:
#         print('計算出来ませんでした！')
#         raise
#     finally:
#         print('計算終了')
# 
#     return result
# 
# 
# try:
#     print(exception_test(100, 100))
#     print(exception_test(200, 200))
#     print(exception_test(300, '300'))
# except:
#     print('エラーを受け取りました')
# 
# 
# 《実行結果》
# ＝＝＝＝計算開始＝＝＝＝
# 計算終了
# 200
# ＝＝＝＝計算開始＝＝＝＝
# 計算終了
# 400
# ＝＝＝＝計算開始＝＝＝＝
# 計算出来ませんでした！
# 計算終了
# エラーを受け取りました
# 
# 上記のサンプルはtryの中でtryを使用しているようなイメージです。exception_testで例外（エラー）発生時にraiseするように記述しているので、それが呼び出し元のtryの方へ伝播します。raiseをコメントアウトすると23行目のexcept配下の処理が実行されないので、試してみてください。
# 
# 
# ３ エラー内容（スタックトレース）の取得
# 処理を実行中にエラーが発生すると、例外内容（スタックトレース）が標準出力へ出力されます。それをプログラム側で取得することも可能です。
# 
# import sys
# import traceback

# def exception_test(value_1, value_2):

#     print('＝＝＝＝計算開始＝＝＝＝')

#     result = 0

#     try:
#         result = value_1 + value_2
#     except:
#         print('計算出来ませんでした！')
#         raise
#     finally:
#         print('計算終了')

#     return result


# try:
#     print(exception_test(100, '200'))
# except:
#     print('---------------------------------------')
#     print(traceback.format_exc(sys.exc_info()[2]))
#     print('---------------------------------------')
# 
# 
# 《実行結果》
# ＝＝＝＝計算開始＝＝＝＝
# 計算出来ませんでした！
# 計算終了
# ---------------------------------------
# Traceback (most recent call last):
#   File "test.py", line 27, in 
#     print exception_test(100,"200")
#   File "test.py", line 14, in exception_test
#     result = value_1 + value_2
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ---------------------------------------
# 
# 
