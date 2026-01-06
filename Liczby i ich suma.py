try:
    with open('numbers.txt', 'r') as plik_zrodlowy:
        tresc = plik_zrodlowy.read()

    with open('copy.txt', 'w') as plik_docelowy:
        plik_docelowy.write(tresc)

    print("Sukces: Zawartość pliku została skopiowana do 'copy.txt'.")

except FileNotFoundError:
    print("Błąd: Plik 'numbers.txt' nie istnieje. Uruchom najpierw poprzednie zadanie, aby go utworzyć.")