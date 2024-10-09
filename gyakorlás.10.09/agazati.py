# print("1. feladat: Kisebb-nagyobb meghatározása")
# a = int(input("Kérem az első számot: "))
# b = int(input("Kérem a második számot: "))

# if a > b:
#     print(f"A nagyobb szám {a}, a kisebb {b}.")
# elif b > a:
#     print(f"A nagyobb szám {b}, a kisebb {a}.")
# else:
#     print("A két szám egyenlő.")
# ---------------------------------------------------
print("2. feladat: szökőév listáző")            # bekér 2 évszámot, és az évszámokon belül (beleértve a kettő számot is) kiírja az összes 
                                                # szökőévet (vagy 400-zal osztható, vagy 4-gyel osztható de 100-zal nem)
a = int(input("Kérem az első évszámot: "))
b = int(input("Kérem a második évszámot: "))
evek = []

for i in range(a,b+1):
    if i % 4 == 0 and i % 100 != 0:
        evek.append(i)
    elif  i % 400 == 0:
        evek.append(i)

if len(evek) == 0:
    print("Nincs szökőév a megadott tartományban.")
else:
    print(f"Szökőévek: {'; '.join(map(str,evek))}")         # ez új
