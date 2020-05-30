# coding:utf-8
a=1
b=2
print(a+b)

for q in [1,2,3,4,5,6,7,8]:
  print(q)
    
for q in range(1,100+1):
  print(q)
  print("こんにちは")

range(1,5+1)

for q in "Hello":
    print(q)

total = 0
z = 1
while total <= 50:
  total = total + z
  z = z + 1
print(total)

for a in range(1, 10+1):
  if a <= 5:
    print("小さいです")
  else:
    print("大きいです")


for a in range(1, 10 + 1):
  print(a)
  if a % 2 == 0:
    print("○")
  if a % 3 == 0:
    print("×")
  if (a % 2 == 0) and (a % 3 == 0):
    print("△")

while True:
  total = a
  a = a + 1
  if total > 50:
    break
print(total)

