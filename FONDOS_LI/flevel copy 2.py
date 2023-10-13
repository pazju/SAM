import pygame 
import sys  
import math # Redondear
import time # Permite generar un loop durante un timpo establecido (Para que las tarjetas se volteen solas de nuevo si están mal)
import random # Permite que las tarjetas salgan siempre en forma aleatoria

"""
Inicializar las librerias de Pygame para configurar sonido, fuentes  pantalla
"""
pygame.init()
pygame.font.init() # Inicializar fuentes a utilizar
pygame.mixer.init() # Inicializar el mezclador porque se van a utilizar sonidos

"""
Funciones y variables globales
"""
#Ajuste de la pantalla
info = pygame.display.Info()
screen_width, screenheight = info.current_w, info.current_h
print(screen_width, screenheight)


altura_boton = 90  # El botón de abajo, para iniciar juego
medida_cuadro = 384  # Medida de la imagen en pixeles
medida_cuadro_h = screen_width/5  # Medida de la imagen en pixeles
medida_cuadro_v = screenheight/2  # Medida de la imagen en pixeles
# Imagen cuando la figura está oculta
tarjeta_oculta = "F_LEVEL/oculta.png"
imagen_oculta = pygame.image.load(tarjeta_oculta)
segundos_mostrar_pieza = 2  # Segundos para ocultar la pieza si no es la correcta
"""
Una clase que representa el cuadro. El mismo tiene una imagen y puede estar
descubierto (cuando ya lo han descubierto anteriormente y no es la tarjeta buscada actualmente)
o puede estar mostrado (cuando se voltea la imagen)
También tiene una fuente o nombre de imagen que servirá para compararlo más tarde
"""
# Colores de las letras y boton
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)
color_gris = (206, 206, 206)
color_azul = (30, 136, 229)

# CRONOMETRO

timer_font = pygame.font.SysFont("adobedevanagaribold", 30)
level_time = 8 # 2 minutes
timer_text = timer_font.render(str(level_time), True, color_blanco)
timer_event = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
pygame.time.set_timer(timer_event, 1000) # set_timer crea una acción cada 1s

# Errores
error_1 = 0 
# Esta clase representa el cuadro de la tarjeta
class Cuadro:
    def __init__(self, fuente_imagen):
        self.mostrar = True
        self.descubierto = False
        """
        Una cosa es la fuente de la imagen (es decir, el nombre del archivo) y otra
        la imagen lista para ser pintada por PyGame
        La fuente la necesitamos para más tarde, comparar las tarjetas
        """
        self.fuente_imagen = fuente_imagen # Fuente: nombre de la img. para hacer la comparación
        self.imagen_real = pygame.image.load(fuente_imagen) # imagen 


"""
Todo el juego; que al final es un arreglo de objetos
"""
# Matriz de arreglos, esta es la estructura general del juego, la cantidad de parejas que se quieren y demás
"""cuadros = [
    [Cuadro("F_LEVEL/agua.png"), Cuadro("F_LEVEL/hilo.png"), Cuadro("F_LEVEL/cepillo.png"), Cuadro("F_LEVEL/enjuague.png"),Cuadro("F_LEVEL/crema.png")],
    [Cuadro("F_LEVEL/agua.png"), Cuadro("F_LEVEL/hilo.png"), Cuadro("F_LEVEL/cepillo.png"), Cuadro("F_LEVEL/enjuague.png"),Cuadro("F_LEVEL/crema.png")],  
]"""

cuadros = [
    [Cuadro("F_LEVEL/crema.png"), Cuadro("F_LEVEL/agua.png"), Cuadro("F_LEVEL/crema.png"), Cuadro("F_LEVEL/enjuague.png"),Cuadro("F_LEVEL/cepillo.png")],
    [Cuadro("F_LEVEL/hilo.png"), Cuadro("F_LEVEL/agua.png"), Cuadro("F_LEVEL/hilo.png"), Cuadro("F_LEVEL/cepillo.png"),Cuadro("F_LEVEL/enjuague.png")],  
]



# Los sonidos a utilizar
sonido_fondo = pygame.mixer.Sound("F_LEVEL/fondo.wav")
sonido_clic = pygame.mixer.Sound("F_LEVEL/clic.mp3")
sonido_exito = pygame.mixer.Sound("F_LEVEL/ganador.mp3")
sonido_fracaso = pygame.mixer.Sound("F_LEVEL/equivocado.mp3")
sonido_voltear = pygame.mixer.Sound("F_LEVEL/voltear.mp3")

# Calculamos el tamaño de la pantalla en base al tamaño de los cuadrados
#anchura_pantalla = len(cuadros[0]) * medida_cuadro # medida de la primera fila * medida del cuadro(img de la fruta)
#screenheight = (len(cuadros) * medida_cuadro) + altura_boton 
#screen_width = anchura_pantalla



