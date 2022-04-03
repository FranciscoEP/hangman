import random
import os
from time import sleep
def dibujo_hangman(oportunidad):
    hangman={
  0:'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
 1:       
'''
 +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
        
   2:'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
     3:   '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
  4:'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
    5:    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
        6:'''
  
  +---+
  |   |
      |
      |
      |
      |
=========''',
7:'''
  +---+
      |
      |
      |
      |
      |
=========
''',
8:'''
      |
      |
      |
      |
      |
=========
''',
9:""" 
      
      
      
      
=========""",
10:""
    }
        

    return print(hangman[oportunidad])

def limpiar_pantalla():
    if os.name == 'posix':
        return os.system('clear')
    else:
        return os.system('cls')

def sin_acentos(palabra):
    '''
    La funcion sin_acentos regresa una palabra sin tildes que anteriormente contenia
    tildes. 
    '''
    vocales = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u"}
    normalizador = str.maketrans(vocales)
    return palabra.translate(normalizador)

def leer_archivo():
    '''
    por definir
    '''
    with open("./words.txt", "r", encoding="utf-8") as file:
        lista_palabras= [sin_acentos(i.strip().lower()) for i in file]
        lista_nivel={'facil': [i for i in lista_palabras if len(i)<7],
                     'medio': [i for i in lista_palabras if 9>len(i)>7],
                     'dificil': [i for i in lista_palabras if len(i)>9]
                    }
        return(lista_nivel)        

        
def selecciona_palabra(n):
    '''
   Selecciona_palabra es una funcion que tiene como parametro la dificultad de la funcion 
   inicio, y dependiendo el valor ingresado tomara una palabra aleatoria de una BD y 
   escondera todas las letras que conforman a esa palabra. 
    
   Las letras se iran descubriendo si el usuario logra teclear aquella que pertenezca
   a la palabra, si hay mas de dos letras iguales en la palabra, la funcion lograra
   aparecer todas sin necesidad de introducir un nuevo registro.
    
   Caso contrario, si el usuario no logra introducir una letra que pertenezca, las opor-
   tunidades que tiene iran disminuyendo hasta que pierda el juego. 
    
    '''
    lectura= leer_archivo()
    
    if n==1:
        palabra= random.choice(lectura['facil'])
        descubierto=[' ? ' for i in palabra ]
        
    if n==2:
        palabra= random.choice(lectura['medio'])
        descubierto=[' ? ' for i in palabra ]
             
    if n==3:
        palabra= random.choice(lectura['dificil'])
        descubierto=[' ? ' for i in palabra ]
        


    oportunidades= 10
    while oportunidades > 0:
        if palabra == "".join(descubierto).lower():
            print("""

██╗ ██╗░░██╗░█████╗░░██████╗  ░██████╗░░█████╗░███╗░░██╗░█████╗░██████╗░░█████╗░██╗
╚═╝ ██║░░██║██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗██║
██╗ ███████║███████║╚█████╗░  ██║░░██╗░███████║██╔██╗██║███████║██║░░██║██║░░██║██║
██║ ██╔══██║██╔══██║░╚═══██╗  ██║░░╚██╗██╔══██║██║╚████║██╔══██║██║░░██║██║░░██║╚═╝
██║ ██║░░██║██║░░██║██████╔╝  ╚██████╔╝██║░░██║██║░╚███║██║░░██║██████╔╝╚█████╔╝██╗
╚═╝ ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝
""")
            return print('la palabra es:', palabra)
        print(descubierto, "---", len(palabra), "letras,", oportunidades, 'vidas\n')
        dibujo_hangman(oportunidades)
        letra = input("Adivina la palabra, ingrese un caracter válido: ").lower()   

        if letra not in palabra and letra.isalpha() and len(letra) == 1:
                limpiar_pantalla()
                oportunidades-=1
                print ('La letra',letra,'no pertenece a la palabra. Aun tienes', oportunidades, 'oportunidades más') 

        if letra.isalpha() and len(letra) == 1:
            for indice in range(len(palabra)):
                if letra == palabra[indice]:
                    descubierto[indice]=letra.upper()
                    limpiar_pantalla()
        else:
            print("Opcion no valida: has ingresado un caracter no valido, intenta de nuevo")
    else:
        dibujo_hangman(oportunidades)
        return print(f"Perdiste, la palabra era: {palabra}")

Intrucciones= """
Instrucciones: seleccione un nivel para jugar.
1. Fácil (4 - 6 letras)
2. Medio (7 - 9 letras)
3. Dificil (10+ letras)
              """    
def inicio():
    '''
    por definir
    
    '''
    
    
    logo = """
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
"""
    print(logo)
    print(Intrucciones)
    try: 
        nivel= int(input("\n\nEscoge tu nivel ")) 
        if nivel==1 or nivel==2 or nivel==3:
            return selecciona_palabra(nivel)
        else:
            raise ValueError
        #if nivel!=1 or nivel!=2 or nivel!=3 or nivel==str:
            #print('el valor ingresado no es correcto. Intenta de nuevo')
            #return inicio()
    except ValueError:
        print('el valor ingresado no es correcto. Intenta de nuevo')
        return inicio()
inicio()