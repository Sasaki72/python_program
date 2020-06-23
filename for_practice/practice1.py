# coding:utf-8

apple_price = 200
money = 1000

input_count = input("購入するりんごの数を入力してください")
count = int(input_count)
total_price = apple_price * count

print("購入するりんごの数は" + str(count) + "個です")
print("支払いは" + str(total_price) + "円です")

if money > total_price:
    print("購入するりんごの数は" + str(count) + "個です")
    print("残金は" + str(money - total_price) + "円です")
elif money == total_price:
    print("購入するりんごの数は" + str(count) + "個です")
    print("財布は空になりました")
else:
    print("金額が足りません")
    print("りんごを買えませんでした")

