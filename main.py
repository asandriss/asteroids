import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatebles = pygame.sprite.Group()     
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (drawables, updatebles) 
    Asteroid.containers = (asteroids, drawables, updatebles)
    AsteroidField.containers = (updatebles)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        # player.update(dt)
        # player.draw(screen)

        for updateble in updatebles:
            updateble.update(dt)

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    

if __name__ == "__main__":
    main()
