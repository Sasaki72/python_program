# 【print】
# Pythonにおいて初心者でも上級者でも利用する機会が多いであろうprintです。基本的な使い方から少し踏み込んだ使い方まで見てみましょう。
# 
# 1 基本的な使い方
# 1.1 Python 3系では
# 2 改行しない
# 2.1 Python 3系では
# 3 出力先の変更
# 3.1 Python 3系では
# 4 フォーマット出力
# 
# 
# １ 基本的な使い方
# 『Python 3系では』
# printは引数の値を指定された出力先へ出力します。標準出力であるsys.stdoutがデフォルトの出力先となり、コマンドプロンプトで実行した場合はコマンドプロンプトのコンソールへ出力されます。またprintごとに改行されて出力されます。
# ※Python 3系でprintは関数化されました。
# 
# Python 3系
# 
# print('python')
# print('-')
# print('izm')
# print('com')
# 
# 《実験結果》
# python
# -
# izm
# com
# 
# 
# ２ 改行しない
# 『Python 3系では』
# end引数でprintの最後に付与する値を指定することができます。デフォルトでは改行（ \n ）が付与されるので、下記のように半角スペースなどを指定すると改行されずに出力されます。もちろん半角スペース以外を指定することもできます。
# 
# Python 3系
# 
# print('python', end=' ')
# print('-', end=' ')
# print('izm', end=' ')
# print('com')
# 
# 《実行結果》
# python - izm com
# 
# 
# ３ 出力先の変更
# 『Python 3系では』
# 出力先を一時的にファイルへ変更する場合、Python 3系ではfile引数へ出力先となるファイルオブジェクトを渡します。これは一時的な適用なので、file引数なしでprintを実行すると元の出力先（コンソール）へ出力されます。ファイル操作の詳細はファイル読み書きを参照してください。(https://www.python-izm.com/advanced/file_rw/)
# 
# Python 3系
# 
# f_obj = open('test.txt', 'w')
# 
# print('python-izm.com', file=f_obj)
# 
# 
# ４ フォーマット出力
# フォーマットを指定して出力を行う方法です。文字列や数値などを交えて出力を行ってみましょう。%sは文字列、%dは数値として認識され、混在して出力することができます。フォーマット識別子を含んだメインの文字列の後に%を接続語としてフォーマット出力を行う値を渡します。
# ※基本的な使用法は2系でも3系でも変わりません。
# 
# print('Pythonの学習サイト : %s' % 'python-izm.com')
# print('Pythonの学習サイト : %s-%s.%s' % ('python', 'izm', 'com'))
# 
# test_int = 100 + 100
# test_str = 'python-izm.com'
# print('サイト開設 %d 日目！ %s' % (test_int, test_str))
# 
# 
# 《実験結果》
# Pythonの学習サイト : python-izm.com
# Pythonの学習サイト : python-izm.com
# サイト開設 200 日目！ python-izm.com
# 
# 
# また別の方法としてformatを利用することができます。
# 
# print('Pythonの学習サイト : {}'.format('python-izm.com'))
# print('Pythonの学習サイト : {0}-{1}.{2}'.format('python', 'izm', 'com'))
# 
# test_int = 100 + 100
# test_str = 'python-izm.com'
# print('サイト開設 {1} 日目！ {0}'.format(test_str, test_int))
# 
# 
# 《実行結果》
# Pythonの学習サイト : python-izm.com
# Pythonの学習サイト : python-izm.com
# サイト開設 200 日目！ python-izm.com
# 
# こちらの方がより新しい方法を用いたフォーマット出力です。文字列内の「 {} 」へ指定した値を埋め込みます。「 {} 」内に整数を指定した場合はformatの引数の順番に応じて出力されます。
# 
# 
