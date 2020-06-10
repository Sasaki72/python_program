# 【文字列を連結してみよう】
# 文字列は「+」で連結できますが、文字と数値を連結するときは変換操作が必要
# 《Pythonでは数値と文字列は別扱い》
# 
# print("abc" + "def")
# 
# 《実行結果》
# abcdef
# 
# 「＋」を使えばいくつでも連結できる
# 
# 《COLUMN》
# 「*」で繰り返す
# 文字列では「*」(アスタリスク)と言う計算式も使える
# 
# print("abc"*3)
# 
# 《実行結果》
# abcabcabc
# 
# 
# 文字列と数値は連結できない
# 「文字列」と「数値」は「+」で連結できない
# 
# print("abc" + 123)
# 
# 《実行結果》
# Error
# 
# 
# これは「+」の記号がそれぞれ違う意味で作用するから
# ・文字列の場合は「連結」
# ・数値の場合は「足し算」
# そのためErrorが出てしまう
# 
# 『解決方法は「数値」を「文字列」に変換すればいいだけ』
# 
# print("abc" + "123")
# 
# 《実行結果》
# abc123
# 
# 【計算と連結させたいとき】
# 「abc」と「123*234」の計算式を連結するときの方法
# 
# print("abc" + "123*234")
# 
# 《実行結果》
# abc123*234　(計算されない状態で出てくる)
# 
# 【重要】
# 今回の「文字列」と「計算式」を連結するためにはPythonの「str関数」を使う
# 「関数」とは、何か「値」を渡すと、内部で計算や加工など何らかの処理を行い、その結果を戻してくれる機能の事
# このように、関数を使って処理をする事を「関数を呼び出す(coll)」と言う
# 
# str関数は、カッコの中に「数値」を渡すと、それを「文字列」に変換した値として戻してくれる
# このstr関数を使って、プログラムを次のように記述する
# 
# print("abc" + str(123*234))
# 
# 《実行結果》
# abc28782
# 
# 
# ここでは「文字列」と「数値」を連結するときはstr関数の変換が必要になる事を説明した
# 今回以外の、数値を何らかの理由で文字列として扱いたいとき(例えば、
# 末尾から３桁目の数を取り出したいとき、「特定の桁の文字」を取り出したい時など)はstr関数を使う
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
