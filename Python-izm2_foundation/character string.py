# 【文字列】
# 入門編では実行方法と基本構文を学びました。基礎編ではまず文字列について解説します。

# 1 文字列の基礎
# 2 文字列の連結
# 3 文字列へ変換
# 4 文字列の置換
# 5 文字列の分割
# 6 文字列の桁揃え
# 7 文字列の検索
# 8 大文字・小文字変換
# 9 先頭・末尾の削除


#【文字列の基礎】 
#Pythonの文字列は 「 ‘ 」（シングルクォーテーション）と「 ” 」（ダブルクォーテーション）の両方で表現出来ます。
# print('python-izm')
# print("python-izm")
#
# 《実行結果》
# python-izm
# python-izm


# クォート記号３つで複数行に分けて書く事も出来ます。
# test_str = """
# test_1
# test_2
# """
# print(test_str)
#
# 《実行結果》
# test_1
# test_2


# 【文字列の連結】
# 文字列の連結は「 + 」を使います。
# test_str = 'python'
# test_str = test_str + '-'
# test_str = test_str + 'izm'
# print(test_str)
#
# print('python-izm')
#
# 《実行結果》
# python-izm


# 「 += 」を用いることで特定の文字列への追加も可能です。
# test_str = '012'
# test_str += '345'
# test_str += '678'
# test_str += '9'
#
# print(test_str)
#
# 《実行結果》
# 0123456789


# 「 * 」を用いることで指定回数分繰り返すこともできます。
# test_str = '012' * 3
#
# print(test_str)
#
# 《実行結果》
# 012012012


# 【文字列へ変換】
# 文字列への変換はstrを使用します。
#
# test_integer = 100
#
# print(str(test_integer) + '円')
#
# 《実行結果》
# 100円


# 【文字列の置換】
# 文字列の置換は replace(替える) を使用します。
# 
# test_str = 'python-izm'
#
# print(test_str.replace('izm', 'ism'))
# 
# 《実行結果》
# python-ism
# 
# 
# 【文字列の分割】
# 文字列の分割はsplitを使用します。これはリスト（list）という形で戻り値を返しますが、リストについては入門編の後の項で説明します。
# ※戻り値とは関数などが返す結果のことで、様々な形で返されます。戻り値を返さないものもあります。
# 
# test_str = 'python-izm'
#  
# print(test_str.split('-'))
# 
# 《実行結果》
# ['python', 'izm']
# 
# 
# 【文字列の桁揃え】
# 文字列の左に値を埋める場合はrjustを使います。第一引数が埋めた後の桁数、第二引数が埋め込む文字列です。ゼロ以外の文字列も埋め込み可能です。
# 
# test_str = '1234'
# 
# print(test_str.rjust(10, '0'))
# print(test_str.rjust(10, '!'))
# 
# 《実行結果》
# 0000001234
# !!!!!!1234
# 
# 特定の文字列を指定せずゼロで桁埋めする場合はzfillを使います。
# 
# test_str = '1234'
# 
# print(test_str.zfill(10))
# print(test_str.zfill(3))
# 
# 《実行結果》
# 0000001234
# 1234
# 
# 
# 【文字列の検索】
# 文字列の検索方法は様々です。まずは文字列の先頭が任意の文字であるかを調べます。戻り値はTrueもしくはFalseです。
# ※TrueやFalseは真偽値を表します。簡単にいうと〇か×かということで〇はTrue、×はFalseになります。
# 
# test_str = 'python-izm'
# 
# print(test_str.startswith('python'))
# print(test_str.startswith('izm'))
# 
# 《実行結果》
# True
# False
# 
# 次は文字列中に任意の文字が含まれているかを調べます。 戻り値は同じくTrueかFalseです。
# 
# test_str = 'python-izm'
# 
# print('z' in test_str)
# print('s' in test_str)
# 
# 《実行結果》
# True
# False
# 
# 
# 【大文字・小文字変換】
# 指定の文字列を大文字・小文字へ変換するにはupperもしくはlowerを使います。
# 
# test_str = 'Python-Izm.Com'
# 
# print(test_str.upper())
# print(test_str.lower())
# 
# 《実行結果》
# PYTHON-IZM.COM
# python-izm.com
# 
# 
# 【先頭・末尾の削除】
# 文字列の先頭・末尾を削除した値を取得します。それぞれlstripは先頭（左から）、rstripは末尾（右から）の削除となり、引数なしでは空白を除去します。
# ※末尾の空白の削除は出力結果ではわかりづらいので、スラッシュを付加しています。
#
# print('----------------------------------')
# 
# test_str = '     python-izm.com'
# print(test_str)
# 
# test_str = test_str.lstrip()
# print(test_str)
#     
# test_str = test_str.lstrip('python')
# print(test_str)
# 
# 
# print('----------------------------------')
# 
# test_str = 'python-izm.com     '
# print(test_str + '/')
# 
# test_str = test_str.rstrip()
# print(test_str + '/')
#     
# test_str = test_str.rstrip("com")
# print(test_str)
#
#《実行結果》
# ----------------------------------
#      python-izm.com
# python-izm.com
# -izm.com
# ----------------------------------
# python-izm.com     /
# python-izm.com/
# python-izm.
# 
# 
# 