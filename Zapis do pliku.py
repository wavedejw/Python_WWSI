words = ["jabłko", "banan", "wiśnia"]

with open("fruits.txt", "w", encoding="utf-8") as plik:
    for slowo in words:
        plik.write(slowo + "\n")

print("Zapisano listę do pliku fruits.txt")