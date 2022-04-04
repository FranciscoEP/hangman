
# Proyecto Hangman (Ahorcado)
<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

- *Daniel Ramírez*.
- *Francisco Ponce*.

*[Data Analytics, México & 4 de abril 2022]*

## Contenido


- [Introducción](#introducción)
- [Flujo de trabajo](#flujo-de-trabajo)
- [Contenido del repositorio](#contenido-del-repositorio)
- [Links](#links)


## Introducción

Hangman (“ahorcado”) es un juego para dos personas donde la meta de un jugador (J1) es adivinar la palabra que 
ha pensado el otro jugador(J2). La palabra pensada ha sido expresada por medio de guiones bajos que en cantidad 
son las mismas que conforman la palabra pensada(ej. una palabra de 6 letras tendrá 6 guiones bajos).
   El juego se desarrolla mientras el jugador J1 va dictando la letra que cree esta contenida en la palabra y, 
si se encuentra, el jugador J2 ocupará los guiones como posiciones donde se encuentra la letra dictada. 
   Si la letra dictada no se encuentra en la palabra, el jugador J2 empezara a dibujar por partes la silueta de
un hombre ahorcado, empezando por la columna y terminando con la cabeza, las partes estan descritas en el pseudo-
código que está en el repositorio.

En este programa, el jugador J1 esta representado por el usuario y el jugador J2 por el programa. El usuario en 
cada juego tendrá 10 intentos para completar todas las letras que conforman a la palabra por medio de entrada por
teclado. No se admiten caracteres numéricos, espacios ni signos ortográficos, únicamente las letras del abeceda-
rio son admisibles. El usuario gana la partida si logra coincidir las letras que ingresó contra las que conforman
la palabra antes de terminarse la cantidad de oportunidades que tiene por cada juego. 


## Flujo de trabajo

Hangman es un juego donde la entrada por teclado definió el camino por el cual ibamos a codificar. Para esto, inicia-
mos con una función que recibiera alguno de los 3 niveles de dificultad. El manejo de errores comienza a partir de
esta función para que no se rompiera al seleccionar una letra, un simbolo, dos número, entre cualquier otra opción
que no fueran ya sea 1 para fácil, 2 para medio y 3 para difícil. 

Una vez definido el nivel, con listas de prueba empezamos a importar palabras en la siguiente función para que pudiera
ser leída en longitud y ser retornada a partir de la dificultad seleccionada anteriormente, además de poder  ser impre-
sa como guiones bajos donde iban a ser reemplazadas por la letra correcta en su posición original. Esta función, al igual
que la anterior, recibiria por teclado la elección de la letra del usuario, por lo que se definieron lineas de codigo
para que no pudieran ingresarse números, mas de dos letras con numeros, entre cualquier otro caracter que no fuera una sola
letra como ingreso. 

La disminución de las oportunidades fue importante ya que durante el proyecto la disminución podía no ser leída durante la
ejecucuión del programa o inclusive terminarse las "vidas" sin haberse ingresado ninguna letra. Además , en el programa se hicieron arreglos para poder igualar la cantidad de letras con la entrada correcta por el usuario, para que pudiera terminar
el programa si el usuario registraba todas las letras correctas o terminaba sus oportunidades. 




## Contenido del repositorio

El repositorio cuenta con el proyecto en formato .ipynb y en formato .py, este último es el que se usará como el
ejecutable del programa. También contiene el archivo de texto que surte las palabras para que se desarrolle el juego.
Además del diagrama de flujo por el cual nos basamos para elaborar el proyecto.
Las carpeta Legacy_code contiene el código que se hizo previamente antes de llegar al nuestro código final, mientras que la
carpeta .ipynb_checkpoints contiene todas las modificaciones realizadas durante el proyecto. 


## Links

[Flujo de trabajo](https://lucid.app/lucidchart/471bc5f8-297c-42c7-8860-0945a2a78e9f/edit?invitationId=inv_14efcd87-82ca-4f84-afba-86d20796dbb7&referringApp=slack#)  
[Pseudocódigo](https://docs.google.com/document/d/1OX07BruAEH_KtiHDkboYBDaLUfI2RaPXt6fCERQ9p0U/edit)  
[Slides](https://docs.google.com/presentation/d/1XxSIoisNOwXswloXvkFB2z95bezzJsN8Cwmb8ulH2Xs/edit?usp=sharing)  


























