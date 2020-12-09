''' High Score Screen

This screen is shown at end of game after pressing on scoreboard button.
Takes data from other_data/highscores.txt and creates a score board of top 10 players.

'''

import pygame
from classes.generalfunctions import quitGame
from classes.text import Text
from classes.menu import Button
from classes.menu import Menu
from operator import itemgetter

background = pygame.image.load('graphics\menu\scoreboard.png')

def scoreBoard(screen, delay, scorelist):

    clock = pygame.time.Clock()
    width = screen.get_width()
    height = screen.get_height()

    list = scorelist

    Header = Text(screen, (width // 2, height // 8), 50, f'PLAYER TOP 10 SCORE')
    player1 = Text(screen, (width // 2, 120), 35, f'{list[-1][0]} = {list[-1][1]}')
    player2 = Text(screen, (width // 2, 160), 35, f'{list[-2][0]} = {list[-2][1]}')
    player3 = Text(screen, (width // 2, 200), 35, f'{list[-3][0]} = {list[-3][1]}')
    player4 = Text(screen, (width // 2, 240), 35, f'{list[-4][0]} = {list[-4][1]}')
    player5 = Text(screen, (width // 2, 280), 35, f'{list[-5][0]} = {list[-5][1]}')
    player6 = Text(screen, (width // 2, 320), 35, f'{list[-6][0]} = {list[-6][1]}')
    player7 = Text(screen, (width // 2, 360), 35, f'{list[-7][0]} = {list[-7][1]}')
    player8 = Text(screen, (width // 2, 400), 35, f'{list[-8][0]} = {list[-8][1]}')
    player9 = Text(screen, (width // 2, 440), 35, f'{list[-9][0]} = {list[-9][1]}')
    player10 = Text(screen, (width // 2, 480), 35, f'{list[-10][0]} = {list[-10][1]}')

    back = Button(screen, 'Back', (400, 585), (lambda: 'go_back'), 25, (126, 64))
    sample_menu = Menu(screen, Header, False, back)

    run = True
    while run:
        clock.tick(delay)

        for event in pygame.event.get():
            # Send each event to the start menu

            if event.type == pygame.QUIT:
                # Detecting user pressing quit button, if X pressed,
                # break loop and quit screen.
                quitGame()

            elif (event.type == pygame.MOUSEBUTTONDOWN) or \
                (event.type == pygame.MOUSEBUTTONUP):

                button_press = sample_menu.do(event)

                if button_press == 'go_back':
                    run = False

        screen.blit(background, (0, 0))
        Header.display()
        player1.display()
        player2.display()
        player3.display()
        player4.display()
        player5.display()
        player6.display()
        player7.display()
        player8.display()
        player9.display()
        player10.display()
        sample_menu.display()
        pygame.display.flip()

