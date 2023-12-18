#1
expression = input("Введіть вираз через пробіл : ")
parts = expression.split()
a = float(parts[0])
operator = parts[1]
b = float(parts[2])
if operator =='+':
    print(a+b)
elif operator =='-':
    print(a-b)
elif operator =='*':
    print(a*b)
elif operator =='/':
    print(a/b)

#2
import random
list = [random.randint(-100,100) for i in range(10)]
print(list)
print(f"Найменше значення : {min(list)}")
print(f"Найбільше значення : {max(list)}")
negative_number = sum(1 for num in list if num < 0)
print(f"Кількість від'ємних чисел : {negative_number}")
positive_number = sum(1 for num in list if num > 0)
print(f"Кількість додатніх чисел : {positive_number}")
zero_number = sum(1 for num in list if num == 0)
print(f"Кількість нулів : {zero_number}")
