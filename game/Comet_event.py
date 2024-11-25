import pygame
from Comet import Comet

# creer une class pour gerer l'event a intervale regulier
class CometFallEvent:
    
    # lors du chargement on va devoir crrer un compteur
    def __init__(self, game):
        self.percent = 0
        self.speed_percent = 40
        self.game = game
        self.fall_mode = False
        
        # definir un groupe de sprite pour stocker les cometes
        self.all_comets = pygame.sprite.Group()
        
        
    def add_percent(self):
        self.percent += self.speed_percent / 100
        
    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0
        
    def meteor_fall(self):
        # boucle pour plusieurs cometes
        for i in range(1,10):
        # apparaitre un boule de feu
            self.all_comets.add(Comet(self))
    
    def attempt_fall(self):
    # Si la barre d'événement est pleine et qu'il n'y a pas de monstres
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("comete!")
            self.meteor_fall()  # Génère les comètes
            self.fall_mode = True  # Active l'événement

            
        
    def update_bar(self, surface):
        # ajouter du pourcentage a barre grace a add.percent
        self.add_percent()

        # barre noir en arriere plan
        pygame.draw.rect(surface, (0,0,0), [
            0, # axe des X
            surface.get_height() - 20, # axe des Y
            surface.get_width(), # longeuur de la barre a la febetre
            10 #epaisseur de la barre
        ])
        
        # barre rouge jaune event
        pygame.draw.rect(surface, (187,11,11), [
            0, # axe des X
            surface.get_height() - 20, # axe des Y
            (surface.get_width() / 100)*self.percent, # longeuur de la barre a la febetre
            10 #epaisseur de la barre
        ])
       