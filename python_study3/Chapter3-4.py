# 【文字を表示してみよう】
# Pythonでは数値だけでなく、文字も扱える
# ただし文字を扱うには、少し特殊な書き方が必要
# 
# 【「""」か「’’」で囲んで書く】
# Pythonでは文字の事を「文字列」と言う
# たとえ１文字でも文字列と言う
# 文字列を示すには、その文字全体を「”」(ダブルクォーテーション)か「’」(シングルクォーテーション)で囲う
#  "abc" か 'abc' など
# 
# 【「”」と「’」の使い分け】
# 一般的には全体をどちらかで統一する
# 
# "It's a pen "  正しい表記
# 'It's a pen' 正しくな表記(「'」の中に「'」がある)
# もしくは「'」を「¥」または「\'」と記述する方法もある
# これを「エスケープシーケンス」という
# 
# 'It's a pen'   間違いの表記
#          ↓
# 'It\'s a pen'  正しい表記
# 
# 
# 【「¥」と「\」に注意】
# Windowsは「¥」
# Macは「\」
# 
#  しかし、「10,000」を表示させたい時「\10,000」と入力すると「@00」とでる
# 「\10,000」　間違いの表記
#     ↓
# 「\\10,000」　正しい表記
# 「\\」と２本入れる
# 
# 《COLUMN》
# raw Stringを利用する
# 「¥」や「\」文字を正しく示す方法は、別にもある。それは、
# 
# print(r"\10,000")
# 
# のように、文字列の「r」を付ける方法
# 「rを付けた文字列」は「raw String」と呼ばれ「¥」や「\」を特殊文字として扱わない。
# 列中に「¥」や「\」をたくさん含んでいるときはこの方法を取ると楽です
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
