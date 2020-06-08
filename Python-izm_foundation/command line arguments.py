# 【コマンドライン引数】
# Pythonのプログラムを起動する際に引数を渡す事ができます。コマンドライン引数と呼ばれるもので、状況に応じて処理を分けたい場合などで有効です。
# 
# 【コマンドライン引数の取得】
# サンプルコードをtest_argv.pyというファイル名で保存し、下記コマンドで実行してみましょう。
# 
# 《コマンド》
# python test_argv.py python izm com
# 
#test_argv.py
# import sys
# 
# args = sys.argv
# 
# print(args)
# print('第１引数：' + args[1])
# print('第２引数：' + args[2])
# print('第３引数：' + args[3])
# 
# 
# 《実行結果》
# ['test_argv.py', 'python', 'izm', 'com']
# 第１引数：python
# 第２引数：izm
# 第３引数：com
# 
# 3行目のsys.argvに起動時に設定した引数が格納されます。リストで値が返されますが、最初の要素には実行ファイル名が入りますので注意しましょう。
# 
# 