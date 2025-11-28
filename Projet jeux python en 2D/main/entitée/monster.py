import pygame
import random
from ..configuration import *

# création de ma classe monster
class Monster(pygame.sprite.Sprite):
    def __init__(self, game, name, image_path, size):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = MONSTER_ATTACK_OGRE
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(0, 300)
        self.rect.y = SCREEN_HEIGHT - size[1] - 50
        self.loot_amount = OGRE_LOOT
        self.name = name

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 2)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = SCREEN_WIDTH + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            self.game.add_score(self.loot_amount)
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, GRAY, [self.rect.x + 50, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, RED, [self.rect.x + 50, self.rect.y - 20, self.health, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
           self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

# création des différente classes de monstres
class Ogre(Monster):
    def __init__(self, game):
        size = (150, 150)
        super().__init__(game, "ogre", OGRE_IMG_PATH, size)
        self.rect.y = SCREEN_HEIGHT - size[1] - 70
        self.set_speed(5)
        self.set_loot_amount(OGRE_LOOT)

class Dragon(Monster):
    def __init__(self, game):
        size = (400, 400)
        super().__init__(game, "dragon", DRAGON_IMG_PATH, size)
        self.rect.y = SCREEN_HEIGHT - size[1] - 30
        self.health = DRAGON_HEALTH
        self.max_health = DRAGON_HEALTH
        self.attack = MONSTER_ATTACK_DRAGON
        self.set_speed(3)
        self.set_loot_amount(DRAGON_LOOT)