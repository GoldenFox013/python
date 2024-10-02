# # megad = False
# # while not megad:
# #     szemely = int(input("Hány személyre lesz a foglalás?(felnőtt) "))
# #     nap = input("Hány napra foglalna szállást? ")
# #     gyerek = int(input("Hány kiskorú lenne? "))

# #     if nap.isdigit():
# #         nap = int(nap)
# #         if nap > 0:
# #             if gyerek <= 2:
# #                 osszeg = (nap * szemely * 5000) - (gyerek * 700)
# #                 megad = True
# #             elif gyerek >= 3:
# #                 osszeg = (nap * szemely * 5000) - (gyerek * 1000)
# #                 megad = True
# #             elif gyerek == 0:
# #                 osszeg = nap * szemely * 5000
# #                 megad = True
# #         else:
# #             print("0-nál kisebb számot adtál meg.")
# #     else:("Nem számot adtál meg.")

# # print(f"A fizetendő összeg: {osszeg}Ft")
# # -------------------------------------------------------------------------------------------------
# # önálló feladat: virágok
# # 3 fajtát kell bekérni (kis-nagybetű, upper-lower fv.), hány szálat kér, addig kell írni, míg legalább egyet ír be
# # rózsa: 500, tuli: 400, liliom: 300
# # végösszeg

# # r = 500          # RTL xd
# # t = 400
# # l = 300          # utólag rájöttem, hogy nem kellett volna külön definiálni az árakat xdd (elég lett volna az összegnél beszorozni)

# # fajta = input("Milyen virágot kér?(rózsa - r, tulipán - t, liliom - l) ").upper()
# # db = input("Hány szálat kér? ")
# # while db.isdigit() == False or int(db) <= 0:                 # basically újrakérdezi, ha nem szám vagy nem pozitív az input
# #     print("Nem jó input.")
# #     db = input("Hány szálat kér? ")

# # db = int(db)

# # if fajta == "R":
# #     osszeg = db * r
# # elif fajta == "T":
# #     osszeg = db * t
# # else:
# #     osszeg = db * l

# # print(f"Végösszeg: {osszeg} Ft.")
# ------------------------------------------------------------------------------------------------------
# # tanárnő megoldása:
# # szam = False
# # while not szam:
# #     virag = input("Válassz egy virágot(R,T,L):").upper()
# #     db = int(input("Hány szál virágot szeretnél?"))

# #     if db.isdigit():
# #         db = int(db)
# #         if db > 0:
# #             if virag == "R":
# #                 osszeg = db * 500
# #                 szam = True
# #                 print(f"A fizetendő összeg: {osszeg} Ft.")
# #             elif virag == "T":
# #                 osszeg = db * 400
# #                 szam = True
# #                 print(f"A fizetendő összeg: {osszeg} Ft.")
# #             elif virag == "L":
# #                 osszeg = db * 300
# #                 szam = True
# #                 print(f"A fizetendő összeg: {osszeg} Ft.")
            
# #     else:
# #         print("Nem számot adtál meg.")
# --------------------------------------------------------------------------------------------
# ujabbosszeg = False
# shop = []
# while not ujabbosszeg:
#     termek = int(input("Add meg a termék összegét: "))
#     if termek > 0:
#         shop.append(termek)

#         valasz = input("Szeretnél-e terméket hozzáadni a listához? ").lower()
#         if valasz != "i":
#             ujabbosszeg = True

# tizezeralatt = []
# for i in shop:
#     if sum(tizezeralatt) + i < 10000:
#         tizezeralatt.append(i)

# print(f"A tizeteralatt lista osszege: {sum(tizezeralatt)} Ft")
# print(f"A megvásárolható termékek: {len(tizezeralatt)} db")

# print(f"A legnagyobb összeg: {max(shop)} Ft")
# print(f"A legkisegg összeg: {min(shop)} Ft")
# print(f"A lista elemeinek száma: {len(shop)} db")
# print(f"A lista tartalmának összege: {sum(shop)} Ft")
# ------------------------------------------------------------------------------------------------
# bevásárlások összegét kell eltárolni egy listában (lényegében ugyanaz. mint az előző)
# írasd ki a konzolra a termékek összegét, a legdrágábbat, a legolcsóbbat
# hány terméket tudnál venni 25k alatt?

# lista = []
# stop = False
# while stop == False:
#     ar = input("Ár: ")
#     if ar.isdigit():
#         ar = int(ar)
#         if ar > 0:
#             lista.append(ar)
#         else:
#             print("0-nál kisebb összeget írtál.")
#     else:
#         print("Nem számot adtál meg.")
#     if input("Folytatod?(i/n) ") != "i":
#         stop = True

# print(f"A lista összege: {sum(lista)} Ft.")
# print(f"A lista legdrágább eleme: {max(lista)} Ft.")
# print(f"A lista legolcsóbb eleme: {min(lista)} Ft.")
# huszon5kalatt = []
# for i in lista:
#     if sum(huszon5kalatt) + i < 25000:
#         huszon5kalatt.append(i)
# print(f"{len(huszon5kalatt)} db terméket tudnánk venni 25k alatt.")

# githubon van fenn nála a "Random" nevű mappában a random számgeneráláshoz anyag
# azt mondta, hogy jövőhéten veszünk fájlbeolvasást és írást

# ---------------------------------------- Random -----------------------------------------------
import random

nyert = False
while nyert == False:
    gep = random.randint(1,5)
    szam = int(input("Adj meg egy számot 1-5ig: "))

    if gep > szam:
        print("Kisebb számot adtál meg.")
    elif gep < szam:
        print("Nagyobb számot adtál meg.")
    elif gep == szam:
        print("Nyertél.")
        nyert = True

print(f"A gép által megadott szám {gep}, szam: {szam}")