# La fuente que estará sobre el botón
tamanio_fuente = 20
fuente = pygame.font.SysFont("Arial", tamanio_fuente)
xFuente = int((screen_width / 2) - (tamanio_fuente / 2)) # posicion de la palabra que aparece sobre el boton respecto a x
yFuente = int(screenheight - altura_boton) # posicion de la palabra que aparece sobre el boton respecto a y

# El botón, que al final es un rectángulo
boton = pygame.Rect(0, screenheight - altura_boton,
                    screen_width, screenheight)

# Banderas
# Bandera para saber si se debe ocultar la tarjeta dentro de N segundos
ultimos_segundos = None
puede_jugar = True  # Bandera para saber si reaccionar a los eventos del usuario
# Saber si el juego está iniciado; así sabemos si ocultar o mostrar piezas, además del botón
juego_iniciado = False
# Banderas de las tarjetas cuando se busca una pareja. Las necesitamos como índices para el arreglo de cuadros
# Se conoce si es la primera vez que se voltea una tarjeta o si es la segunda
# x1 con y1 sirven para la primer tarjeta
x1 = None
y1 = None
# Y las siguientes para la segunda tarjeta
x2 = None
y2 = None

"""
Funciones útiles
"""


# Ocultar todos los cuadros
# Recorre las filas y colmunas de los cuadros
def ocultar_todos_los_cuadros():
    for fila in cuadros:
        for cuadro in fila:
            cuadro.mostrar = False
            cuadro.descubierto = False

# Calcula la cantidad de filas y cantidad de columnas y elige aleatoriamente una imagen
def aleatorizar_cuadros():
    # Elegir X e Y aleatorios, intercambiar
    cantidad_filas = len(cuadros)
    cantidad_columnas = len(cuadros[0])
    for y in range(cantidad_filas):
        for x in range(cantidad_columnas):
            x_aleatorio = random.randint(0, cantidad_columnas - 1)
            y_aleatorio = random.randint(0, cantidad_filas - 1)
            cuadro_temporal = cuadros[y][x]
            cuadros[y][x] = cuadros[y_aleatorio][x_aleatorio]
            cuadros[y_aleatorio][x_aleatorio] = cuadro_temporal

# Determina si se gana, reinicia el juego y suena la pista correspondiente
def comprobar_si_gana():
    if gana():
        pygame.mixer.Sound.play(sonido_exito)
        reiniciar_juego()
        
        


# Regresa False si al menos un cuadro NO está descubierto. True en caso de que absolutamente todos estén descubiertos
# Recorre todas las filas de la matriz y en caso de que alguno no esté descubierto retorna a falso, de lo contrario pasa a true
def gana():
    for fila in cuadros:
        for cuadro in fila:
            if not cuadro.descubierto:
                return False
    return True

    

# si es falso, se reinicia el juego donde se modifica una variable global con falso
def reiniciar_juego():
    global juego_iniciado
    juego_iniciado = False

# Reproduce el sonido de click para que empiece, modifica el juego iniciado y lo aleatoriza 3 veces (primero mezcla los cuadros y luego los oculta)
def iniciar_juego():
    pygame.mixer.Sound.play(sonido_clic)
    global juego_iniciado

    # Aleatorizar 3 veces
    """for i in range(3):
        aleatorizar_cuadros()"""
    ocultar_todos_los_cuadros()
    juego_iniciado = True


