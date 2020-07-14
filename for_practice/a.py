# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_line = input()
input_list = input_line.split()
int_list = []
for i in input_list:
    int_list.append(int(i))
if int_list[0] == int_list[1]:
    print("eq")
else:
    print(max(int_list))

    