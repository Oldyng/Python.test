print("Введите максимальную массу для лодки")
m = int(input())

print("Введите количество рыбаков")
n = int(input())

print("Введите вес каждого рыбака (по одному числу на строку)")
a = []
for _ in range(n):
    a.append(int(input()))
    
print('Минимальное число лодок:', (2 * min(a) <= m) + len([x for x in a if x + min(a) > m]))

