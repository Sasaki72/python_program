# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_line = input()
test = input_line
test1 = test.split()
if "km" == test1[1]:
    test2 = int(test1[0]) *1000000
    print(test2)
elif "cm" == test1[1]:
    test2 = int(test1[0]) *10
    print(test2)
elif "m" == test1[1]:
    test2 = int(test1[0]) *1000
    print(test2)