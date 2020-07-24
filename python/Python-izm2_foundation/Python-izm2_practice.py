# 複素数
# 複素数を表すcomplexは、数値へjやJを付与することで虚数になります。次の例は実数が100、虚数が5の複素数です。
# 1
# 2
# 3
# 4
# 5
# test_complex = 100 + 5j

# print(test_complex)
# print(test_complex.real)
# print(test_complex.imag)
# (100+5j)
# 100.0
# 5.0


# この結果が並び順でないのは何でか？
# test_set_1 = set()

# test_set_1.add('python')
# test_set_1.update({'izm', '_', 'com', '.'})

# print(test_set_1)

# test_list_1 = [['https', 'www'], ['python-izm', 'com']]

# for value in test_list_1:
#     print(value)

# for value_1, value_2 in test_list_1:
#     print(value_1, value_2)

test_list_1 = [['https', 'www'], ['python-izm', 'com'], ['python', 'c']]

for value in test_list_1:
    print(value)

for value_1, value_2, value_3 in test_list_1:
    print(value_1, value_2, value_3)
    
# 関数とメソッド 
# 関数
def test_func():
    print('call test_func')
  
  
class TestClass:
    # メソッド
    def test_method():
        print('call test_method')
 
print('------------------------')
print(test_func)
print(TestClass.test_method)
 
print('------------------------')
print(type(test_func))
print(type(TestClass.test_method))
 
print('------------------------')
t = TestClass()
print(test_func)
print(t.test_method)