"""
Iniciamos la pantalla con las medidas previamente calculadas, colocamos título y
reproducimos el sonido de fondo
"""
# En esta parte se utilizan todas las variables y funciones creadas previamente
screen = pygame.display.set_mode((screen_width, screenheight))
pygame.display.set_caption('Juego Prueba')
#pygame.mixer.Sound.play(sonido_fondo, -1)  # El -1 indica un loop infinito
# Ciclo infinito...
while True:
    # Escuchar eventos, pues estamos en un ciclo infinito que se repite varias veces por segundo
    for event in pygame.event.get():
        if event.type == timer_event:
            level_time -= 1 
            timer_text = timer_font.render(str(level_time), True, color_negro)
            if level_time == 0:
                pygame.time.set_timer(timer_event, 0)
                ##Puedo poner variables para cambiar de nivel o pantallas
                

        
        # Si quitan el juego, salimos
        if event.type == pygame.QUIT:
            sys.exit()
        # Si hicieron clic y el usuario puede jugar...
        elif event.type == pygame.MOUSEBUTTONDOWN and puede_jugar:
            """
            xAbsoluto e yAbsoluto son las coordenadas de la pantalla en donde se hizo
            clic. PyGame no ofrece detección de clic en imagen, por ejemplo. Así que
            se deben hacer ciertos trucos
            """
            # Si el click fue sobre el botón y el juego no se ha iniciado, entonces iniciamos el juego
            xAbsoluto, yAbsoluto = event.pos
            #if boton.collidepoint(event.pos):
            #   if not juego_iniciado:
            #      iniciar_juego()

            #else:
                # Si no hay juego iniciado, ignoramos el clic
            if not juego_iniciado:
                iniciar_juego()
                continue
            """
            Ahora necesitamos a X e Y como índices del arreglo. Los índices no
            son lo mismo que los pixeles, pero sabemos que las imágenes están en un arreglo
            y por lo tanto podemos dividir las coordenadas entre la medida de cada cuadro, redondeando
            hacia abajo, para obtener el índice.
            Por ejemplo, si la medida del cuadro es 100, y el clic es en 140 entonces sabemos que le dieron
            a la segunda imagen porque 140 / 100 es 1.4 y redondeado hacia abajo es 1 (la segunda posición del
            arreglo) lo cual es correcto. Por poner otro ejemplo, si el clic fue en la X 50, al dividir da 0.5 y
            resulta en el índice 0
            """
            x = math.floor(xAbsoluto / medida_cuadro_h)
            y = math.floor(yAbsoluto / medida_cuadro_v)
            # Primero lo primero. Si  ya está mostrada o descubierta, no hacemos nada
            cuadro = cuadros[y][x]
            if cuadro.mostrar or cuadro.descubierto:
                # continue ignora lo de abajo y deja que el ciclo siga
                continue
            # Si es la primera vez que tocan la imagen (es decir, no están buscando el par de otra, sino apenas
            # están descubriendo la primera)
            if x1 is None and y1 is None:
                # Entonces la actual es en la que acaban de dar clic, la mostramos
                x1 = x
                y1 = y
                cuadros[y1][x1].mostrar = True
                pygame.mixer.Sound.play(sonido_voltear)
            else:
                # En caso de que ya hubiera una clickeada anteriormente y estemos buscando el par, comparamos...
                x2 = x
                y2 = y
                cuadros[y2][x2].mostrar = True
                cuadro1 = cuadros[y1][x1]
                cuadro2 = cuadros[y2][x2]
                # Si coinciden, entonces a ambas las ponemos en descubiertas:
                if cuadro1.fuente_imagen == cuadro2.fuente_imagen:
                    cuadros[y1][x1].descubierto = True
                    cuadros[y2][x2].descubierto = True
                    x1 = None
                    x2 = None
                    y1 = None
                    y2 = None
                    pygame.mixer.Sound.play(sonido_clic)
                else:
                    pygame.mixer.Sound.play(sonido_fracaso)
                    error_1 = error_1 + 1 
                    print(error_1)
                    # Si no coinciden, tenemos que ocultarlas en el plazo de [segundos_mostrar_pieza] segundo(s). Así que establecemos
                    # la bandera. Como esto es un ciclo infinito y asíncrono, podemos usar el tiempo para saber
                    # cuándo fue el tiempo en el que se empezó a ocultar
                    ultimos_segundos = int(time.time())
                    # Hasta que el tiempo se cumpla, el usuario no puede jugar
                    puede_jugar = False
            comprobar_si_gana()


    ahora = int(time.time())
    # Y aquí usamos la bandera del tiempo, de nuevo. Si los segundos actuales menos los segundos
    # en los que se empezó el ocultamiento son mayores a los segundos en los que se muestra la pieza, entonces
    # se ocultan las dos tarjetas y se reinician las banderas
    if ultimos_segundos is not None and ahora - ultimos_segundos >= segundos_mostrar_pieza:
        cuadros[y1][x1].mostrar = False
        cuadros[y2][x2].mostrar = False
        x1 = None
        y1 = None
        x2 = None
        y2 = None
        ultimos_segundos = None
        # En este momento el usuario ya puede hacer clic de nuevo pues las imágenes ya estarán ocultas
        puede_jugar = True

    # Hacer toda la pantalla blanca
    screen.fill(color_blanco)
    # Banderas para saber en dónde dibujar las imágenes, pues al final
    # la pantalla de PyGame son solo un montón de pixeles
    x = 0
    y = 0
    # Recorrer los cuadros
    timer_rect = timer_text.get_rect(center = (90,90)) # Centro de la pantalla: center = screen.get_rect().center
    for fila in cuadros:
        x = 0
        for cuadro in fila:
            """
            Si está descubierto o se debe mostrar, dibujamos la imagen real. Si no,
            dibujamos la imagen oculta
            """
            if cuadro.descubierto or cuadro.mostrar:
                screen.blit(timer_text, timer_rect)
                screen.blit(cuadro.imagen_real, (x, y))
            else:
                screen.blit(timer_text, timer_rect)
                screen.blit(imagen_oculta, (x, y))
            x += medida_cuadro_h
        y += medida_cuadro_v

    # Actualizamos la pantalla
    pygame.display.update()