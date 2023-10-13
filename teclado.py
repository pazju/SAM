import pygame
import sys

def virtual_keyboard():
    # Inicializar Pygame
    pygame.init()

    # Configuración de la pantalla
    height = pygame.display.Info().current_h
    width = pygame.display.Info().current_w
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Teclado Virtual")
    
    # Cargar la imagen de fondo
    background_image = pygame.image.load("Assets/menu/teclado.png")
    background_image = pygame.transform.scale(background_image, (width, height))

    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
     
    fuente = int(height/20)
    # Fuentes
    font = pygame.font.Font(None, fuente)

    # Texto ingresado por el usuario
    input_text = ""

    # Posición del teclado
    keyboard_x, keyboard_y = width*3/10 , height*3/10

    # Teclas del teclado
    keyboard_layout = [
        "1234567890",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
    ]

    # Posición del cursor en el teclado
    cursor_x, cursor_y = 0, 0

    # Función para dibujar el teclado
    def draw_keyboard():
        key_width, key_height = width/20, width/20
        x, y = keyboard_x, keyboard_y

        for row in keyboard_layout:
            for key in row:
                key_rect = pygame.Rect(x, y, key_width, key_height)
                pygame.draw.rect(screen, BLACK, key_rect, 2)
                key_text = font.render(key, True, BLACK)
                screen.blit(key_text, (x + fuente/2, y + fuente/2 ))

                if cursor_x == row.index(key) and cursor_y == keyboard_layout.index(row):
                    pygame.draw.rect(screen, GREEN, key_rect, 2)
                    pygame.draw.rect(screen, GREEN, (x + 2, y + 2, key_width - 4, key_height - 4), 2)

                x += key_width + fuente/3
            x = keyboard_x
            y += key_height + fuente/3

    # Ciclo principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cursor_x = max(0, cursor_x - 1)
                elif event.key == pygame.K_RIGHT:
                    cursor_x = min(len(keyboard_layout[cursor_y]) - 1, cursor_x + 1)
                elif event.key == pygame.K_UP:
                    cursor_y = max(0, cursor_y - 1)
                    cursor_x = min(len(keyboard_layout[cursor_y]) - 1, cursor_x)
                    # Deseleccionar las opciones y quitar el color rojo
                elif event.key == pygame.K_DOWN:
                    cursor_y = min(len(keyboard_layout) - 1, cursor_y + 1)
                    cursor_x = min(len(keyboard_layout[cursor_y]) - 1, cursor_x)  
                elif event.key == pygame.K_n:
                    # Teclas del teclado virtual
                    selected_key = keyboard_layout[cursor_y][cursor_x]
                    input_text += selected_key
                elif event.key == pygame.K_e and input_text != "":
                    # Borrar la última letra
                    input_text = input_text[:-1]
                elif event.key == pygame.K_v and input_text != "":
                    # Borrar todo el texto
                    input_text = ""
                elif event.key == pygame.K_c and input_text != "":
                    # Guardar
                    #pygame.quit()
                    running = False
                    return input_text
                
        # Limpiar la pantalla
        screen.fill(WHITE)

        # Dibujar la imagen de fondo
        screen.blit(background_image, (0, 0))

        # Dibujar el teclado
        draw_keyboard()

        # Dibujar el texto ingresado
        text_surface = font.render(input_text, True, BLACK)
        screen.blit(text_surface, (keyboard_x, keyboard_y - 50))

        # Actualizar la pantalla
        pygame.display.flip()
        # Actualizar la pantalla
        #pygame.display.update()
        
# Ejemplo de uso
# if __name__ == "__main__":
#     pa = "teclado.png"
#     result = virtual_keyboard(pa)  # Llama a la función principal para mostrar el teclado virtual
#     print("Texto guardado:", result)  # Imprime el texto ingresado por el usuario
