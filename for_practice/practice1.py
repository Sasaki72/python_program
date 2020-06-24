# coding:utf-8

apple_price = 200
money = 1000

input_count = input("購入するりんごの数を入れてください")
count = int(input_count)
total_price = count * apple_price

print("購入するりんごの数は" + str(count) + "個です")
print("支払い金額は" + str(total_price) + "円です")

if money > total_price:
    print("購入するりんごの数は" + str(count) + "個です")
    print("支払い金額は" + str(total_price) + "円です")
elif money == total_price:
    print("購入するりんごの数は" + str(count) + "個です")
    print("財布が空になりました")
else:
    print("お金が足りません")
    print("購入できませんでした")
