people = {
    "szgergo" :  "Szkiva Gergő",
    "gyadam" : "Györgyi Ádám",
    "bmaja" : "Borók Maja",
    "tmartin" : "Tőkés Martin",
    "svivien" : "Sánta Vivien"      # tranziens memória
}

people.popitem()
people.popitem()
people.popitem()

for key, value in people.items():
    print(key, value)

# person = "gyadam"
# print(people[person])
# howmany = len(people)
# print(howmany)

# print("asd" in people) #False
# print("gyadam" in people) #True
# peopleName = "asd"

# if peopleName in people:
#     print(people[peopleName])
# else:
#     print("Nincs ilyen személy a szótárunkban.")

# print(people.get(peopleName, "Nincs ilyen személy a szótárunkban."))

# people['bmaja'] = "Nagy Borók Maja"
# people.update({"bmaja" : "Nagy Borók Maja"})
# print(people.get("bmaja"))

# people.update({"redavid" : "Rédai Dávid"})

# print(len(people))
# print(people)
