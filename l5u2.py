print("Введите слово маленькими латинскмими буквами")
word = str(input())

a = 0
b = 0

for letter in word:
    if letter in "aeiou":
        a += 1
    elif letter in "bcdfghjklmnpqrstvwxyz":
        b += 1
else:
    print(False)

print("Гласных букв:", a)
print("Согласных букв:", b)