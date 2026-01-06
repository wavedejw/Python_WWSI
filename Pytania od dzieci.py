import random

# Lista pytań, które często zadają dzieci
questions = [
    "Dlaczego gwiazdy świecą?",
    "Czemu deszcz pada z chmur?",
    "Dlaczego ptaki potrafią latać?",
    "Skąd się bierze wiatr?",
    "Dlaczego ogień jest gorący?",
    "Czemu księżyc zmienia kształt?",
    "Dlaczego muszę jeść warzywa?",
    "Jak ryby oddychają pod wodą?",
]

# Hasło kończące program
stop_phrase = "to wszystko"

print(" Ciekawskie dziecko zaczyna zadawać pytania!")
print(f"(Aby zakończyć, wpisz: {stop_phrase})\n")

answer = ""

while answer != stop_phrase:
    # Losowe pytanie
    question = random.choice(questions)

    # Pobranie odpowiedzi od użytkownika
    answer = input(f"Dziecko: {question}\nRodzic: ").strip().lower()

    # Jeśli to nie jest hasło kończące — dziecko pyta dalej
    if answer != stop_phrase:
        print("Dziecko: Dlaczego?\n")

print("\nDziecko: Okej, to już wszystko! ")