import random

#print(random.randint(1,10))     minden egyes futtatásnál egy másik számot generál

counter = 0

while counter < 10:
    print(random.randint(1,10))     #ez kiír 10db random számot 1-9ig
    counter += 1

lista = ["a", "b", "c", "d", "e"]
counter = 0
while counter < 10:
    print(lista[random.randint(0,len(lista)-1)], end=" ")    #ez 10szer választ egy random listaelemet és kiírja
    counter += 1

counter = 0
while counter < 10:
    betu = lista[random.randint(0,len(lista)-1)]    #ez is 10szer választ egy random listaelemet és kiírja, de ha talál egy bizonyos petűt 
    counter += 1                                    #pl "e", akkor kilép a ciklusból
    if betu == "e":
        print("e betű, kiléptem")
        break
    else:
        print(betu)