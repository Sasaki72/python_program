# 【タプル（tuple）】
# タプルはプログラミングにおける機能としては一般的ですが、他の言語ではあまり聞かないネーミングです。簡単に言うと、複数の要素から構成されそれを一つのモノとして扱える機能です。後の項で解説するリストとの違いは、作成した後に要素の追加や削除が出来るか出来ないかです。タプルの場合は作成した後の変更は不可、リストの場合は可と覚えておきましょう。
# 
# ・タプルとは？
# 先に述べたとおり、タプルの特徴は作成した後の変更が不可能という点です。複数の値を返す関数の戻り値などをタプルにすると良いでしょう。使い方は下記の通りです。
# 
# import datetime
# 
# 
# def get_today():
# 
#     today = datetime.datetime.today()
#     value = (today.year, today.month, today.day)
# 
#     return value
# 
# 
# test_tuple = get_today()
# 
# print(test_tuple)
# print(test_tuple[0])
# print(test_tuple[1])
# print(test_tuple[2])
# 
# 
# 《実行結果》
# (2010, 5, 8)
# 2010
# 5
# 8
# 
# ※プログラムの実行時間によって結果は異なります。
# 
# 
# 7行目で要素を3つ「 () 」（カッコ）を使用して囲んでいます。これでその3要素を保持しているタプルとして作成することができます。
# 
# import datetime
# 
# 
# def get_today():
# 
#     today = datetime.datetime.today()
#     value = (today.year, today.month, today.day)
# 
#     return value
# 
# 
# test_tuple = get_today()
# 
# print(test_tuple)
# print(test_tuple[0])
# print(test_tuple[1])
# print(test_tuple[2])
# 
# またタプルやリストなどは（文字列もそうです）、シーケンス型と呼ばれ「 [] 」を用いたインデックス値で各要素にアクセスできるようになっています（インデックス値は0から始まります）。
# 
# 