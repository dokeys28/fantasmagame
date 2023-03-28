import pygame

#juego con modo guardar partida
#personaje que se mueve dentro de un mapa
#que al guardar partida y cargemos partida
#el personaje aparezca en el mismo lugar

MAPA = 'bosque.png'
PERSONAJE = 'fantasma.png'

pygame.init()

ventana = pygame.display
ventana.init()
app = ventana.set_mode((512,512))
pygame.display.set_caption('Fantasma')
fondo = pygame.image.load(MAPA)
personaje = pygame.image.load(PERSONAJE)
pygame.display.set_icon(personaje)
posicionPersonajeInicial = (50,200)
terminar = False
minPosicionNube =(450,0)
maxPosicionNube =(463,70)
minPosicionNubeLoad =(15,10)
maxPosicionNubeLoad =(67,54)
posicionPersonajeActualx, posicionPersonajeActualy = posicionPersonajeInicial
historial = ['derecha']
partidaGuardadas = []
cancion = pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

def guardarPartida():
    print('Guardando Partida....')
    #conseguir posicion actual del jugador
    posicionActual = (posicionPersonajeActualx, posicionPersonajeActualy)
    partidaGuardadas.append(posicionActual)
    print('Partida Guardada')

def cargarPartida():
    print('Cargando Partida....')
    #conseguir posicion actual del jugador
    print('Partida Cargada')
    return partidaGuardadas[-1]



while not terminar:


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            terminar = True
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            posicionMousex,posicionMousey = pygame.mouse.get_pos()
            if posicionMousex >= minPosicionNube[0] and posicionMousex <=maxPosicionNube[0]:
                if posicionMousey >= minPosicionNube[1] and posicionMousey <=maxPosicionNube[1]:
                    guardarPartida()
            elif posicionMousex >= minPosicionNubeLoad[0] and posicionMousex <=maxPosicionNubeLoad[0]:
                if posicionMousey >= minPosicionNubeLoad[1] and posicionMousey <=maxPosicionNubeLoad[1]:
                    posicionPersonajeActualx,posicionPersonajeActualy=cargarPartida()
                    if historial[-1] != 'derecha':
                        personaje = pygame.transform.flip(personaje,True,False)
       
        #manejo de teclas
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                posicionPersonajeActualx+= 20
                if historial[-1] != 'derecha':
                    personaje = pygame.transform.flip(personaje,True,False)
                    historial.append('derecha')
            elif event.key == pygame.K_LEFT:
                posicionPersonajeActualx-= 20
                if historial[-1] != 'izquierda':
                    personaje = pygame.transform.flip(personaje,True,False)
                    historial.append('izquierda')
        
            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT:

                    posicionPersonajeActualx=posicionPersonajeActualx
                
                elif event.key == pygame.K_LEFT:
                    
                    posicionPersonajeActualx=posicionPersonajeActualx

        app.blit(fondo,(0,0))
        app.blit(personaje,(posicionPersonajeActualx,posicionPersonajeActualy))
        ventana.update()


