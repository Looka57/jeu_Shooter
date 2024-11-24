import pygame
pygame.init()
from Game import Game

# definir une clock
clock = pygame.time.Clock()
FPS = 100

# GENERERER LA FENETRE DU JEU
# Le titre
pygame.display.set_caption("Game Meteor")

# Les dimensions
screen = pygame.display.set_mode((1080,720))

# importer et charger l'img de l'arriere plan
background = pygame.image.load('assets/bg.jpg')
# charger le jeu
game = Game()

# Maintient de la fenetre ouverte
running = True
# boucle tant que la condition est vrai
while running:

    # appliquer l'arriere plan du jeu
    screen.blit(background, (0,-200))
    
    # importer notre banniere
    banner = pygame.image.load('assets/banner.png')
    banner = pygame.transform.scale(banner,(600, 600))
    banner_rect = banner.get_rect()
    banner_rect.x = screen.get_width()/4
    
    # importer le bouton play
    play_button = pygame.image.load('assets/button.png') 
    play_button = pygame.transform.scale(play_button,(400, 150))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = screen.get_width()/3
    play_button_rect.y = screen.get_height()/2 + 80

    # verifier si notre jeu a commencé ou non 
    if game.is_playing:
        # declencher les instrucyion de la partie
        game.update(screen)
    # si notre jeu n'a pas commencé
    else:
        # mon bouto play
        screen.blit(play_button, (play_button_rect))
        # mon ecran de bienvenue
        screen.blit(banner, (banner_rect))

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre 
    for event in pygame.event.get():
        # que l'evenenment est la fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("le jeu est fermé")
        # detecter quand un joueur appuie sur une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # detecter quand un joueur appuie sur la barre d'espace
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # mettre le jeu en action
                    game.start()
                    # jouer le son de play
                    game.sound_manager.play('click')
        # detecter quand un joueur n'appuie plus sur une touche
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en colision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en action
                game.start()
                # jouer le son de play
                game.sound_manager.play('click')
    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)