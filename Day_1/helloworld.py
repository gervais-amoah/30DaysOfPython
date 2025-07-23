# Niveau 2
# Question 1
# Pour vérifier la version de Python, utilisez la commande ci-dessous dans votre terminal ou invite de commande.
# Windows: `python --version`
# Unix: `python3 --version`

# Question 2
print("Résultats des opérations arithmétiques entre 3 et 4:")
print("Addition:", 3 + 4)
print("Soustraction:", 3 - 4)
print("Multiplication:", 3 * 4)
print("Module:", 3 % 4)
print("Division:", 3 / 4)
print("Exponentielle:", 3**4)
print("Floor Division Operator:", 3 // 4)

# Question 3
print("\nAffichage de chaînes de caractères:")
print("Prénoms: Yao Gervais")
print("Nom de famille: Amoah")
print("Pays: Togo")
print("Phrase: Je profite de 30 jours de python")

# Question 4
print("\nTypes de données en Python:")
print(type(10))
print(type((9, 8)))  # Erreur si on fait type(9, 8)
print(type(3.14))
print(type(4 - 4j))
print(type(["Asabeneh", "Python", "Finlande"]))
print(type("Yao Gervais"))
print(type("Amoah"))
print(type("Togo"))

# Niveau 3
# Question 1
# Un exemple pour différents types de données Python
number0 = 3
number1 = 3.8
number2 = 5j
string0 = "un string"
boolean0 = True
list0 = [number0, number1, number2]
tuple0 = (number0, number2)
set0 = {number0, number2, number1}
dict0 = {"0": number0, "1": number1}

print("\nExemples de types de données:")
print("Nombres:", number0, number1, number2)
print("String:", string0)
print("Boolean:", boolean0)
print("List:", list0)
print("Tuple:", tuple0)
print("Set:", set0)
print("Dictionary:", dict0)

# Question 2
import math

distance_euclidienne = math.sqrt((2 - 10) ** 2 + (3 - 8) ** 2)
print(
    "\nDistance euclidienne entre les points (2, 3) et (10, 8) est:",
    distance_euclidienne,
)
