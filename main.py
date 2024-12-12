import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from circleshape import CircleShape

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	game_clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable)
	asteroidfield = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		pygame.Surface.fill(screen, "black")
		
		for thing in updatable:
			thing.update(dt)

		for thing in asteroids:
			if (thing.collision(player)):
				print("Game over!")
				return

		for thing in drawable:
			thing.draw(screen)
		
		pygame.display.flip()
		delta_time = game_clock.tick(60)
		dt = delta_time / 1000

if __name__ == "__main__":
	main()
