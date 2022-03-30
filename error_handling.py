from locale import normalize
import random

logo =  """
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

Made by Daniel Ramírez and Francisco Ponce
"""
instructions ="""
Instrucciones: seleccione un nivel para jugar.

1. Fácil (4 - 6 letras)
2. Medio (7 - 9 letras)
3. Dificil (10+ letras)
"""

def normalize_vowels(word):
    # https://stackoverflow.com/questions/65833714/how-to-remove-accents-from-a-string-in-python
    vowels = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u"}
    normalize = str.maketrans(vowels)
    return word.translate(normalize)

def read_csv():
    with open("./words.txt", "r", encoding="utf-8") as file:
        words=[(normalize_vowels(word).lower().strip()) for word in file]
        return {"easy": [word for word in words if len(word) < 7],
                "medium":[word for word in words if len(word) < 10],
                "hard": [word for word in words if len(word)>=  10]
                }

words = read_csv()

def choose_level():
    try:
        level = int(input("Seleccione un nivel: "))
        if level == 1:
            return random.choice(words["easy"])
        elif level == 2:
            return random.choice(words["medium"])
        elif level == 3:
            return random.choice(words["hard"])
        else:
            print(instructions)
            print("Opción no válida: has ingresado un caracter no válido, intenta de nuevo")
            return choose_level()
    except ValueError:
        print("Opción no válida: has ingresado un caracter no válido, intenta de nuevo")
        print(instructions)
        return choose_level()

# def game_logic(letter, word):
#     if letter in word:
#         return True
#     else:
#         return False
def run():
    print(logo)
    print(instructions)
    word = choose_level()
    hide_word = len(word) * "_ "
    lifes = 10
    print(f"{hide_word} -- {len(word)} letras")
    
    while lifes > 0:
        new_word = [] 
        print(f"{new_word}")
        print(f"{lifes} vidas")
        letter = input("""Adivina la palabra, ingrese un caracter válido:""")

    # https://www.programiz.com/python-programming/methods/string/isalpha
        if letter.isalpha() and len(letter) == 1:
            print(word)
            # print(new_word)
            
        else:
            print("Opción no válida: has ingresado un caracter no válido, intenta de nuevo")
            continue
    # select_word = random.choice(read_csv())
    # print(select_word)

if __name__ == '__main__':
    run()
