# # class(クラス)の基本・使い方と定義方法

# # クラスとは、インスタンスに共通で利用する値（データ）や特定の実行処理を行うプログラムを一つにまとめた設計図の様なもの
# # インスタンス (instance)とは『実態』と言う意味。
# # 変数にクラスを格納することでクラスがインスタンス化（実体化）され、クラスが持つデータや実行処理を呼び出せる様になります。

# class SampleVar2:
#     def __init__(self, no):
#         self.var_x = no

#     def func1(self, add_no):
#         self.var_x += add_no
#         return self.var_x

#     def func2(self, add_no):
#         self.var_x += add_no
#         return self.var_x          #　←ここの部分が消えても支障が無いのでは？ 

# # SampleVar2をインスタンス化
# sv2 = SampleVar2(5)

# # 変数var_xに格納されている値を確認
# print(sv2.var_x)

# # func1に引数を渡して実行
# y1 = sv2.func1(10)
# print(y1)

# # func2に引数を渡して実行
# y2 = sv2.func1(20)
# print(y2)        



# class NameCheck:
#     def __init__(self, text):
#         self.text = text
#         self.length = 0

#     def text_len(self):
#         for i in self.text:
#             self.length += 1
#         return self.length

#     def even_or_odd(self):
#         if self.length % 2 == 0:
#             return '偶数'
#         else:
#             return '奇数'

# x1 = 'たろう'
# # クラス『NameCheck』をインスタンス化
# nc_ta = NameCheck(x1)

# # 変数lengthに格納されている値を呼び出
# len1 = nc_ta.length
# print(len1)

# # 文字数を測る関数text_lenを実行
# y1 = nc_ta.text_len()
# print(y1)

# # 変数lengthに格納されている値を呼び出す
# len2 = nc_ta.length
# print(len2)

# # 偶数か奇数かを判定する関数even_or_oddを実行
# y2 = nc_ta.even_or_odd()
# print(y2)

# # 出力結果
# # 3 # print(y1)
# # 奇数 # print(y2)



class NameCheck:
    
    def __init__(self, text):
        self.text = text
        self.length = 0
        
    def text_len(self):
        for i in self.text:
            self.length += 1
        return self.length
    
    def even_or_odd(self):
        if self.length % 2 == 0:
            return '偶数'
        else:
            return '奇数'

y1 = 'たろう'

# クラス『NameCheck』をインスタンス化
nc_ta = NameCheck(y1)


# 変数lengthに格納されている値を呼び出す
len1 = nc_ta.length
print(len1)

# 文字数を測る関数text_lenを実行
x1 = nc_ta.text_len()
print(x1)

# 変数lengthに格納されている値を呼び出す
len2 = nc_ta.length
print(len2)

# 偶数か奇数かを判定する関数even_or_oddを実行
y2 = nc_ta.even_or_odd()
print(y2)