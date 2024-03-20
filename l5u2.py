print("Введите слово маленькими латинскмими буквами")
word = str(input())

v = 0
c = 0
a = 0
e = 0
i = 0
o = 0
u = 0

for letter in word:
    if letter in "aeiou":
        v += 1
    elif letter in "bcdfghjklmnpqrstvwxyz":
        c += 1

for letter in word:
    if letter in "a":
        a += 1
    elif letter in "e":
        e += 1
    elif letter in "i":
        i += 1
    elif letter in "o":
        o += 1
    elif letter in "u":
        u += 1

print("Гласных букв:", v)
print("Согласных букв:", c)

if a + e + i + o + u == 0:
    print(False)
else:    
    print(f"Количество букв a: {a};\nКоличество букв e: {e};\nКоличество букв i: {i};\nКоличество букв o: {o};\nКоличество букв u: {u}.")
