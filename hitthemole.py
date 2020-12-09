import pygame
import random
pygame.init()

# Display
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Hit the Mole')



# Entities
class Mole(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/mole1.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.sound = pygame.mixer.Sound('sounds/slip.wav')
        self.rect.left = random.randint(0, 620)
        self.rect.top = random.randint(0, 460)

    def flee(self):
        self.rect.left = random.randint(0, 620)
        self.rect.top = random.randint(0, 460)

    def cry(self):
        self.sound.play()

    def hit(self, pos):
        self.rect.collidepoint(pos)


class Shovel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/shovel.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


mole = Mole()
shovel = Shovel()


sprite_group = pygame.sprite.Group()
sprite_group.add(mole)
sprite_group.add(shovel)

bg = pygame.image.load('images/grass.jpg')
bg = pygame.transform.scale(bg, size)

bg_red = pygame.Surface(size)
bg_red = bg_red.convert()
bg_red.fill('red')

font = pygame.font.Font(None, 25)

# Action --> Alter

# Assign Variables


def main_loop():
    run = True
    ctr = 0
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 200)
    start_ticks = pygame.time.get_ticks()
    while run:
        # Timer
        clock.tick(30)

        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if seconds > 10:
            screen.fill("blue")
            text = font.render(u'Moles:' + str(ctr), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (400, 300)
            screen.blit(text, text_rect)
            text1 = font.render("Click anywhere to play again!", True, (255, 255, 255))
            text1_rect = text1.get_rect()
            text1_rect.center = (400, 320)
            screen.blit(text1, text1_rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main_loop()
                elif event.type == pygame.QUIT:
                    run = False

            # Event Handling Main Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.sprite.collide_rect(mole, shovel):
                    mole.cry()
                    ctr += 1
                    screen.blit(bg_red, (0, 0))
                    break
            elif event.type == pygame.USEREVENT:
                mole.flee()
                pygame.time.set_timer(pygame.USEREVENT, random.randint(500, 1000))
                screen.blit(bg, (0, 0))
                sprite_group.update()
                sprite_group.draw(screen)
                text = font.render(u'Moles:' + str(ctr), True, (255, 255, 255))
                screen.blit(text, (10, 230))

        sprite_group.update()
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()
    quit()
main_loop()



