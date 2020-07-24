# 【可変長引数】
# Pythonでは可変長引数を定義することができます。プログラミングを行う上で必須の知識ではないので、まずは「そういった機能があるんだ」という程度でも構いません。慣れてきたらPythonの便利な機能の1つとして活用するとよいでしょう。
# 
# 1 *args
# 2 **kwargs
# 
#  
# １ *args
# 関数のパラメータ定義において、引数名の前に「 * 」を付与することで可変長引数となります。
# 
# def test_func(*args):
#     print(args)
# 
# test_func(1, 2, 3, 4, 5)
# 
# 
# 《実行結果》
# (1, 2, 3, 4, 5)
# 
# 
# 実行結果の通り、「 * 」を用いた可変長引数は、関数内においてタプルとして引き渡されます。これはたとえばos.path.joinを使用したパスの結合・連結(https://www.python-izm.com/basic/path_join/)などで、結合対象のパスをいくつでも渡せるような機能を持たせることができます。また通常の引数と併用することも可能です。
# 
# def test_func(code, name, *args):
#     print(code, name)
#     print(args)
# 
# test_func(100, 'python-izm', 'JP', 'US')
# 
# 
# 《実行結果》
# 100 python-izm
# ('JP', 'US')
# 
# 
# なお引数名は必ずしも*argsでなくてはならないわけではありません。ただし慣習的に*argsとすべき、というような場合もあります（汎用的な用途の関数など）。なおargsはargumentsの略です。
# 
# def test_func(code, name, *countries):
#     print(code, name)
#     print(countries)

# test_func(100, 'python-izm', 'JP', 'US')
# 
# 
# 
# ２ **kwargs
# 引数名の前に「 ** 」を付与することでも可変長引数となります。
# 
# def test_func(**kwargs):
#     print(kwargs)
# 
# test_func(code=100, name='python-izm')
# 
# 
# 《実行結果》
# {'code': 100, 'name': 'python-izm'}
# 
# 
# 実行結果の通り、「 ** 」を用いた可変長引数は、関数内においてディクショナリとして引き渡されます（keyが引数名、valueが値）。こちらも同様に通常の引数と併用することができ、さらに「 * 」を使用した可変長引数と併用することも可能です。
# 
# def test_func(code, name, kana, *args, **kwargs):
#     print(code, name, kana)
#     print(args)
#     print(kwargs)
# 
# test_func(
#     100, 'python-izm', u'パイソンイズム',
#     'JP', 'US', 
#     email='xxxx', city='Tokyo'
# )
# 
# 
# 《実行結果》
# 100 python-izm パイソンイズム
# ('JP', 'US')
# {'email': 'xxxx', 'city': 'Tokyo'}
# 
# 
# こちらの引数名も同様に、必ずしも**kwargsでなくてはならないわけではありません。ただし慣習的に**kwargsとすべき、というような場合もあります（汎用的な用途の関数など）。なおkwargsはkeyword argumentsの略です。
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
