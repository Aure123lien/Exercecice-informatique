import pygame
import random
from ..configuration import *

# création de ma classe comet
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load(COMET_IMG_PATH)
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(COMET_VELOCITY_MIN, COMET_VELOCITY_MAX)
        self.rect.x = random.randint(20, SCREEN_WIDTH - 20)
        self.rect.y = -random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play("meteorite")
        # verifier si les comète sont = 0
        if len(self.comet_event.all_comets) == 0:
            print("La pluie de comète est fini")
            self.comet_event.reset_percent()
            self.comet_event.game.restart_wave()

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= SCREEN_HEIGHT:
            self.remove()
            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.remove()
            # dégat sur le joueur
            self.comet_event.game.player.damage(COMET_DAMAGE)