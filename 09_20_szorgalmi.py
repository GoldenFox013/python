print("11. feladat----------------------------------------------------------\n")

print("The prime numbers between 25 and 50 are:\n")
for x in range(25,51):
    prim_e = True
    for y in range(2,x//2):
        if x % y == 0:
            prim_e = False
    if prim_e == True:
        print(x)

print("\n12. feladat--------------------------------------------------------\n")

lista = [0,1]

for i in range(10):
    if i < 2:
        print(lista[i])
    else:
        new = lista[-2] + lista[-1]
        print(new)
        lista.append(new)
    
print("\n13. feladat--------------------------------------------------------\n")

adott_szam = 5
szorzat = 1
for i in range(2,adott_szam + 1):
    szorzat = i * szorzat
print(f"{adott_szam}! = {szorzat}")

print("\n14. feladat--------------------------------------------------------\n")

adott_szam = str(76452)
for i in range(1, len(adott_szam) + 1):
    print(adott_szam[i * -1], end = "")

print("\n15. feladat--------------------------------------------------------\n")

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(my_list)):
    if i % 2 != 0:
        print(my_list[i])

print("\n16. feladat--------------------------------------------------------\n")

adott_szam = 6
for i in range(1, adott_szam + 1):
    print(f"Number is: {i} and the cube is {i**3}")

print("\n17. feladat--------------------------------------------------------\n")

# 1 ciklussal:
for i in range(-4,5):
    print("* " * (5 - abs(i)))

print()

# 2 ciklussal:
for i in range(5):
    print("* " * (i + 1))
for i in range(-4,0):
    print("* " * abs(i))
