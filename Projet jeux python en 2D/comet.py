import pygame
import random

# création de ma classe comet
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("Projet jeux python en 2D/assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

    def fall(self):
        self.rect.y += self.velocity
        
        if self.rect.y >= 500:
            print ("Sol")
            self.remove()


        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            print("la comète a toucher")
            self.remove()
            # dégat sur le joueur
            self.comet_event.game.player.damage(20)