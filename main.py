import pygame
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import *
from constants import *
from player import *
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000
        screen.fill("black")
        player.draw(screen)
        for sprite in drawable:
            if hasattr(sprite, "draw"):
                sprite.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if(asteroid.check_collision(player)):
                raise SystemExit("Game Over!")
        pygame.display.flip()
        

if __name__ == "__main__":
    main()