import pygame
import random

# créer la classe Monster
class Monster(pygame.sprite.Sprite):
    def __init__(self, game, name, image_path, size):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = 900 + random.randint(0, 300)
        self.rect.y = 465
        self.name = name

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 2)

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.x = 900 + random.randint(0, 300)
            self.velocity = random.randint(1,self.default_speed)
            self.health = self.max_health

            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (94, 90, 90), [self.rect.x + 50, self.rect.y -20, self.max_health, 5])
        pygame.draw.rect(surface, (255, 41, 0), [self.rect.x + 50, self.rect.y -20, self.health, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
           self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)


# classe Ogre
class Ogre(Monster):
    def __init__(self, game):
        super().__init__(game, "ogre", "Projet jeux python en 2D/assets/ogre.png", (130, 130))
        self.set_speed(3)

# classe Dragon
class Dragon(Monster):
    def __init__(self, game):
        super().__init__(game, "dragon", "Projet jeux python en 2D/assets/dragon.png", (250, 250))
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.rect.y = 360
        self.set_speed(1)