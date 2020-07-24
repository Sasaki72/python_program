# 【スライス】
# Pythonではスライスと呼ばれる表記方法で、シーケンスから範囲を指定して要素を取得することができます。シーケンスはタプルやリスト、文字列などを示す型で、ディクショナリやセットは含まれません。
# 
# 1 スライスの基本
# 2 要素の取得
# 3 要素の代入
# 
# 
# １ スライスの基本
# スライスは以下のような記述で開始位置、終了位置、ステップ幅を指定します。またこれらの指定は省略可能で、シーケンスの要素数に応じて適切に動作します。
# 
# 《書式》
# sequence[<開始位置>:<終了位置>:<ステップ幅>]
# 
# たとえば次のような記述でシーケンス（ここではリスト）の要素をすべて取得することができます。
# 
# test_list = ['https', 'www', 'python', 'izm', 'com']
# 
# print(test_list[:])
# print(test_list[::])
# 
# 
# 《実行結果》
# ['https', 'www', 'python', 'izm', 'com']
# ['https', 'www', 'python', 'izm', 'com']
# 
# 
# ２ 要素の取得
# 開始位置を省略し、終了位置を指定することで先頭から指定位置までの要素を取得することができます。
# 
# test_list = ['https', 'www', 'python', 'izm', 'com']
# 
# print(test_list[:4])
# 
# 
# 《実行結果》
# ['https', 'www', 'python', 'izm']
# 
# 開始位置を指定し、終了位置を省略することで指定位置から末尾までの要素を取得することができます。
# 
# test_list = ['https', 'www', 'python', 'izm', 'com']
# 
# print(test_list[2:])
# 
# 
# 《実行結果》
# ['python', 'izm', 'com']
# 
# ステップ幅を指定することで、指定数ごとの要素を取得することができます。
# 
# test_list = ['https', 'www', 'python', 'izm', 'com']
# 
# print(test_list[::2])
# 
# 
# 《実行結果》
# ['https', 'python', 'com']
# 
# 開始位置と終了位置を指定することで範囲内の要素を取得することができます。
# 
# test_list = ['https', 'www', 'python', 'izm', 'com']
# 
# print(test_list[3:5])
# 
# 
# 《実行結果》
# ['izm', 'com']
# 
# 負の数を指定することで末尾から取得することができます。
# 
# test_list = ['https', 'www', 'python', 'izm', 'com']
# 
# print(test_list[-1:])   # 末尾から全ての要素
# print(test_list[:-1])   # 末尾まで全ての要素
# print(test_list[::-1])  # 末尾から全ての逆順要素
# 
# 
# 《実行結果》
# ['com']
# ['https', 'www', 'python', 'izm']
# ['com', 'izm', 'python', 'www', 'https']
# 
# 範囲指定が要素数を超過している場合は、要素数に応じてカットされます。
# 
# test_list = ['https', 'www', 'python', 'izm', 'com']
# 
# print(test_list[:999])
# 
# 
# 《実行結果》
# ['https', 'www', 'python', 'izm', 'com']
# 
# 
# ２ 要素の代入
# 要素の代入における範囲指定方法も要素の取得と変わりません。
# 
# test_list = ['https', 'www', 'python', 'izm', 'com']
# 
# test_list[1:3] = ('WWW', 'PYTHON')
# 
# print(test_list)
# 
# 
# 《実行結果》
# ['https', 'WWW', 'PYTHON', 'izm', 'com']
# 
# 
