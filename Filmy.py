# Utwórz słownik filmów. Klucz: nazwa filmu, wartości: [kryterium_wiekowe, liczba_biletów]
movies = {
    "Harry Potter": [10, 5],
    "Avengers": [12, 7],
    "Joker": [18, 3],
    "Minions": [5, 9]
}

# Utwórz pętlę, która będzie działać w nieskończoność
while True:

    # Pobierz tytuł filmu od użytkownika, usuń spacje i zamień na format tytułowy
    title = input("Podaj tytuł filmu (lub wpisz 'koniec' aby zakończyć): ").strip().title()

    if title.lower() == "koniec":
        print("Zakończono program.")
        break

    # Jeśli wybrany film jest dostępny w słowniku, kontynuuj
    if title in movies:

        # Zapytaj użytkownika o wiek
        age_str = input("Podaj swój wiek: ").strip()

        # Sprawdzenie czy da się zamienić na liczbę
        if not age_str.isdigit():
            print("Wiek musi być liczbą!\n")
            continue

        age = int(age_str)

        # Sprawdź użytkownika pod kątem kwalifikowalności
        required_age = movies[title][0]
        available_tickets = movies[title][1]

        if age >= required_age:

            # Jeśli użytkownik w grupie docelowej, sprawdź dostępność miejsc
            if available_tickets > 0:

                # Jeśli liczba miejsc dodatnia, zmniejsz pulę o 1
                movies[title][1] -= 1
                print(f" Rezerwacja udana! Zostało biletów na '{title}': {movies[title][1]}\n")

            else:
                print(f" Brak dostępnych biletów na '{title}'.\n")

        else:
            print(f" Masz {age} lat, a film '{title}' jest od {required_age} lat.\n")

    else:
        print(" Nie mamy takiego filmu w repertuarze.\n")
        print("Dostępne filmy:", ", ".join(movies.keys()), "\n")