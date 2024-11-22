import pygame
from Players import Player
from Monster import Monster, Mummy, Alien
from Comet_event import CometFallEvent 
from Sounds import SoundManager




# crrer un 2nd classe qui va represneter le jeu
class Game:
    def __init__(self):
        # defiir si le jeu a commencé ou non
        self.is_playing = False
        # generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement comete
        self.comet_event = CometFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # gerer le son du jeu
        self.sound_manager = SoundManager()
        # Mettre le score du joueur a 0
        self.score = 0
        self.pressed = {}

        
    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        
    def add_score(self, points = 10):
        self.score += points
        
    def game_over(self):
        # remettre le jeu a zero
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        # remettre le score a 0
        self.score = 0
        # jouer le son
        self.sound_manager.play('game_over')
        
        
    def update (self, screen):
        # afficher le score sur l'ecran
        font = pygame.font.SysFont("Helvetica", 24, ) #creer la police
        # police d'ecriture personalisé
        # font = pygame.font.Font("assets/mycustomFont.ttf", 25)
        score_texte = font.render(f"Score: {self.score}", 1, (0,0,0))#crrer un texte avec couleur
        screen.blit(score_texte, (20, 20))
        
        
            # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)
        
        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        
        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)
        
        # actualiser l'animation du joueur
        self.player.update_animation()

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres et pour les faire avancer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen) 
            monster.update_animation()
            
        # recuperer les cometes qui tombent 
        for comet in self.comet_event.all_comets:
            comet.fall()
            
        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstres
        self.all_monsters.draw(screen)
        
        # appliquer l'ensemble des images de mon groupe de cometes
        self.comet_event.all_comets.draw(screen)
        
        

    # verifier si le joueur souhaite aller a droit ou gauche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect. x > 0:
            self.player.move_left()
            

    def check_collision (self, sprite, group):
        return pygame.sprite.spritecollide (sprite, group, False, pygame.sprite.collide_mask)

# creer l'apparition du monstre dans le jeu
    def spawn_monster(self, monster_class_name):
        if len(self.all_monsters) < 3:  # Limite à 3 monstres
            self.all_monsters.add(monster_class_name.__call__(self)) # et on range les monstre dans le groupe de monstre quand ils sont crée


