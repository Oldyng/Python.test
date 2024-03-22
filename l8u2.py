def rcr(a):
    r = [a[-1]]
    r += a[:n-1]
    return r

print("Введите число") 
n = int(input())

print("Введите числа через пробел") 
l = [x for x in input().split()]

print(*rcr(l))