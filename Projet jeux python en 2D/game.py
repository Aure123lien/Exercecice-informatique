import pygame
from player import Player
from monster import Dragon, Ogre
from comet_event import CometFallEvent
from sounds import SoundManager

class Game:

    def __init__(self):
        self.is_playing = False
        self.is_game_over = False

        # Joueur
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)

        # Événements
        self.comet_event = CometFallEvent(self)

        # Monstres
        self.all_monsters = pygame.sprite.Group()

        # Sons
        self.sound_manager = SoundManager()

        # Gestion des touches
        self.pressed = {}

        # fin de partie affichage
        self.game_over_image = pygame.image.load("Projet jeux python en 2D/assets/Game_over.png").convert()
        self.go_title_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 60)
        self.go_sub_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 35)
        self.go_restart_button = pygame.Rect(390, 300, 300, 60)
        self.go_menu_button = pygame.Rect(390, 380, 300, 60)

    # ajout des points pour les monstres
    def add_score(self, points):
        self.player.add_score(points)

    # Démarrer une partie
    def start(self):
        self.is_playing = True
        self.player.rect.x = 350
        # Toujours sur le sol
        self.player.rect.y = 1080 - self.player.image.get_height() - 130
        self.player.health = self.player.max_health
        self.all_monsters.empty()
        self.comet_event.all_comets.empty()
        self.comet_event.reset_percent()
        for _ in range(2):
            self.spawn_monster(Ogre)
        self.spawn_monster(Dragon)

    # Fin de la partie
    def game_over(self):
        self.all_monsters.empty()
        self.comet_event.all_comets.empty()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.is_game_over = True
        self.player.score = 0
        self.sound_manager.play("game_over")

    # Affichage écran de fin de partie
    def display_game_over(self, screen):
        screen.blit(self.game_over_image, (0, 0))
        title = self.go_title_font.render("Vous avez péri", True, (255, 0, 0))
        screen.blit(title, title.get_rect(center=(screen.get_width() // 2, 90)))

        pygame.draw.rect(screen, (200, 200, 200), self.go_restart_button)
        restart_text = self.go_sub_font.render("Recommencer", True, (0, 0, 0))
        screen.blit(restart_text, restart_text.get_rect(center=self.go_restart_button.center))

        pygame.draw.rect(screen, (200, 200, 200), self.go_menu_button)
        menu_text = self.go_sub_font.render("Retour au menu", True, (0, 0, 0))
        screen.blit(menu_text, menu_text.get_rect(center=self.go_menu_button.center))

    # Mise à jour de la partie
    def update(self, screen):
        # Joueur et barre de vie
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        # Barre de progression comète
        self.comet_event.update_bar(screen)

        # Projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()
        self.player.all_projectiles.draw(screen)

        # Monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        self.all_monsters.draw(screen)

        # Comètes
        for comet in self.comet_event.all_comets:
            comet.fall()
        self.comet_event.all_comets.draw(screen)

        # Déplacements joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.right < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.left > 0:
            self.player.move_left()

    # Système de Collision
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # Spawn des monstres
    def spawn_monster(self, monster_class_name=Ogre):
        self.all_monsters.add(monster_class_name(self))



















