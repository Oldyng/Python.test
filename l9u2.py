print("Введите первый список чисел")
a = set(input().split())

print("Введите второй список чисел")
b = set(input().split())

print(len(a.intersection(b)))
