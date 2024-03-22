print("Введите количество элементов")

a = int(input())

print("Введите элементы через пробел")

b = list(map(int, input().split()))[:a]

c = set(b)

print(len(c))
