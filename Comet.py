import pygame
import random

# creer le sprit de la comete

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        # definir l'image
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3,12)
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0,800)
        self.comet_event = comet_event
        
        
    def remove(self):
    # chute de la comete
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play('meteorite')
        # verifier si le nb de comete est de 0
        if len(self.comet_event.all_comets) == 0:
            print ("levenement est fini2")
        # remettre la barre a 0
        self.comet_event.reset_percent()
        # apparaitre les 2 premiers monstres
        self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity 
        # ne pas sur le sol
        if self.rect.y >= 550:
            print("sol")
            # retirer la boule de feu
            self.remove()
            # si n'y a plus de boule de feu sur le jeu
            if len(self.comet_event.all_comets) == 0:
                print("evenement finished")
            # remettre lla jauge au depart 
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

            
            # verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            print("joueur touché")

# si n'y a plus de boule de feu sur le jeu
# if self.comet_event.all_comets            # retirer la boule de feu
            self.remove()
            # subir des degats
            self.comet_event.game.player.damage(20)