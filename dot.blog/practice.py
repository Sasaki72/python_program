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

x1 = 'たろう'

# クラス『NameCheck』をインスタンス化
nc_ta = NameCheck(x1)


# 変数lengthに格納されている値を呼び出す
len1 = nc_ta.length
print(len1)
# 出力結果　0


# 文字数を測る関数text_lenを実行
y1 = nc_ta.text_len()
print(y1)

# 偶数か奇数かを判定する関数even_or_oddを実行
y2 = nc_ta.even_or_odd()
print(y2)

# 出力結果
# 3 # print(y1)
# 奇数 # print(y2)