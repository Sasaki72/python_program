# 【日付・時間】
# プログラミングにおける日付や時間の使用頻度は高いです。言語ごとにかなり違いがあるので、調べたりする機会は多々あると思います。
# 
# 1 日付の取得
# 2 日付の計算
# 3 うるう年の判定
# 
# 【日付の取得】
# 
# 日付の取得方法は下記の通りです。標準ライブラリであるdatetimeを使用しましょう。このように標準ライブラリやサードパーティライブラリなど、特定の機能を使用したい場合はimportを用います。
# ※str(‘a’)やint(‘1’)など、ごく一般的なプログラムにおいても高い使用頻度が想定されている一部のものは、importを行わずに使うことができます。
# 
# import datetime  (import = 取り寄せる、datetime = 日時)
# 
# 
# today = datetime.date.today()　　　　　　　　　(date = 日にち)
# todaydetail = datetime.datetime.today()　　　(todaydetail = 今日の詳細、)
#  
# # 今日の日付
# print('----------------------------------')
# print(today)
# print(todaydetail)
#  
# # 今日に日付：それぞれの値
# print('----------------------------------')
# print(today.year)
# print(today.month)
# print(today.day)
# print(todaydetail.year)
# print(todaydetail.month)
# print(todaydetail.day)
# print(todaydetail.hour)
# print(todaydetail.minute)
# print(todaydetail.second)
# print(todaydetail.microsecond)
#  
# # 日付のフォーマット
# print('----------------------------------')
# print(today.isoformat())
# print(todaydetail.strftime("%Y/%m/%d %H:%M:%S"))
# 
# 《実行結果》
# ----------------------------------
# 2010-05-08
# 2010-05-08 15:42:00.731000
# ----------------------------------
# 2010
# 5
# 8
# 2010
# 5
# 8
# 15
# 42
# 0
# 731000
# ----------------------------------
# 2010-05-08
# 2010/05/08 15:42:00
# 
# ※プログラムの実行時間によって結果は異なります。
# 
# 
# 【日付の計算】
# 日付の計算はtimedeltaを使用します。timedeltaは月の日数、うるう年なども気にしないでよいので、自分で計算するより多くの手間を省くことができます。
# 
# import datetime
#  
#  
# today = datetime.datetime.today()
#  
# 今日の日付
# print(today)
#  
# 明日の日付
# print(today + datetime.timedelta(days=1))
#  
# newyear = datetime.datetime(2010, 1, 1)
#  
# 2010年1月1日の一週間後
# print(newyear + datetime.timedelta(days=7))
#  
# 2010年1月1日から今日までの日数
# calc = today - newyear
#  
# 計算結果の戻り値は「timedelta」
# print(calc.days)
# 
# 《実行結果》
# 2010-05-08 15:36:24.006000
# 2010-05-09 15:36:24.006000
# 2010-01-08 00:00:00
# 127
# 
# ※プログラムの実行時間によって結果は異なります。
# 
# 
# 【うるう年の判定】
# その年がうるう年かどうかを判定するにはcalendar.isleapを、指定期間内に何回のうるう年があるかを取得するにはcalendar.leapdaysを使用します。
# 
# import calendar
#  
# print(calendar.isleap(2015))
# print(calendar.isleap(2016))
# print(calendar.isleap(2017))
#  
# print(calendar.leapdays(2010, 2020))
# 
# 《実行結果》
# False
# True
# False
# 2
# 
# 