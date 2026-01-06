import os

filename = "data.txt"

if os.path.exists(filename):
    print("Plik już istnieje")
else:
    with open(filename, "w") as f:
        f.write("Jakieś początkowe dane\n")
    print("Plik utworzony i dane zapisane")