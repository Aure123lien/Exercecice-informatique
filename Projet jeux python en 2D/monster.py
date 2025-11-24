import pygame
import random


# créer la classe Monster
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load("Projet jeux python en 2D/assets/ogre.png")
        self.rect = self.image.get_rect()
        self.rect.x = 900 + random.randint(0, 300)
        self.rect.y = 465
        self.velocity = random.randint(1, 3)
    # Redimensionner l'image du monstre
        self.image = pygame.transform.scale(self.image, (200, 150))

    def damage(self, amount):
        # le nombre de dégats
        self.health -= amount

        # faire un if pour savoir si le monstre meurt
        if self.health <= 0:
            # Faire réaparaitre un nouveau monstre au départ
            self.rect.x = 900 + random.randint(0, 300)
            self.velocity = random.randint(1,3)
            self.health = self.max_health



    def update_health_bar(self, surface):
        # mettre la barre de vie visuellement
        pygame.draw.rect(surface, (94, 90, 90), [self.rect.x + 50, self.rect.y -20, self.max_health, 5])
        pygame.draw.rect(surface, (255, 41, 0), [self.rect.x + 50, self.rect.y -20, self.health, 5])
        


    def forward(self):
        # cette ligne rajoute que mon monstre pourra se déplacer jusqu'a ce qu'il est une colission avec le joueur
        if not self.game.check_collision(self, self.game.all_players):
           self.rect.x -= self.velocity
        # si le monstre est en colision
        else:
            self.game.player.damage(self.attack)