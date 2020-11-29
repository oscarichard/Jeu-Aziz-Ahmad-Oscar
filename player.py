import pygame
from projectile import Heatvision


# class joueur
class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 40
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/superman.gif")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 570

    def damage(self,amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_health_bar(self, surface):
        # definir une couleur pour la barre de vie
        bar_color = (50, 200, 0)
        # arrier plan de la jauge
        back_bar_color = (255, 0, 35)
        # definir la position ,la largeur ,la longeur
        bar_position = [self.rect.x-20, self.rect.y+120, self.health, 5]
        # definir la position de l'arriere plan
        back_bar_position = [self.rect.x-20 , self.rect.y+120 , self.max_health, 5]
        # dessiner l'arriere plan
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # dessiner notre barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        self.all_projectiles.add(Heatvision(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

