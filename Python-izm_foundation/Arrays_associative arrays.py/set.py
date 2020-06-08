# 【セット・集合（set）】
# 任意の数の要素を持つことができる配列です。作成した後でも要素の追加や削除を行うことができますが、1つのセットの中で重複した要素を持つことができません。
# 
# ディクショナリの次はセットです。集合とも呼ばれます。リストと同じように要素を追加、削除することができますが、重複した要素を持つことができないのが特徴です。また本項では更新することができないsetであるfrozensetも取り扱います。
# ※セットのもう少し踏み込んだ使い方はセットの比較・作成・更新で触れています。
# 
# 1 セットの基本
# 2 要素の追加
# 3 要素の削除
# 4 frozenset
# 
# 
# １ セットの基本
# test_set_1 = {'python', '-', 'izm', '.', 'com'}
# print(test_set_1)
#  
# for i in test_set_1:
#     print(i)
# 
# 
# 《実行結果》
# {'izm', '.', '-', 'python', 'com'}
# --------------------------------
# python
# -
# com
# izm
# .
# 
# 要素がない空のセットを作成する時はsetを用います。
# 
# # これはディクショナリ
# test_dict = {}
# 
# # これはセット
# test_set = {'python'}
# 
# # 空のセットは「set」を使う
# empty_set = set()
# 
# 前述の通り、重複した値を持つことはできません。たとえば次の例では‘python’と‘izm’が重複していますが、そのセットの出力結果には1つだけしか存在していません。
# 
# test_set_1 = {'python', '-', 'izm', '.', 'com', 'python', 'izm'}
# print(test_set_1)
# 
# print('--------------------------------')
# 
# for i in test_set_1:
#     print(i)
# 
# 
# 《実行結果》
# {'izm', '.', '-', 'python', 'com'}
# --------------------------------
# python
# -
# com
# izm
# .
# 
# 
# ２ 要素の追加
# 単一の要素を追加する場合はadd、他のセットやリスト、タプルなどから要素を追加する場合はupdateを使用します。
# 
# test_set_1 = set()
# 
# test_set_1.add('python')
# test_set_1.update({'-', 'izm', '.', 'com'})
# 
# print(test_set_1)
# 
# 
# 《実行結果》
# {'izm', '.', '-', 'python', 'com'}
# 
# 
# ３ 要素の削除
# セットから要素を削除する場合はremove、discardを使用します。removeは指定した要素が存在していない場合はエラーとなります。
# 
# test_set_1 = {'python', '-', 'izm', '.', 'com'}
# 
# test_set_1.remove('-')
# test_set_1.discard('.')
# 
# print(test_set_1)
# 
# 
# 《実行結果》
# {'izm', 'python', 'com'}
# 
# 
# ４ frozenset
# frozensetはfrozenset関数を使用して通常のsetのように作成できます。ただし次の例にあるようなremoveやdiscard、さらにaddやupdateなどを行おうとするとAttributeErrorが発生します。
# 
# test_set_1 = frozenset({'python', '-', 'izm', '.', 'com'})
# 
# # test_set_1.remove('-')
# # test_set_1.discard('.')
# 
# print(test_set_1)
# 
# 
# 《実行結果》
# frozenset({'izm', '.', '-', 'python', 'com'})
# 
# 
# 
# 【セットのもう少し踏み込んだ使い方・セットの比較・作成・更新】
# Pythonのセットは、セット同士の比較や反復可能オブジェクトとの比較をさまざまな条件で行うことができます。またその結果をもって新たなセットを作成したり、既存のセットを更新することも可能で、一部の関数は演算子を用いても同じ結果を得ることができます。
# 
# 1 セットを比較
# 2 セットを比較して作成
# 3 セットを比較して更新
# 
# 
# １ セットを比較
# isdisjointはセットと引数の反復可能オブジェクトとの間で共通の要素を持たないときにTrueとなります。issubsetはセットの全要素が引数の反復可能オブジェクトに含まれているときにTrueとなります。issupersetは引数の反復可能オブジェクトの全要素がセットに含まれているときにTrueとなります。
# 
# test_set_1 = set({'python', '-', 'izm', '.', 'com'})
# 
# print(test_set_1.isdisjoint({'python', 'izm'}))
# print(test_set_1.isdisjoint({1, 2, 3}))
# 
# print('----------------------------')
# 
# print(test_set_1.issubset({'python', 'izm'}))
# print(test_set_1.issubset({'www', 'python', '-', 'izm', '.', 'com'}))
# 
# print('----------------------------')
# 
# print(test_set_1.issuperset({'python', 'izm'}))
# print(test_set_1.issuperset({'www', 'python', '-', 'izm', '.', 'com'}))
# 
# 
# 《実行結果》
# False
# True
# ----------------------------
# False
# True
# ----------------------------
# True
# False
# 
# 
# issubsetとissupersetは演算子を用いることでも同様の結果を得ることができます。
# 
# # test_set_1 = {'python', '-', 'izm', '.', 'com'}
# 
# # issubsetと同じ
# print(test_set_1 <= {'python', 'izm'})
# print(test_set_1 <= {'www', 'python', '-', 'izm', '.', 'com'})
# 
# print('----------------------------')
# 
# # issupersetと同じ
# print(test_set_1 >= {'python', 'izm'})
# print(test_set_1 >= {'www', 'python', '-', 'izm', '.', 'com'})
# 
# 
# 《実行結果》
# False
# True
# ----------------------------
# True
# False
# 
# 
# ２ セットを比較して作成
# unionはセットと引数の反復可能オブジェクトのすべての要素を持つセットを作成します。intersectionはセットと引数の反復可能オブジェクトとの間における共通の要素を新たなセットとして作成します。differenceはセットに含まれていて引数の反復可能オブジェクトには含まれない要素を持つ新たなセットを作成します。symmetric_differenceはセットと引数の反復可能オブジェクトのどちらかだけに含まれる要素を持つ新たなセットを作成します。
# 
# test_set_1 = {'python', 'izm', 'com'}
# 
# print(test_set_1.union({'python', 'www'}))
# print(test_set_1.intersection({'python', 'www'}))
# print(test_set_1.difference({'python', 'www'}))
# print(test_set_1.symmetric_difference({'python', 'www'}))
# 
# 
# 《実行結果》
# {'com', 'www', 'izm', 'python'}
# {'python'}
# {'com', 'izm'}
# {'com', 'www', 'izm'}
# 
# また演算子を用いることでも同様の結果を得ることができます。
# 
# test_set_1 = {'python', 'izm', 'com'}
# 
# print(test_set_1 | {'python', 'www'})
# print(test_set_1 & {'python', 'www'})
# print(test_set_1 - {'python', 'www'})
# print(test_set_1 ^ {'python', 'www'})
# 
# 
# 《実行結果》
# {'com', 'www', 'izm', 'python'}
# {'python'}
# {'com', 'izm'}
# {'com', 'www', 'izm'}
# 
# 
# ３ セットを比較して更新
# intersection_updateはセットと引数の反復可能オブジェクトとの間における共通の要素を持つセットへ更新します。difference_updateは引数の反復可能オブジェクトに含まれる要素を除外したセットへ更新します。symmetric_difference_updateはセットと引数の反復可能オブジェクトのどちらかだけに含まれる要素を持つセットへ更新します。
# 
# test_set_1 = {'python', 'izm', 'com'}
# test_set_1.intersection_update({'python', 'www'})
# print(test_set_1)
# 
# test_set_1 = {'python', 'izm', 'com'}
# test_set_1.difference_update({'python', 'www'})
# print(test_set_1)
# 
# test_set_1 = {'python', 'izm', 'com'}
# test_set_1.symmetric_difference_update({'python', 'www'})
# print(test_set_1)
# 
# 
# 《実行結果》
# {'python'}
# {'com', 'izm'}
# {'com', 'www', 'izm'}
# 
# また演算子を用いることでも同様の結果を得ることができます。
# test_set_1 = {'python', 'izm', 'com'}
# test_set_1 &= {'python', 'www'}
# print(test_set_1)

# test_set_1 = {'python', 'izm', 'com'}
# test_set_1 -= {'python', 'www'}
# print(test_set_1)

# test_set_1 = {'python', 'izm', 'com'}
# test_set_1 ^= {'python', 'www'}
# print(test_set_1)
# 
# 
# 《実行結果》
# {'python'}
# {'com', 'izm'}
# {'com', 'www', 'izm'}
# 
# 