# 【for文】
# プログラミングにおいて繰り返し処理を行う場面は多々あります。そこでfor文の登場となります。
# 
# 【for文の基礎】
# 下記サンプルではリストの要素を出力しています。まずforを記述し、次にvalueという変数名を指定しています。続いてinの記述をはさみ、最後に繰り返し処理を行う対象のオブジェクトを指定します。また変数valueには繰り返し対象のオブジェクトの要素が１つずつ格納されます。
# 
# for_sample = []
# for_sample.append("python")
# for_sample.append("-")
# for_sample.append("izm")
# for_sample.append("for")
# for_sample.append("statement")
# for_sample.append("sample")
# 
# for value in for_sample:
#     print(value)
# 
# 
# 《実行結果》
# python
# -
# izm
# for
# statement
# sample
# 
# 
# 反復処理をサポートしているオブジェクトであれば何でも構いません。たとえば文字列などもループ処理の対象となります。
# 
# for value in 'ABCDEF':
#     print(value)
# 
# 
# 《実行結果》
# A
# B
# C
# D
# E
# F
# 
# 
# また以下のように複数の値へ分割して取得することができます。
# 
# test_list_1 = [['https', 'www'], ['python-izm', 'com']]
# 
# for value in test_list_1:
#     print(value)
# 
# for value_1, value_2 in test_list_1:
#     print(value_1, value_2)
# 
# 
# 《実行結果》
# ['https', 'www']
# ['python-izm', 'com']
# https www
# python-izm com
# 
# 
