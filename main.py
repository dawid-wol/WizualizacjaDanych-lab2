#Zad1
sporty = ["pilkanozna","siatkowka","koszykowka"]
print(sporty)
list.reverse(sporty)
print(sporty)
sporty.append("wioslarstwo")
sporty.append("skokwdal")
print(sporty)

#Zad2
slownik = {}
slownik["wyd."] = "wydanie"
slownik["t."] = "tom"
slownik["red."] = "redakcja"
slownik["oprac."] = "opracowanie"
slownik["tlum."] = "tlumaczenie"
print(slownik)

#Zad3
gry = {
    "GTAV" : "Grand Theft Auto V",
    "CSGO" : "Counter Strike Global Offensive",
    "MC" : "Minecraft",
    "LOL" : "League of Legends",
    "WOW" : "World of Warcraft",
    "W3" : "The Witcher 3"
}
ilosc = len(gry)
print(ilosc)

#Zad4
zdanie = input("Wpisz zdanie:")
print(zdanie)
litera_a = 0
for char in zdanie:
    char = char.lower()
    if char == "a":
        litera_a+=1
print("Litera a występuje ", litera_a, "razy")

#Zad5