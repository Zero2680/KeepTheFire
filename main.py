from pygame import *
init()
from random import *
from button import Button
import asyncio
screen = display.set_mode((1280, 720))
display.set_caption('Fire Game')
screen.fill((0, 0, 0)) 

class Objeto(sprite.Sprite):
	def __init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion, color, vidas, team):
		sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.ancho = ancho
		self.largo = largo
		self.direccionx = direccionx
		self.direcciony = direcciony
		self.puntuacion = puntuacion
		self.color = color
		self.vidas = vidas
		self.team = team

	def DibujarObjeto(self):
		draw.rect(screen, self.color, (self.x,self.y,self.ancho,self.largo))

	def check_colisiones(sprite1, sprite2):
		xsprite1 = sprite1.x
		ysprite1 = sprite1.y
		anchosprite1 = sprite1.ancho
		largosprite1 = sprite1.largo
		xsprite2 = sprite2.x
		ysprite2 = sprite2.y
		anchosprite2 = sprite2.ancho
		largosprite2 = sprite2.largo
		if (ysprite1 + largosprite1) > ysprite2 and ysprite1 < (ysprite2 + largosprite2) and (xsprite1 + anchosprite1) > xsprite2 and xsprite1 < (xsprite2 + anchosprite2):
			return True

class Bola(Objeto):
	def __init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion, color, vidas, team):
		Objeto.__init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion, color, vidas, team)
	
	def Movimiento(self):
		x = self.x
		y = self.y
		keys = key.get_pressed()
		if keys[K_w]==1:
			self.direcciony = 1
			if y > 0:
				self.y -= 5
		if keys[K_s]:
			self.direcciony = 0
			if y < 700:
				self.y += 5
		if keys[K_a]==1:
			self.direccionx = 0
			self.direcciony = 2
			if x > 0:
				self.x -= 5
		if keys[K_d]:
			self.direccionx = 1
			self.direcciony = 2
			if x < 1260:
				self.x += 5
    
	def MovimientoLetra(self, num):
		global l1, l2, l3, letras, cod1, cod2, cod3, fuego
		if self.direcciony == 1:
			if self.y < 720:
				if self.y == -100:
					self.x = randrange(1, 13) * 100
				self.y += 4
			if self.y >= 720:
				if self.y == 720: 
					fuego -= 5
					error_sound.play()
				self.y = -100
				if num == 1:
					l1 = choice(letras)
					cod1 = key.key_code(l1)
				elif num == 2:
					l2 = choice(letras)
					cod2 = key.key_code(l2)
				elif num == 3:
					l3 = choice(letras)
					cod3 = key.key_code(l3)
				elif num == 4:
					l4 = choice(letras)
					cod4 = key.key_code(l4)
				elif num == 5:
					l5 = choice(letras)
					cod5 = key.key_code(l5)
				elif num == 6:
					l6 = choice(letras)
					cod6 = key.key_code(l6)
		elif self.direccionx == 1:
			if self.x < 1280:
				if self.x == -100:
					self.y = randrange(1, 7) * 100
				self.x += 4
			if self.x >= 1280:
				if self.x == 1280: 
					fuego -= 5
					error_sound.play()
				self.x = -100
				if num == 1:
					l1 = choice(letras)
					cod1 = key.key_code(l1)
				elif num == 2:
					l2 = choice(letras)
					cod2 = key.key_code(l2)
				elif num == 3:
					l3 = choice(letras)
					cod3 = key.key_code(l3)
				elif num == 4:
					l4 = choice(letras)
					cod4 = key.key_code(l4)
				elif num == 5:
					l5 = choice(letras)
					cod5 = key.key_code(l5)
				elif num == 6:
					l6 = choice(letras)
					cod6 = key.key_code(l6)

def get_font(size):
    return font.Font("menu_assets/font.ttf", size)

def barra_hp(screen, x, y, hp, color):
	largo = 165
	ancho = 10
	calculo_barra = int((hp / 100)*largo)
	draw.rect(screen, color, Rect(x, y, calculo_barra, ancho))

