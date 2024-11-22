import pygame

# class qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):
    # definir les choses a la creation de l'entité
    def __init__(self, sprite_name, size=(200,200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{ sprite_name }.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 #pour commencer l'animation a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False
        
    # definir une methode pour demarrer l'animation
    def start_animation(self):
        self.animation = True
    
    # definir une methode pour animer le sprite
    def animate(self, loop=False):
        
        # verifier si l'animation est active pour cette entité
        if self.animation:
           # passer a l'image suivante
            self.current_image += 1
            # verifier si on attenit la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au depart
                self.current_image = 0
                
                # verifier si l'animation n'est pas en mode boucle
                if loop is False:
                    # arreter l'animation
                    # desactivation de l'animation
                    self.animation = False
                    
                # modifier l'image precedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)
        
        
        
        
# definir une foction pour charger les images du sprite
def load_animation_images(sprite_name):
    # charger les 24 images du sprites du dossiers
    images = []
    # recuperer le chemin du dossier pour le sprite
    path = f'assets/{sprite_name}/{sprite_name}'
    # boucler le dossier des sprites
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
        
    # renvoyer le contenue de la liste d'image
    return images

# definir un dictionnaire qui va contenir les images charger de chaque sprite

animations = {
    'mummy' : load_animation_images('mummy'),
    'player' : load_animation_images('player'),
    'alien' : load_animation_images('alien'),
}