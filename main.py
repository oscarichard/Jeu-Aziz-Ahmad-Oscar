import pygame
import math
from Game import Game
pygame.init()

# fenetre
pygame.display.set_caption("SuperMan In Space")
screen = pygame.display.set_mode((1080, 720))

# importer background
background = pygame.image.load("assets/space.jpg")
background = pygame.transform.scale(background,(1080,720))

# importer le bouton
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.2)
play_button_rect.y = math.ceil(screen.get_height() / 1.5)

# importer la banier
banner = pygame.image.load("assets/bannier_super.jpg")
banner = pygame.transform.scale(banner, (1080,720))
banner_rect = banner.get_rect()

# music
music = pygame.mixer.music.load("assets/theme.mp3")
pygame.mixer.music.play(-1)

# charger notre jeu
game = Game()
running = True

# while tant que running est vrai
while running:
    # appliquer l'arriere plan de notre jeu

    screen.blit(background, (0,0))

    # verifie si le jeu a commencer
    if game.is_playing:
        # déclencher les instruction
        game.update(screen)
    else:
        # ecran de bonjour
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    # mettre à jour l'ecran
    pygame.display.flip()

    # si la fenetre est fermer
    for event in pygame.event.get():
        # evenenment si fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("joueur ne veut plus jouer")
        # detecter si le joueur enclenche une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_UP:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.game_start()