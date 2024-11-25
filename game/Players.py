import pygame
from Projectile import Projectile
import Animation

# creer la 1er class qui va representer notre joueur
class Player(Animation.AnimateSprite):
    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.velocity = 10
        self.all_projectiles = pygame.sprite.Group()
        # self.image = pygame.image.load('assets/player.png') #charger image
        self.rect = self.image.get_rect() #positionner l'image sur l'ecran elle doit avoir un rectangle
        self.rect.x = 400 #positionner l'image sur son abscisse de l'ecran (horizontale)
        self.rect.y = 500 #positionner l 'image sur son ordonné de l'ecran (verticale)
        
        
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        # quand le joueur n'a plus de point de vie
        else:
            self.game.game_over()
            
        # mettre a jour l'aniùation
    def update_animation(self):
        self.animate()
            
        
    def update_health_bar(self, surface):
        # barre de vie en base
        pygame.draw.rect(surface, (87, 100, 92), [self.rect.x + 50, self.rect.y -10, self.max_health, 10])
        # dessine la barre de vie
        pygame.draw.rect(surface, (81, 168, 112), [self.rect.x + 50, self.rect.y -10, self.health, 10])

    def launch_projectile(self):
        # creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))# on insert chaque projectile que le joueur va lancer dans ce groupe
        # demarrer l'animation du lancer
        self.start_animation ()
        # jouer le son
        self.game.sound_manager.play('tir')

# bouger a droite et a gauche
    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left (self):
        self.rect.x -= self.velocity
        