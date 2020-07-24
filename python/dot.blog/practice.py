# # coding:utf-8
class Car:
    def __init__(self, color):
        self. color = color

car1 = Car("red")
car2 = Car("blue")
car3 = Car("green")

print(car1. color)
print(car2. color)
print(car3. color)

class MenuItem:
    def __init__ (self):
        print("メニューです")

menu_itme1 = MenuItem()


class MenuItem:
    # __init__メソッドを定義してください
    def __init__(self):
        print('MenuItemクラスのインスタンスが生成されました！')

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

print(menu_item1.info())

result = menu_item1.get_total_price(1000)
print('合計は' + str(result) + '円です')