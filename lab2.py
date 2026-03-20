'''
# 1.1
a = int(input("Первое число:"))
b = int(input("Второе число:"))
c = int(input("Третье число:"))

min_num = min(a,b,c)
print(f"Минимальное число: {min_num}")



# 1.2
a = int(input("Первое число:"))
b = int(input("Второе число:"))
c = int(input("Третье число:"))

if 1 <= a <= 50:
    print(f"Число {a} попадает в интервал от 1 до 50")
if 1 <= b <= 50:
    print(f"Число {b} попадает в интервал от 1 до 50")
if 1 <= c <= 50:
    print(f"Число {c} попадает в интервал от 1 до 50")
          


# 1.3
m = float(input("Введите число:"))

for i in range(1, 11):
    print( f" {i} * {m} = {i * m}")



# 1.4

print("Введите целые числа. для окончания нажмите Enter")

total = 0
count = 0

while True:
    s = input()
    if s == "":
        break
    num = int(s)
    total += num
    count +=1
    
print(f"Сумма: {total}")
print(f"Количество: {count}")

=
# 2.12

string_w = input("Введите строку: ")
word = ""

for c in string_w:
    if c == " ":
        # выводиn слово, если оно не пустое и оканчивается на u
        if word != "" and word[-1] == "u":
            print(word)
        word = ""            
    else:
        word = word + c    

# проверяет последнее слово
if word != "" and word[-1] == "u":
    print(word)

'''
# 3.12
import sys 
import random

A = []

for i in range(1, 11):
    A.append(int(sys.argv[i]))
min_odd = None
for num in A:
    if num % 2 != 0:
        if min_odd is None or num < min_odd:
            min_odd = num
print("Массив A", A)
print(f"Наименьший нечетный: {min_odd} ")

B = []
for i in range(10):
    B.append(random.randint(1, 100))

print("Рандомно созданный массив B:", B)

for i in range(10):
    temp = A[i]
    A[i] = B[i]
    B[i] = temp

print("A:", A)
print("B:", B)




