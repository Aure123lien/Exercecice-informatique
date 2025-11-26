import pygame

if not pygame.mixer.get_init():
    pygame.mixer.pre_init(44100, -16, 2, 2, 512)
    pygame.mixer.init()

class SoundManager:
    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound("Projet jeux python en 2D/assets/sounds/click.ogg"),
            "game_over": pygame.mixer.Sound("Projet jeux python en 2D/assets/sounds/game_over.ogg"),
            "meteorite": pygame.mixer.Sound("Projet jeux python en 2D/assets/sounds/meteorite.ogg"),
            "tir": pygame.mixer.Sound("Projet jeux python en 2D/assets/sounds/tir.ogg"),
        }

    def play(self, sound_name):
        self.sounds[sound_name].play()
