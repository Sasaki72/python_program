# 【if文】
# プログラミングにおいて最も重要といっても過言ではないif文です。Pythonにおいても当然if文が存在しますのでここで確認しておきましょう。
# 
# 1 if文の基礎
# 2 条件の組み合わせ
# 3 pass
# 
# 
# １ if文の基礎
# ifを記述後に条件式を記述し、その条件がTrueであれば条件配下の処理が実行される仕組みとなります。それぞれの条件式の最後に必ず「 : 」（コロン）を忘れずに付けましょう。
# 
# value = 2

# if value == 1:
#     print('valueの値は1です')
# elif value == 2:
#     print('valueの値は2です')
# elif value == 3:
#     print('valueの値は3です')
# else:
#     print('該当する値はありません')
# 
# 
# 《実行結果》
# valueの値は2です
# 
# 別の条件式を定義する際にはelifを使用します。どの条件にも該当しない場合の処理を定義する場合はelseを使用しましょう。
# 
# 
# ２ 条件の組み合わせ
# 条件の組み合わせにはand、orなどを用います。下記コードにおいてandは、value_1とvalue_2の両者がTrueであれば式としてTrueとみなし、orの場合はvalue_1とvalue_2のどちらかがTrueであれば式としてTrueとみなします。
# 
# value_1 = 'python'
# value_2 = 'izm'
# 
# if value_1 == 'Python':
#     pass
# elif value_1 == 'python' and value_2 == 'izm':
#     print('2番目の条件式がTrue')
# elif value_1 == "IZM" or value_2 == "PYTHON":
#     print('3番目の条件式がTrue')
# 
# 
# 《実行結果》
# 2番目の条件式がTrue
# 
# 
# ３ pass
# 先程のコードの5行目にpassという記述がありますが、これは簡単にいうと何もしませんという命令になります。Pythonはインデントによってブロック構造を形成しているため、基本的には空のブロックを持つことができません。インタープリタはifの「 : 」のすぐ後にあるブロックに命令が記述されていると判断しますが、それがない場合は構文的には正しくないものとなってしまうためエラーを発生させます。それを回避するのがpassであり、これは後述するクラスなどでも使用することができます。
# 
# 
# value_1 = 'python'
# value_2 = 'izm'
# 
# if value_1 == 'Python':
#     pass
# elif value_1 == 'python' and value_2 == 'izm':
#     print('2番目の条件式がTrue')
# elif value_1 == "IZM" or value_2 == "PYTHON":
#     print('3番目の条件式がTrue')
# 
# 
