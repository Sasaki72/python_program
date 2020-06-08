def exception_test(value_1, value_2):

    print('＝＝＝＝計算開始＝＝＝＝')

    result = 0

    try:
        result = value_1 + value_2
    except:
        print('計算出来ませんでした！')
        raise
    finally:
        print('計算終了')

    return result


try:
    print(exception_test(100, 100))
    print(exception_test(200, 200))
    print(exception_test(300, '300'))
except:
    print('エラーを受け取りました')