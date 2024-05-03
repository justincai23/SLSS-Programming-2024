# Intro to Pygame
#    - boilerplate
#    - Sprite class

import pygame

WIDTH = 1280  # Pixels
HEIGHT = 760
SCREEN_SIZE = (WIDTH, HEIGHT)


class Dvdlogo(pygame.sprite.Sprite):
    """Represents the DVD Logo"""

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("/Users/jc000746/Desktop/Screenshot 2024-04-26 at 11.52.24 AM.png")

        # sets the x and y to 0
        #    first position of the image is in the top right
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2

        # How much position changes over time
        #    - pixels per tick
        self.vel_x = 3
        self.vel_y = 3

    def update(self):
        # Update position of Dvdlogo
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Keep the Dvdlogo in the screen
        # Right side of the screen
        #     - if the right edge of dvdlogo > WIDTH
        #          - switch the direction (+vel-x -> -vel-x)
        if self.rect.right >= WIDTH:
            self.vel_x = -self.vel_x
        if self.rect.left <= 0:
            self.vel_x = -self.vel_x
        if self.rect.bottom >= HEIGHT:
            self.vel_y = -self.vel_y
        if self.rect.top <= 0:
            self.vel_y = -self.vel_y

        # Top side
        # Bottom side

        print(self.rect.x, self.rect.y)


def start():
    """Environment Setup and Game Loop"""

    pygame.init()

    # --CONSTANTS--
    # COLOURS
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    EMERALD = (21, 219, 147)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GRAY = (128, 128, 128)

    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    dvdlogo = Dvdlogo()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(dvdlogo)

    pygame.display.set_caption("DVD Screen Saver")

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Update the world state
        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()

class Box:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def display(self):
        print("Box position:", self.x, self.y)
        print("Box dimensions:", self.width, "x", self.height)

class BouncingBox(Box):
    def __init__(self, x, y, width, height, dx, dy):
        super().__init__(x, y, width, height)
        self.dx = dx  # Horizontal velocity
        self.dy = dy  # Vertical velocity

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def check_boundary(self, max_width, max_height):
        # Check if the box hits the boundaries and change direction
        if self.x <= 0 or self.x + self.width >= max_width:
            self.dx *= -1  # Reverse horizontal direction
        if self.y <= 0 or self.y + self.height >= max_height:
            self.dy *= -1  # Reverse vertical direction

# Example usage
bouncing_box = BouncingBox(10, 10, 20, 10, 1, 1)  # Starting at (10, 10) with a velocity of (1, 1)
for _ in range(20):
    bouncing_box.move()
    bouncing_box.check_boundary(30, 20)  # Assuming maximum width and height
    bouncing_box.display()