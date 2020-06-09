# 【クラス作成】
# Pythonではクラスを定義しそれを作成する（インスタンス化）ことができます。クラス化する事によって様々な恩恵を得ることができ、プログラミングの幅も広がります。
# 
# 1 クラスの基礎
# 2 クラスの初期化
# 3 クラスの利用
# 
# 
# １ クラスの基礎
# classと記述し、後にクラス名が続きます（今回の例ではTestClassがクラス名になります）。クラス名の後には必ず「 : 」（コロン）を付けましょう。
# 
# class TestClass:
# 
#     def __init__(self, code, name):
#         self.code = code
#         self.name = name
# 
# 
# classes = []
# classes.append(TestClass(1, 'テスト１'))
# classes.append(TestClass(2, 'テスト２'))
# 
# for test_cls in classes:
#     print('===== Class =====')
#     print('code --> ' + str(test_cls.code))
#     print('name --> ' + test_cls.name)
# 
# 
# 《実行結果》
# ===== Class =====
# code --> 1
# name --> テスト１
# ===== Class =====
# code --> 2
# name --> テスト２
# 
# 
# これでクラスを定義し、クラスからインスタンスを作成し、それを利用することができました。それぞれの詳細を見ていきましょう。
# 
# 
# ２ クラスの初期化
# 3行目に__init__というメソッドがあります。これは特殊なメソッドで、クラスの初期化時に必ず実行されるメソッドです。クラスを利用する上での前準備のような処理を記述することが多いでしょう。もう一つの注目点として__init__メソッドの第一引数にselfがあります。これはクラスのインスタンス自身を表すもので、self.xxといった形で自身が保持する情報へアクセスする事ができます。いわゆる通常のメソッド（インスタンスメソッド）では省略する事が出来ないので、必ず書いてください。
# 
# class TestClass:
# 
#     def __init__(self, code, name):
#         self.code = code
#         self.name = name
# 
# 
# classes = []
# classes.append(TestClass(1, 'テスト１'))
# classes.append(TestClass(2, 'テスト２'))
# 
# for test_cls in classes:
#     print('===== Class =====')
#     print('code --> ' + str(test_cls.code))
#     print('name --> ' + test_cls.name)
# 
# 
# 続いて4、5行目ではcodeとnameという2つのインスタンス属性（インスタンス変数）を__init__メソッドの引数から自身のインスタンスへ引き渡しています。これらはTestClassインスタンス自身からはself.codeやself.nameでアクセスすることができ、クラスを作成した側からはインスタンス名.codeやインスタンス名.nameでアクセスすることができます（例示コードの場合はtest_cls.codeなど）。
# 
# class TestClass:
# 
#     def __init__(self, code, name):
#         self.code = code
#         self.name = name
# 
# 
# classes = []
# classes.append(TestClass(1, 'テスト１'))
# classes.append(TestClass(2, 'テスト２'))
# 
# for test_cls in classes:
#     print('===== Class =====')
#     print('code --> ' + str(test_cls.code))
#     print('name --> ' + test_cls.name)
# 
# 
# ３ クラスの利用
# 9行目と10行目でクラスのインスタンス化を行っています。クラス定義から2つインスタンスを作成し、それぞれ別のcodeとnameを__init__メソッドを通して情報を保持させます。これらはインスタンスごとに異なる情報を設定することができます（例示コードでは1 と テスト１のインスタンスと2 とテスト２の情報を持つインスタンスが存在している）。
# 
# class TestClass:
# 
#     def __init__(self, code, name):
#         self.code = code
#         self.name = name
# 
# 
# classes = []
# classes.append(TestClass(1, 'テスト１'))
# classes.append(TestClass(2, 'テスト２'))
# 
# for test_cls in classes:
#     print('===== Class =====')
#     print('code --> ' + str(test_cls.code))
#     print('name --> ' + test_cls.name)
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
