# def hello(user_name = "nobody"):
#     print("Hello " + user_name + "!")

# def parose(n):
#     if n % 2 == 0:
#         print("Páros.")
#     else:
#         print("Páratlan.")

# hello("Maja")

# parose(5)
# parose(4)

# def sorter(*args):
#     newlist = list(args)              # erre csak pluszban rákérdeztem, ez tetszőleges számú változót elfogad

#     newlist.sort()
#     print(newlist)

# sorter(5, 4, 6, 2, 1)
    
def kokatenal(szoveg1, szoveg2):
    return szoveg1 + " " + szoveg2

valtozo = kokatenal("kutya", "macska")
print(valtozo)
print(len(valtozo))

def lowertoupper(anystring):
    temp = ""
    for betu in anystring:
        if betu.islower():
            temp += betu.upper()
        else:
            temp += betu.lower()
    
    return temp

print(lowertoupper("kuTya"))
