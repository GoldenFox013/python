with open("gombak.txt", "r", encoding = "UTF-8") as fajl:
    elsosor = fajl.readline()               # ez beolvassa az első sort és tárolja, így később nem lesz útban

    gombak = []                             # üres tömb, ahova a gombákat pakoljuk majd
    for sor in fajl:                        # a fájl minden során átfut
        adatok = sor.strip().split("@")     # ez megcsupaszítja a sorokat, aztán a @ mentén szétválasztja elemekre, és azok listaként az adatok változóba kerülnek
        gombak.append(adatok)               # a gombak lista minden eleme mégegy lista (adatok), ez később fontos

def gombak_szama(lista):                    # a gombak_szama függvény majd meghíváskor a zárójelben egy változót kap, ezt itt listának neveztük el
    print(f"A gombák száma: {len(lista)}")  # itt csak kiírjuk a megadott lista hosszát (ez majd a gomba lesz)

gombak_szama(gombak)                        # itt meghívjuk a függvényt és megadjuk neki a már telepakolt gombak listánkat

# a C feladat azért érdekes, mert azt mondta órán, hogy listákkal dolgozzunk class helyett (ha jól emlékszem)
# így viszont egy olyan módszert kell alkalmazni (szerintem), amit még nem tanultunk
# a net valszeg szebben elmagyarázza: mátrix / listák listája (ez más progis nyelvben kétdimenziós tömb)
# lehet a tanárnő majd mutat más megoldást, nekem hirtelen ez tűnt ésszerűnek, mint módszer
# a legnagyobb lényeg, hogy így hivatkozunk egy értékére:
# jelen esetben pl.: gombak[0][2]
# ez a gombak első sorának harmadik adata, kinda mint egy táblázat (én így szoktam vizualizálni)

def papsapka(lista):
    for i in range(len(lista)):             # itt a for ciklusban jobb index-szel dolgozni (könnyebb hivatkozni a gomba egyes elemeire)
        if lista[i][1] == "papsapkagombák ": # itt az első papsapkagombák előfordulásánál "belép" az if-es elágazódásba és az ottani dolgokat végre fogja hajtani
            print(f"Az első papsapkagomba neve: {lista[i][0]}") # ha egyezés van, kiírja az adott indexű sor első elemét, ami itt maga a gomba neve
            break                           # a break meg fogja törni a ciklust az első találat kiírása után, így a függvénynek nem lesz további teendője
# funfact itt az egészben, hogy naon fura a forrásfájl, így vannak üres és hiányos sorok, itt pl a papsapkagombák után kell egy szóköz, mert a forrásfájlban az összes úgy van beírva xdd
papsapka(gombak)

def tinoru(lista):
    db = 0                                  # számláló, majd ehhez adunk hozzá, ha találunk egyezést
    for i in range(len(gombak)):
        if gombak[i][1] == "tinóru":        # hasonlóképp, mint az előzőnél: ha a gomba i-edik sorának második eleme (azaz a nemzettség) megegyezik, belép az elágazásba (if)
            db += 1                         # a számlálót növeljük egyezéskor
    print(f"A tinóru gombák száma: {db}")

tinoru(gombak)

# asszem ennyi, sry ha valamit nem jól írtam vagy félrebeszéltem, nemigen tudok magyarázni xdd