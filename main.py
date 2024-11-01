import pygame
import random
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
   
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

   
    # container groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    
    # setting class container groupings
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    pygame.init()

    #creating player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()
    #asteroid = (ASTEROID_MIN_RADIUS, ASTEROID_MIN_RADIUS)

    while ( True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        time = clock.tick(60) 
        dt = time/1000 


        for updateMe in updatable:
            updateMe.update(dt)
        for drawMe in drawable:
            drawMe.draw(screen)
       
        pygame.display.flip()
    
   
       

if __name__ == "__main__":
    main()
