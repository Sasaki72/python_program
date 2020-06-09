# 【クラス継承】
# Pythonではクラスを継承して、既存クラスを容易に拡張することができます。
# 
# クラス継承の基礎
# 親クラスであるCountryを定義しcountry_name属性を保持します。さらにCityをCountryクラスを継承して定義しcity_name属性を保持します。
# 
# class Country:
# 
#     def __init__(self, country_name):
#         self.country_name = country_name
# 
# 
# class City(Country):
# 
#     def __init__(self, country_name, city_name):
#         super().__init__(country_name)
#         self.city_name = city_name
# 
# 
# classes = []
# classes.append(City('Japan', 'Tokyo'))
# classes.append(City('USA', 'Washington, D.C.'))
# 
# for test_cls in classes:
#     print('===== Class =====')
#     print('country_name --> ' + test_cls.country_name)
#     print('city_name --> ' + test_cls.city_name)
# 
# 
# 《実行結果》
# ===== Class =====
# country_name --> Japan
# city_name --> Tokyo
# ===== Class =====
# country_name --> USA
# city_name --> Washington, D.C.
# 
# 
# 既存クラスの継承を行って新たにクラスを定義する場合、クラス名の後に「 () 」を用いてスーパークラス名を記述します（例示コードの場合はCountry、7行目）。また親クラスが持つメソッドと同じ名前のメソッドを定義することができ、その処理内容を上書きすることができます。例示のコードの場合、10行目で親クラスの同名メソッドを呼び出すことにより親が行っている処理をそのまま利用しつつ、子クラス側で独自の処理を追加しています。子クラス側ではcountry_name属性に対して値を代入していないにもかかわらずprintで出力できているのも、親クラス側でその処理を行っているからです。
# なおPython 3系ではさほど意識する必要はありませんが、2系では旧クラススタイルおよび新クラススタイルがあります。次項の新旧クラススタイルも目を通しておくと良いでしょう。
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
