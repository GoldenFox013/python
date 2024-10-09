import random
# import string

# nevek = ["Anna", "Béla", "Cecil", "Dávid", "Emma"]
# nev = random.choice(nevek)
# print(f"A választott név: {nev}")                       # ezek újak
# print(f"A választott nevek: {random.sample(nevek,2)}")
# -----------------------------------------------------------------
# alany = ['A macska', 'A kutya', 'A kisfiú', 'A tanár']
# ige = ['fut', 'ugrik', 'alszik', 'játszik']
# targy = ['a labdával', 'a fűben', 'a házban', 'a barátokkal']

# print(f"{random.choice(alany)} {random.choice(ige)} {random.choice(targy)}.")
# -----------------------------------------------------------------
# karakterek = string.ascii_letters + string.digits
# jelszo = "".join(random.choice(karakterek) for i in range(20))         # ez is új xd (de amúgy nem igazán részletezi a dolgokat)
# print(jelszo)
# # -----------------------------------------------------------------
# lista = ["kő", "papír", "olló"]
# gep = random.choice(lista)
# user = input("Válassz egyet: kő/papír/olló ")
# print(gep)
# if user == gep:
#     print("Döntetlen")
# if user == "kő" and gep == "olló" or user == "olló" and gep == "papír" or user == "papír" and gep == "kő":
#     print("Nyertél")
# else:
#     print("Vesztettél")
# -----------------------------------------------------------------
szamok = []                                 # be kell kérni számokat addig, amíg a lista nem lesz 15 hosszúságú, akkor evsszük fel a 
                                            # listába a számokat, ha a szám páros és 1 <= x <= 200
while len(szamok) < 15:
    print(f"A lista hosszúsága: {len(szamok)}.")
    szam = random.randint(1,200)
    if szam % 2 == 0:
        szamok.append(szam)
print(('; '.join(map(str, szamok))))
# -----------------------------------------------------------------

with open("numbers.txt", "w") as file:
    file.write('; '.join(map(str,szamok)))

fajl = open('data.txt', 'w') as file:
