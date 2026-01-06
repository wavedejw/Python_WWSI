# Prosty program kalkulatora

# Dodawanie dwóch liczb
def add(a, b):
    return a + b

# Odejmowanie dwóch liczb
def subtract(a, b):
    return a - b

# Mnożenie dwóch liczb
def multiply(a, b):
    return a * b

# Dzielenie dwóch liczb
def divide(a, b):
    if b == 0:
        return "Błąd: dzielenie przez zero!"
    return a / b


# Lista operacji
print("Proszę wybrać operację.")
print("a. Dodawanie")
print("b. Odejmowanie")
print("c. Mnożenie")
print("d. Dzielenie")

# Wybór operacji
op = input("Proszę wybrać operację (a/ b/ c/ d): ")

# Wpisywanie dwóch liczb
num1 = float(input("Wpisz pierwszą liczbę: "))
num2 = float(input("Wpisz drugą liczbę: "))

# Logiki określonych operacji
if op == 'a':
    print("Wynik:", add(num1, num2))

elif op == 'b':
    print("Wynik:", subtract(num1, num2))

elif op == 'c':
    print("Wynik:", multiply(num1, num2))

elif op == 'd':
    print("Wynik:", divide(num1, num2))

# Wybór opercaji, która nie jest dostępna
else:
    print("Operacja niedostępna. Proszę wybrać dostępną operację.")