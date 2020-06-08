# 【while文】
# Pythonでもwhile文が存在します。for文で代用できるケースもありますが、while文ではより複雑な条件で繰り返し処理を行うことができます。
# 
# 【while文の基礎】
# 下記例ではcounterが10より大きくなるまで繰り返しprintを実行します。(https://www.python-izm.com/basic/print/)
# 
# counter = 0
# 
# while counter < 10:
#     counter += 1
#     print(counter)
# 
# 
# 《実行結果》
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 
# 
# 次のようにループ条件へTrueを指定することで簡単に無限ループを作成することができます。breakでループを終了させていますが、これは次項で説明します。(https://www.python-izm.com/basic/break/)
# 
# counter = 0

# while True:
#     counter += 1
#     print(counter)
#     if counter == 10:
#         break
# 
# 
# 《実行結果》
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 
# 