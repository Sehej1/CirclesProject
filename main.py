# Bubbles Challenge
import pygame
import random

pygame.init()

Width, Height = 1000, 650
surface = pygame.display.set_mode((Width, Height))


class Bubble:
    def __init__(self, x, y):
        self.colour1 = random.randint(0, 255)
        self.colour2 = random.randint(0, 255)
        self.colour3 = random.randint(0, 255)
        self.width = random.randint(7, 45)
        self.ySpeed = random.randint(4, 10)
        self.x = x
        self.y = y

    def move(self):
        self.y += self.ySpeed
        self.ySpeed += 0.25

        if self.y + (self.width / 2) >= Height:
            self.ySpeed -= 1
            self.ySpeed *= -1

    def draw(self):
        pygame.draw.circle(surface, (self.colour1, self.colour2, self.colour3), (self.x, self.y), self.width)


def main():
    run = True
    clock = pygame.time.Clock()
    lst = []

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                circle = Bubble(x, y)
                lst.append(circle)

        surface.fill((0, 0, 0))

        for i in range(len(lst)):
            i -= 1
            lst[i].move()
            lst[i].draw()

            if lst[i].y - lst[i].width >= Height:
                lst.pop(i)

        pygame.display.flip()
        clock.tick(120)

    pygame.quit()


main()
