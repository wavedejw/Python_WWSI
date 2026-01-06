# Utwórz zmienne "vowels" i "consonants" i przypisz każdej z nich wartość 0

vowels = 0
consonants = 0

# Utwórz pętlę i przeiteruj łańcuch znaków „Programowanie Pythona”

text = "Programowanie Pythona"


# Utwórz instrukcję warunkową IF-ELSE, wyliczającą liczbę samogłosek i spółgłosek w  łańcuchu znaków

for char in text.lower():
    if char.isalpha():
        if char in "aeiouyąę":
            vowels += 1
        else:
            consonants += 1
    
    
# Wydrukuj łączną liczbę samogłosek i spółgłosek w  łańcuchu znaków

print("Liczba samogłosek:", vowels)
print("Liczba spółgłosek:", consonants)