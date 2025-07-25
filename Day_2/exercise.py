age = 27
height = 1.6
complex_number = 3 + 4j


def task_4():
    base = input("Entrez la base du triangle: ")
    height = input("Entrez la hauteur du triangle: ")
    area = 0.5 * float(base) * float(height)
    print(f"L'aire du triangle est: {area}")


def task_5():
    sideA = input("Entrez le côté A: ")
    sideB = input("Entrez le côté B: ")
    sideC = input("Entrez le côté C: ")
    perimeter = float(sideA) + float(sideB) + float(sideC)
    print(f"Le périmètre du triangle est: {perimeter}")


def task_6_1():
    length = input("Entrez la longueur du rectangle: ")
    width = input("Entrez la largeur du rectangle: ")
    perimeter = 2 * (float(length) + float(width))
    print(f"Le périmètre du rectangle est: {perimeter}")


def task_6_2():
    length = input("Entrez la longueur du rectangle: ")
    width = input("Entrez la largeur du rectangle: ")
    area = float(length) * float(width)
    print(f"L'aire du rectangle est: {area}")


def task_14():
    phrase = "I hope this course is not full of jargon."
    if "jargon" in phrase:
        print("La phrase contient le mot 'jargon'.")


if __name__ == "__main__":
    print("Bienvenue dans l'exercice de Python!")

    # Calcul de l'aire du triangle
    task_4()

    # Calcul du périmètre du triangle
    task_5()

    # Calcul du périmètre du rectangle
    task_6_1()

    # Calcul de l'aire du rectangle
    task_6_2()

    # Utilisation de la fonction pour vérifier la présence du mot "jargon"
    task_14()

    print("\nFin de l'exercice.")
