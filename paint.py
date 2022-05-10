"""
Actividad 4: Juego de Pintado 

Equipo 9:
Christopher Gabriel Pedraza Pohlenz A01177767
Kevin Susej Garza Aragón A00833985
Eugenia Ruiz Velasco Olvera A01177887
"""


# Se importan las librerías de turtle y freegames
from turtle import *
import turtle as t

from freegames import vector


# Función para dibujar una linea
# Recibe: la pos inicial y final
def line(start, end):
    up() # levanta la pluma (deja de dibujar)
    goto(start.x, start.y) # mueve el puntero (pluma) a la posición inicial (donde se presíonó)
    down() # baja la pluma (empieza a dibujar)
    goto(end.x, end.y) # se mueve a la posición final (el segundo click)


# Función para dibujar un cuadrado
# Recibe: la pos inicial y final
def square(start, end):
    up() # deja de dibujar
    goto(start.x, start.y) # mueve el puntero a la pos inicial
    down() # empieza a dibujar
    begin_fill() # empieza a rellenar lo que se dibuje

    # Ciclo por cada lado del cuadrado (4)
    for count in range(4):
        # Se mueve al frente y luego gira 90 grados para hacer cada lado del cuadrado
        forward(end.x - start.x)
        left(90)

    # deja de rellanar la figura
    end_fill()


# Función para dibujar un círculo
# Recibe: la pos inicial y final
def circle(start, end):
    pass  # TODO


# Función para dibujar un rectángulo
# Recibe: la pos inicial y final
def rectangle(start, end):
    up() # deja de dibujar
    goto(start.x, start.y) # mueve el puntero a la pos inicial
    down() # empieza a dibujar
    begin_fill() # se rellena la figura que se dibuja

    # El rectangulo tiene pares de lados iguales por lo que el ciclo es de 2
    for count in range(2):
        # Se mueve hacia delante, gira 90 grados, se vuelve a mover hacia delante, y gira nuevamente para hacer 2 lados
        forward(end.x - start.x)
        left(90)
        forward(end.x + start.x)
        left(90)

    # deja de dibujar el rectángulo
    end_fill()


# Función para dibujar un triángulo
# Recibe: la pos inicial y final
def triangle(start, end):
    up() # deja de dibujar
    goto(start.x, start.y) # mueve el puntero a la pos inicial
    down() # empieza a dibujar nuevamente
    begin_fill() # comienza a rellenar la figura

    # ciclo por cada uno de los 3 lados del triángulo
    for count in range(3):
        # Se mueve una cantidad al frente y gira 120 grados para hacer un triángulo equilatero
        forward(end.x - start.x)
        left(120)

    # deja de rellenar la figura
    end_fill()


# Función que se llama cada vez que se da un click en la pantalla
# Recibe: la pos horizontal y vertical del click
def tap(x, y):
    # guarda la posición incial guardada en el diccionario
    start = state['start']

    # si la posición está vacía (significando que se trata de una pos inicial y no final)
    if start is None:
        # guarda en el diccionario un vector de la posición
        state['start'] = vector(x, y)
    else: # si NO está vacía
        # toma la forma seleccionada del diccionario
        shape = state['shape']
        # guarda la posición final (el diccionario ya dio la inicial)
        end = vector(x, y)
        # se pasan las coordenadas a la función de la figura seleccionada
        shape(start, end)
        # se cambia la pos inicial del diccionario 
        state['start'] = None


# Función para guardar el valor de la tecla presionada con respecto a la figura
def store(key, value):
    # se guarda el valor de la figura con la llave 'shape'
    state[key] = value


# Se crea diccionario de la posición y figura por defecto
state = {'start': None, 'shape': line}
# Asigna el tamaño y posición de la ventana
setup(420, 420, 370, 0)
# Cuando se hace click en la pantalla se llama a la función tap
onscreenclick(tap)
# Empieza a "escuchar" las teclas que se presionan
listen()
# onkey(func, key) une una función a una tecla, para que se llame a esta cuando se presiona la tecla
onkey(undo, 'u')
# Teclas para cambiar el color del puntero y líneas
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple3'), 'P')
# Teclas para cambiar la figura
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
# Comienza el ciclo de eventos
done()