import pygame
x = pygame.init()
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption('My First Snake Game')

# Game specific variables
exit_game = False
game_over = False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")
            if event.key == pygame.K_LEFT:
                print("You have pressed left arrow key")
            if event.key == pygame.K_UP:
                print("You have pressed up arrow key")
            if event.key == pygame.K_DOWN:
                print("You have pressed down arrow key")

pygame.quit()
quit()
