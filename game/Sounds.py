import pygame

class SoundManager():
    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound('static/assets/sounds/click.ogg'),
            'game_over': pygame.mixer.Sound('static/assets/sounds/game_over.ogg'),
            'meteorite': pygame.mixer.Sound('static/assets/sounds/meteorite.ogg'),
            'tir': pygame.mixer.Sound('static/assets/sounds/tir.ogg'),
        }
        
    def play(self, name):
        self.sounds[name].play()