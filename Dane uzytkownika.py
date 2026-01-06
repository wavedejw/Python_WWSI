name = input("Podaj swoje imię: ")
age = input("Podaj swój wiek: ")

with open("user.txt", "w", encoding="utf-8") as file:
    file.write(f"Imię: {name}  Wiek: {age}")