import pygame
import random

class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.attack_laser = 5
        self.image = pygame.image.load("assets/spaceship.png")
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,950)
        self.rect.y = 0
        self.velocity = 1

    def damage(self, amount):
        # infliger des degats
        self.health -= amount
        if self.health <= 0:
            self.game.score += 1
            self.remove()

    def update_health_bar(self, surface):
        # definir une couleur pour la barre de vie
        bar_color = (50, 200, 0)

        # arrier plan de la jauge
        back_bar_color = (255, 0, 35)

        # definir la position ,la largeur ,la longeur
        bar_position = [self.rect.x-5, self.rect.y-20, self.health, 5]

        # definir la position de l'arriere plan
        back_bar_position = [self.rect.x-5 , self.rect.y - 20, self.max_health, 5]

        # dessiner l'arriere plan
        pygame.draw.rect(surface, back_bar_color, back_bar_position)

        # dessiner notre barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)

    def remove(self):
        self.game.all_monsters.remove(self)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity
        else:
            self.game.player.damage(self.attack)
        # appelle la fonction remove pour effacer le monstre
        if self.rect.y > 1000:
            self.game.score -= 1
            self.remove()


class Boss_monster(Monster):
    def __init__(self, game):
        super().__init__(game)
        self.health = 300
        self.max_health = 300
        self.attack = 1
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 950)
        self.rect.y = 0
        self.velocity = 1

    def damage(self, amount):
        # infliger des degats
        self.health -= amount
        if self.health <= 0:
            self.game.score += 5
            self.remove()

    def update_health_bar(self, surface):
        # definir une couleur pour la barre de vie
        bar_color = (50, 200, 0)
        # arrier plan de la jauge
        back_bar_color = (255, 0, 35)
        # definir la position ,la largeur ,la longeur
        bar_position = [self.rect.x-25, self.rect.y - 20, self.health/2, 10]
        # definir la position de l'arriere plan
        back_bar_position = [self.rect.x-25, self.rect.y - 20, self.max_health/2, 10]
        # dessiner l'arriere plan
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # dessiner notre barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)

    def remove(self):
        super().remove()

    def forward(self):
        super().forward()


class Kryptonite(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.attack = 20
        self.image = pygame.image.load("assets/kryptonite.gif")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 950)
        self.rect.y = 0
        self.velocity = random.randint(1,2)

    def remove(self):
        self.game.all_krypto.remove(self)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity
        else:
            self.remove()
            self.game.player.damage(self.attack)
        # appelle la fonction remove pour effacer le monstre
        if self.rect.y > 1000:
            self.remove()


class plus_health(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("assets/powerup.gif")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = 570

    def remove(self):
        self.game.all_power_up.remove(self)

    def effet(self):
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.health += 50
            self.remove()
            if self.game.player.health > 100:
                self.game.player.health = 100



