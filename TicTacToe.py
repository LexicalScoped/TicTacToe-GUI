import pygame # type: ignore

from Game import Game

# vars
Height = 400
Width = 400
Run_Game = True
White = (255, 255, 255)
Black = (0, 0, 0)

# Pygame init code
pygame.init()

screen = pygame.display.set_mode((Width, Height + 100))
pygame.display.set_caption("TicTacToe - By LexicalScoped")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)


# game / pygame mixed functions
g = Game()

def draw_board(g):
    Menu = "Press N to reset/new game - press q to quit."
    screen.blit(font.render(Menu, True, Black), (10,10))
    if g.State and g.Win == " ":
        TurnStr = "It is " + g.Turn + "'s Turn."
    elif g.Win != " ": 
        TurnStr = "Congratulations - " + g.Win + " wins!"
    else: 
        TurnStr = "Out of moves."
    screen.blit(font.render(TurnStr, True, Black), (10,40))
    
    screen.blit(font.render(str(g.Board[0][0]), True, Black), (90,190))
    screen.blit(font.render(str(g.Board[0][1]), True, Black), (200,190))
    screen.blit(font.render(str(g.Board[0][2]), True, Black), (300,190))
    pygame.draw.line(screen, Black, (50,250), (350,250))
    screen.blit(font.render(str(g.Board[1][0]), True, Black), (90,290))
    screen.blit(font.render(str(g.Board[1][1]), True, Black), (200,290))
    screen.blit(font.render(str(g.Board[1][2]), True, Black), (300,290))
    pygame.draw.line(screen, Black, (50,350), (350,350))
    screen.blit(font.render(str(g.Board[2][0]), True, Black), (90,390))
    screen.blit(font.render(str(g.Board[2][1]), True, Black), (200,390))
    screen.blit(font.render(str(g.Board[2][2]), True, Black), (300,390))
    pygame.draw.line(screen, Black, (150,150), (150, 450))
    pygame.draw.line(screen, Black, (250,150), (250, 450))


while Run_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run_Game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if g.Win == " ":
                if (event.pos[0] in range(50,150) and event.pos[1] in range(150,250)):
                    g.validate_values(0, 0)
                if (event.pos[0] in range(151,250) and event.pos[1] in range(150,250)):
                    g.validate_values(0, 1)
                if (event.pos[0] in range(251,350) and event.pos[1] in range(150,250)):
                    g.validate_values(0, 2)
                if (event.pos[0] in range(50,150) and event.pos[1] in range(251,350)):
                    g.validate_values(1, 0)
                if (event.pos[0] in range(151,250) and event.pos[1] in range(251,350)):
                    g.validate_values(1, 1)
                if (event.pos[0] in range(251,350) and event.pos[1] in range(251,350)):
                    g.validate_values(1, 2)
                if (event.pos[0] in range(50,150) and event.pos[1] in range(350,450)):
                    g.validate_values(2, 0)
                if (event.pos[0] in range(151,250) and event.pos[1] in range(350,450)):
                    g.validate_values(2, 1)
                if (event.pos[0] in range(251,350) and event.pos[1] in range(350,450)):
                    g.validate_values(2, 2)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                g.reset_game()
            if event.key == pygame.K_q:
                Run_Game = False

    screen.fill(White)

    draw_board(g)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
