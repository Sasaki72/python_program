# 【インポート】
# Pythonのインポート(import)は標準ライブラリのインポートはもちろん、自ら作成したモジュールのインポートも行うことができます。
# 
# 1 import, from
# 2 別名インポート – as
# 
# 
# １　import, from
# 
# まずは簡単なモジュールファイルを用意します。下記コードをtestmod.pyという名前で作業ディレクトリに保存してください。
#
#testmod.py
# class TestClass:
# 
#     def __init__(self):
#         print('create TestClass')
# 
#     def test_method(self, val):
#         print('call test_method')
#         print(val)
#
# 次は上記モジュールを実行（インポート）するコードを記述します。Pythonはコード中のどこにimport、fromを記述してもエラーにはなりません。
# 
# import testmod
# 
# test_class_1 = testmod.TestClass()
# test_class_1.test_method('1')
# 
# 
# from testmod import TestClass
# 
# test_class_2 = TestClass()
# test_class_2.test_method('2')
# 
# 
# 《実行結果》
# create TestClass
# call test_method
# 1
# create TestClass
# call test_method
# 2
# 
# まずは1行目のimportで対象のモジュールをインポートしています。これでtestmodモジュールを使用する準備ができました。この時のモジュール名はファイル名の.pyを含まない形にしてください。そして次の行でtestmod内のTestClassのインスタンスを作成した形です。この場合はモジュール名.クラス名でインスタンス化を行い、TestClassが定義しているtest_methodの呼び出しを行いました。
# 毎回モジュール名.クラス名と記述するのは面倒だというときには、7行目のようなfromを使用しましょう。fromの後にモジュール名、importの後にクラス名という指定方法です。これにより次の行では、前述のモジュール名.クラス名ではなくクラス名だけで使用出来るようになります。なおクラスだけではなく、モジュール内に定義されているものであれば関数や変数などもfromでインポートすることができます。
# 
# 
# ２ 別名インポート – as
# 
# インポートを行う時、別の名前でインポートをしたい場合があります。これはたとえば以下のようなケースが挙げられます。

# ・サードパーティ製のモジュールや自作のモジュールなどで、モジュールファイル名が同じケース（それらをfromで利用したい場合など）
# ・コード内で混乱を招くことがないよう、同じような機能を持つモジュールに対し、わかりやすい名前で利用したいケース
# ・元々のモジュール名が長いため、短い名前で利用したいケース
# 
# from datetime import datetime
# datetime.today()
# 
# from datetime import datetime as d
# d.today()
# 
# asを用いることで別名インポートを行うことができます。上記コードではtodayを2回呼んでいますが、いずれも全く同じものです。
# 
# 
# 