clock = time.Clock()
fondo = transform.scale(image.load("keepthefire_images/fondo.png").convert(), (1280, 720))
persona1 = transform.scale(image.load("keepthefire_images/person1.png"), (175, 175))
persona2 = transform.scale(image.load("keepthefire_images/person2.png"), (175, 175))
fire1 = transform.scale(image.load("keepthefire_images/fire1.png"), (60, 100))
fire2 = transform.scale(image.load("keepthefire_images/fire2.png"), (60, 100))
fire3 = transform.scale(image.load("keepthefire_images/fire3.png"), (60, 100))
fire4 = transform.scale(image.load("keepthefire_images/fire4.png"), (60, 100))
npc1 = transform.scale(image.load("keepthefire_images/npc1.png"), (175, 175))
npc2 = transform.scale(image.load("keepthefire_images/npc2.png"), (175, 175))
npc3 = transform.scale(image.load("keepthefire_images/npc3.png"), (175, 175))
npc4 = transform.scale(image.load("keepthefire_images/npc4.png"), (175, 175))
error_sound = mixer.Sound('keepthefire_sounds/Damage.ogg')
error_sound.set_volume(0.125)

async def main():
    global l1, l2, l3, l4, l5, l6, letras, cod1, cod2, cod3, cod4, cod5, cod6, fuego
    estado = "Menu"
    plataforma = Bola(300,350,55,55, 1, 1, 0, (0,0,255), 100, 0)
    letra1 = Bola(640,-100,40,40, 0, 1, 0, (255,0,0), 100, 0)
    letra2 = Bola(-100,0,40,40, 1, 0, 0, (255,0,0), 100, 0)
    letra3 = Bola(640,-100,40,40, 0, 1, 0, (255,0,0), 100, 0)
    letra4 = Bola(-100,0,40,40, 1, 0, 0, (255,0,0), 100, 0)
    letra5 = Bola(640,-100,40,40, 0, 1, 0, (255,0,0), 100, 0)
    letra6 = Bola(-100,0,40,40, 1, 0, 0, (255,0,0), 100, 0)
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    l1 = choice(letras)
    cod1 = key.key_code(l1)
    l2 = choice(letras)
    cod2 = key.key_code(l2)
    l3 = choice(letras)
    cod3 = key.key_code(l3)
    l4 = choice(letras)
    cod4 = key.key_code(l4)
    l5 = choice(letras)
    cod5 = key.key_code(l5)
    l6 = choice(letras)
    cod6 = key.key_code(l6)
    fuego = 100
    inicio_temporizador = time.get_ticks()
    tiempo_juego = 0
    tiempo_letras = 0
    while True:
        if estado == "Menu":
            mixer.music.stop()
            screen.blit(fondo, (0, 0))

            MENU_MOUSE_POS = mouse.get_pos()

            MENU_TEXT = get_font(75).render("KEEP THE FIRE", True, (178, 64, 182))
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=image.load("menu_assets/Play Rect.png"), pos=(640, 250), 
                                text_input="PLAY", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
            OPTIONS_BUTTON = Button(image=image.load("menu_assets/Options Rect.png"), pos=(640, 400), 
                                text_input="OPTIONS", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
            QUIT_BUTTON = Button(image=image.load("menu_assets/Quit Rect.png"), pos=(640, 550), 
                                text_input="QUIT", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

            screen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(screen)
            
            for evento in event.get():
                if evento.type == QUIT:
                    quit()
                    exit()
                if evento.type == MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        mixer.music.set_volume(0.25)
                        mixer.music.load('keepthefire_sounds/Musica.ogg')
                        mixer.music.set_volume(mixer.music.get_volume())
                        mixer.music.play(-1)
                        estado = "Play"
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        estado = "Options"
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        quit()
                        exit()
                if evento.type==KEYDOWN:
                    if evento.key == K_1 and mixer.music.get_volume() > 0.0:
                        mixer.music.set_volume(mixer.music.get_volume() - 0.1)
                    if evento.key == K_2 and mixer.music.get_volume() > 0.0:
                        mixer.music.set_volume(mixer.music.get_volume() + 0.1)
                    if evento.key == K_ESCAPE:
                        quit()
                        exit()
            display.update()
        
        elif estado == "Options":
            mixer.music.stop()
            OPTIONS_MOUSE_POS = mouse.get_pos()

            screen.fill((0, 0, 0)) 

            OPTIONS_TEXT = get_font(45).render("OPTIONS", True, (178, 64, 182))
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
            screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

            DECREASE_TEXT = get_font(45).render("1 : Decrease Volume", True, (215, 252, 212))
            DECREASE_RECT = DECREASE_TEXT.get_rect(center=(640, 250))
            screen.blit(DECREASE_TEXT, DECREASE_RECT)

            INCREASE_TEXT = get_font(45).render("2 : Increase Volume", True, (215, 252, 212))
            INCREASE_RECT = INCREASE_TEXT.get_rect(center=(640, 400))
            screen.blit(INCREASE_TEXT, INCREASE_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 550), 
                                text_input="BACK", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(screen)

            for evento in event.get():
                if evento.type == QUIT:
                    quit()
                    exit()
                if evento.type == MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        estado = "Menu"
                if evento.type==KEYDOWN:
                    if evento.key == K_1 and mixer.music.get_volume() > 0.0:
                        mixer.music.set_volume(mixer.music.get_volume() - 0.1)
                    if evento.key == K_2 and mixer.music.get_volume() > 0.0:
                        mixer.music.set_volume(mixer.music.get_volume() + 0.1)
                    if evento.key == K_ESCAPE:
                        estado = "Menu"

            display.update()
        
        elif estado == "Play":
            screen.blit(fondo, (0, 0))

            if tiempo_juego <= 50:
                screen.blit(persona1, (555, 480))
            elif tiempo_juego <= 100:
                screen.blit(persona2, (545, 480))
                if tiempo_juego == 100: tiempo_juego = 0
            
            if tiempo_juego <= 50:
                screen.blit(npc1, (130, 470))
            elif tiempo_juego <= 100:
                screen.blit(npc2, (130, 470))
                if tiempo_juego == 100: tiempo_juego = 0
            
            if tiempo_juego <= 50:
                screen.blit(npc3, (940, 480))
            elif tiempo_juego <= 100:
                screen.blit(npc4, (940, 480))
                if tiempo_juego == 100: tiempo_juego = 0

            if fuego >= 66:
                if tiempo_juego <= 50:
                    screen.blit(fire2, (675, 550))
                elif tiempo_juego <= 100:
                    screen.blit(fire1, (675, 550))
                    if tiempo_juego == 100: tiempo_juego = 0
            elif fuego >= 33:
                screen.blit(fire3, (675, 550))
            elif fuego >= 1:
                screen.blit(fire4, (675, 550))

            barra_hp(screen, 555, 480, fuego, (237, 137, 0))

            tiempo_juego += 1
            tiempo_letras += 1
            fuego -= 0.05
            if tiempo_letras >= 2500: fuego -= 0.025
            if tiempo_letras >= 5000: fuego -= 0.025

            if fuego > 100: fuego = 100

            letra1.MovimientoLetra(1)
            LETRA1_BUTTON = Button(image=None, pos=(letra1.x+25, letra1.y+25), text_input=l1.upper(), font=get_font(37), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
            LETRA1_BUTTON.update(screen)

            if tiempo_letras >= 1000:
                letra2.MovimientoLetra(2)
                LETRA2_BUTTON = Button(image=None, pos=(letra2.x+25, letra2.y+25), text_input=l2.upper(), font=get_font(37), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
                LETRA2_BUTTON.update(screen)

            if tiempo_letras >= 2000:
                letra3.MovimientoLetra(3)
                LETRA3_BUTTON = Button(image=None, pos=(letra3.x+25, letra3.y+25), text_input=l3.upper(), font=get_font(37), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
                LETRA3_BUTTON.update(screen)

            if tiempo_letras >= 3000:
                letra4.MovimientoLetra(4)
                LETRA4_BUTTON = Button(image=None, pos=(letra4.x+25, letra4.y+25), text_input=l4.upper(), font=get_font(37), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
                LETRA4_BUTTON.update(screen)

            if tiempo_letras >= 4000:
                letra5.MovimientoLetra(5)
                LETRA5_BUTTON = Button(image=None, pos=(letra5.x+25, letra5.y+25), text_input=l5.upper(), font=get_font(37), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
                LETRA5_BUTTON.update(screen)

            if tiempo_letras >= 5000:
                letra6.MovimientoLetra(6)
                LETRA6_BUTTON = Button(image=None, pos=(letra6.x+25, letra6.y+25), text_input=l6.upper(), font=get_font(37), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
                LETRA6_BUTTON.update(screen)

            if fuego <= 0:
                estado = "Final"

            display.update()
            for evento in event.get():
                if evento.type == QUIT:
                    quit()
                    exit()
                if evento.type==KEYDOWN:
                    if evento.key == cod1:
                        letra1.y = 730
                        fuego += 5
                    elif evento.key == cod2 and tiempo_letras >= 1000:
                        letra2.x = 1290
                        fuego += 5
                    elif evento.key == cod3 and tiempo_letras >= 2000:
                        letra3.y = 730
                        fuego += 5
                    elif evento.key == cod4 and tiempo_letras >= 3000:
                        letra4.x = 1290
                        fuego += 5
                    elif evento.key == cod5 and tiempo_letras >= 4000:
                        letra5.y = 730
                        fuego += 5
                    elif evento.key == cod6 and tiempo_letras >= 5000:
                        letra6.x = 1290
                        fuego += 5
                    elif evento.key == K_1 and mixer.music.get_volume() > 0.0:
                        mixer.music.set_volume(mixer.music.get_volume() - 0.1)
                    elif evento.key == K_2 and mixer.music.get_volume() > 0.0:
                        mixer.music.set_volume(mixer.music.get_volume() + 0.1)
                    elif evento.key == K_ESCAPE:
                        quit()
                        exit()
                    else:
                        error_sound.play()
                        fuego -= 10

        elif estado == "Final":
            mixer.music.stop()

            if fuego != -100:
                tiempo_minijuego = (time.get_ticks() - inicio_temporizador) // 1000
                minutos = tiempo_minijuego // 60
                segundos = tiempo_minijuego % 60
                fuego = -100

            DURACION_TEXT = get_font(37).render("You lasted:", True, (226, 63, 63))
            DURACION_RECT = DURACION_TEXT.get_rect(center=(640, 225))
            screen.blit(DURACION_TEXT, DURACION_RECT)

            TIEMPO_TEXT = get_font(37).render(f"{minutos:02}:{segundos:02}", True, (226, 63, 63))
            TIEMPO_RECT = TIEMPO_TEXT.get_rect(center=(640, 300))
            screen.blit(TIEMPO_TEXT, TIEMPO_RECT)

            NICE_TEXT = get_font(37).render("Nice time!", True, (226, 63, 63))
            NICE_RECT = NICE_TEXT.get_rect(center=(640, 375))
            screen.blit(NICE_TEXT, NICE_RECT)

            display.update()
            for evento in event.get():
                if evento.type == QUIT:
                    quit()
                    exit()
                if evento.type==KEYDOWN:
                    if evento.key == K_1 and mixer.music.get_volume() > 0.0:
                        mixer.music.set_volume(mixer.music.get_volume() - 0.1)
                    if evento.key == K_2 and mixer.music.get_volume() > 0.0:
                        mixer.music.set_volume(mixer.music.get_volume() + 0.1)
                    if evento.key == K_ESCAPE:
                        quit()
                        exit()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())