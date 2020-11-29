import pygame
import random
from player import Player
from monster import Monster, Boss_monster, Kryptonite, plus_health

# class qui represente le jeu
class Game:
    def __init__(self):
        self.is_playing = False
        # Generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.monster = Monster(self)
        self.all_players.add(self.player)
        # Groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        # Permet de faire spawn les monstres aléatoirement
        self.tic = 0
        self.score = 0
        self.score_boss_spawn = 0
        # kryptonite
        self.all_krypto = pygame.sprite.Group()
        # Power up
        self.all_power_up = pygame.sprite.Group()
        # boss
        self.boss_mode = False



    def game_start(self):
        self.is_playing = True

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.all_power_up = pygame.sprite.Group()
        self.all_krypto = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        self.score_boss_spawn = 0
        self.player.rect.x = 400
        self.player.rect.y = 500

    def update(self, screen):
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # affichage du score
        font = pygame.font.Font("freesansbold.ttf", 32)
        score_fond = font.render("Score : " + str(self.score), True, (255,255,255))
        screen.blit(score_fond, (10,10))

        # apparition des monstres et kryptonite aléatoire
        self.tic += 1
        if self.tic == 100:
            rand = random.randint(0, 100)
            self.tic = 0
            if rand > 85-(5*self.score_boss_spawn) and len(self.all_monsters)+len(self.all_krypto) < 10:
                self.spawn_monster()
            elif rand > 50-(5*self.score_boss_spawn) and len(self.all_monsters)+len(self.all_krypto) < 10:
                self.spawn_kryptonite()
            elif rand < 3 and len(self.all_power_up) < 3:
                self.spawn_power_up()

        # apparition des boss
        if self.score % 10 == 0 and self.score-(10*self.score_boss_spawn) != 0:
            self.spawn_boss()
            self.score_boss_spawn += 1

        # vie du joueur
        self.player.update_health_bar(screen)

        # mouvement des projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # mouvement des monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # mouvement des krypto
        for kryptonite in self.all_krypto:
            kryptonite.forward()

        # effet du power up
        for plus_health in self.all_power_up:
            plus_health.effet()

        # appliquer l'image de mes projectiles
        self.player.all_projectiles.draw(screen)

        # les image de mon groupe de monstre
        self.all_monsters.draw(screen)

        # celles des krypto
        self.all_krypto.draw(screen)

        # celles du power_up
        self.all_power_up.draw(screen)

        # Direction du joueur
        # Droite, Gauche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1010:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    # verifier les colistion
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite,group, False, pygame.sprite.collide_mask)

    # spawn des monstres
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    # spawn du boss
    def spawn_boss(self):
        boss = Boss_monster(self)
        self.all_monsters.add(boss)

    # spawn des krypto
    def spawn_kryptonite(self):
        kryptonite = Kryptonite(self)
        self.all_krypto.add(kryptonite)

    # spawn power up
    def spawn_power_up(self):
        power_up = plus_health(self)
        self.all_power_up.add(power_up)
