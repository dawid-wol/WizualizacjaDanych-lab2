import math

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
print("Litera a występuje ", litera_a, " razy")

#Zad5

#Zad6
print("Podaj trzy liczby:")
x = int(input())
y = int(input())
z = int(input())
najwieksza = 0
if x > y and x > z:
    najwieksza = x
else:
    if y > z:
        najwieksza = y
    else:
        najwieksza = z

print("najwieksza to: ", najwieksza)

#zad7
liczby = [2, 7.2, 8.4, 6, 5]
idx = 0
for x in liczby:
    liczby[idx] = x ** 2
    idx += 1

print(liczby)

#Zad8
print("Podaj 10 liczb:")
i = 0
lista = []
while i < 10:
    a = int(input())
    i += 1
    if a % 2 == 0 :
        lista.append(a)
print(lista)

#9

#10
print("Oblicz pierwiastek z: ")
e = float(input())
if e < 0:
    print("liczba ujemna pierwiastek nie istnieje")
else:
    wynik = math.sqrt(e)
    print(wynik)
