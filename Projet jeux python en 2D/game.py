import pygame
from player import Player
from monster import Dragon, Monster, Ogre
from comet_event import CometFallEvent

# créer une seconde classe
class Game:

    def __init__(self):
        # Definir si le jeux a commencer
        self.is_playing = False
        # générer un joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generation de l'evenement
        self.comet_event = CometFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        # spawn initial de monstres
       

    def start(self):
        self.is_playing = True
        self.spawn_monster(Ogre)
        self.spawn_monster(Ogre)
        self.spawn_monster(Dragon)

    def game_over(self):
        # remettre le jeux à zéro
        # réinitialiser la vie du personnage
        # retirer les monstres
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False

    def update(self, screen):
        # afficher le joueur
        screen.blit(self.player.image, self.player.rect)

        # afficher la barre de vie du joueur
        self.player.update_health_bar(screen)

        # afficher la barre de la comète
        self.comet_event.update_bar(screen)

        # déplacer et afficher les projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()
        self.player.all_projectiles.draw(screen)

        # déplacer et afficher les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        for comet in self.comet_event.all_comets:
            comet.fall()


        self.all_monsters.draw(screen)

        # appliquer mon groupe comet
        self.comet_event.all_comets.draw(screen)

        # déplacement du joueur (géré ici pour que le rendu soit cohérent)
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name=Ogre):
        self.all_monsters.add(monster_class_name.__call__(self))
