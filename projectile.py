import pygame


# projectile de bases
class Heatvision(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("assets/heatvision.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 15
        self.rect.y = player.rect.y
        self.origin_image = self.image

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.velocity
        # verifier la colisions avec les monstres
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
        # infliger des degat
            monster.damage(self.player.attack)
        # detruir si il sort de l'ecran grace a la fonction remove
        if self.rect.y < 0:
            self.remove()
        # verifie la colisions avec la krypto
        if self.player.game.check_collision(self, self.player.game.all_krypto):
            self.remove()

