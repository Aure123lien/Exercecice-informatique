import pygame
import random
from ..configuration import *

font = pygame.font.SysFont("Arial", 16)

# création de ma classe monster
class Monster(pygame.sprite.Sprite):
    # Classe de base pour les monstres
    def __init__(self, game, name, image_path, size, multiplier=1):
        super().__init__()
        self.game = game
        self.health = 100 * multiplier
        self.max_health = 100 * multiplier
        self.attack = MONSTER_ATTACK_OGRE * multiplier
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(0, 300)
        self.rect.y = SCREEN_HEIGHT - size[1] - 50
        self.loot_amount = OGRE_LOOT * multiplier
        self.name = name

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, int(self.default_speed))

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            # Respawn du monstre
            self.rect.x = SCREEN_WIDTH + random.randint(0, 300)
            self.velocity = random.randint(1, int(self.default_speed))
            self.health = self.max_health
            self.game.add_score(self.loot_amount)
            # Si l'événement comète est chargé, déclencher la chute
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        bar_width = 100
        bar_height = 5
        bar_x = self.rect.centerx - bar_width // 2
        bar_y = self.rect.y - 30
        pygame.draw.rect(surface, GRAY, [bar_x, bar_y, bar_width, bar_height])
        pygame.draw.rect(surface, RED, [bar_x, bar_y, (self.health / self.max_health) * bar_width, bar_height])
        text = font.render(f"{int(self.health)}/{int(self.max_health)}", True, BLACK)
        text_rect = text.get_rect(centerx=self.rect.centerx, y=bar_y - 20)
        surface.blit(text, text_rect)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
           self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

# création des différentes classes de monstres
class Ogre(Monster):
    def __init__(self, game, multiplier=1):
        size = (150, 150)
        super().__init__(game, "ogre", OGRE_IMG_PATH, size, multiplier)
        self.rect.y = SCREEN_HEIGHT - size[1] - 70
        self.set_speed(5 * multiplier)
        self.set_loot_amount(OGRE_LOOT * multiplier)

class Dragon(Monster):
    def __init__(self, game, multiplier=1):
        size = (400, 400)
        super().__init__(game, "dragon", DRAGON_IMG_PATH, size, multiplier)
        self.rect.y = SCREEN_HEIGHT - size[1] - 30
        self.health = DRAGON_HEALTH * multiplier
        self.max_health = DRAGON_HEALTH * multiplier
        self.attack = MONSTER_ATTACK_DRAGON * multiplier
        self.set_speed(3 * multiplier)
        self.set_loot_amount(DRAGON_LOOT * multiplier)