# kaptunk lapot, azokon vannak feladatok, ezek azok megoldásai

# 1. feladat------------------------------------------------
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. feladat------------------------------------------------
print()
for x in range(1,6):
    for y in range(1,x+1):
        print(y, end=" ")
    print()

# 3. feladat------------------------------------------------
print()
szam = int(input("Kérek egy számot: "))
osszeg = 0
for i in range(1,szam + 1):
    osszeg += i

print("Összeg: ", osszeg)

# 4. feladat------------------------------------------------
print()
szam = int(input("Kérek egy számot: "))
for i in range(1, 11):
    print(szam * i)

# 5. feladat-----------------------------------------------
print()
lista = [12, 75, 150, 180, 145, 525, 50]
for i in lista:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)

# 6. feladat------------------------------------------------
print()
szam = int(input("Kérek egy számot: "))
szamjegyekSzama = len(str(szam))
print(szamjegyekSzama, "db")

# 7. feladat (sztem ugyanaz mint a második de idk.. feladta, hogy csináljuk meg, ha unatkozunk xddd)

# 8. feladat
print()
lista = [10,20,30,40,50]
lista = reversed(lista)
for i in lista:
    print(i)

# 9. feladat-----------------------------------------------
print()
for i in range(-10,0):
    print("\t", i)
else:
    print("Done!")

# 10. feladat
print()
for i in range(5):
    print(i)
else:
    print("Done!")

# "11-17-ig jó munkát majd, használgasság, gyakorolgassák" xdd gondolom otthoni szorgalminak feladta