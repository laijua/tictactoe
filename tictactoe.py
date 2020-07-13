#  image for the x and o from https://www.geeksforgeeks.org/tic-tac-toe-gui-in-python-using-pygame/
#  tile used for tic tac toe from https://www.youtube.com/watch?v=Gv8hsNsX5G4
import pygame

pygame.init()
window = pygame.display.set_mode((550, 550))
pygame.display.set_caption('Tic-Tac-Toe')

first = pygame.draw.rect(window, (255, 255, 255), (25, 25, 150, 150))
second = pygame.draw.rect(window, (255, 255, 255), (200, 25, 150, 150))
third = pygame.draw.rect(window, (255, 255, 255), (375, 25, 150, 150))

fourth = pygame.draw.rect(window, (255, 255, 255), (25, 200, 150, 150))
fifth = pygame.draw.rect(window, (255, 255, 255), (200, 200, 150, 150))
sixth = pygame.draw.rect(window, (255, 255, 255), (375, 200, 150, 150))

seventh = pygame.draw.rect(window, (255, 255, 255), (25, 375, 150, 150))
eighth = pygame.draw.rect(window, (255, 255, 255), (200, 375, 150, 150))
ninth = pygame.draw.rect(window, (255, 255, 255), (375, 375, 150, 150))

x_img = image = pygame.image.load('x.png')
o_img = image = pygame.image.load('o.png')

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
retry_text = myfont.render('Retry', False, (255, 255, 255))

board = []
for i in range(3):
    board += [[None] * 3]


def reset():
    board_temp = []
    for i in range(3):
        board_temp += [[None] * 3]
    global board
    board = board_temp

    pygame.draw.rect(window, (255, 255, 255), (25, 25, 150, 150))
    pygame.draw.rect(window, (255, 255, 255), (200, 25, 150, 150))
    pygame.draw.rect(window, (255, 255, 255), (375, 25, 150, 150))

    pygame.draw.rect(window, (255, 255, 255), (25, 200, 150, 150))
    pygame.draw.rect(window, (255, 255, 255), (200, 200, 150, 150))
    pygame.draw.rect(window, (255, 255, 255), (375, 200, 150, 150))

    pygame.draw.rect(window, (255, 255, 255), (25, 375, 150, 150))
    pygame.draw.rect(window, (255, 255, 255), (200, 375, 150, 150))
    pygame.draw.rect(window, (255, 255, 255), (375, 375, 150, 150))


def win(side, x, y):
    a = [(1, 1), (0, 1), (-1, 1), (1, 0)]
    for element in a:
        if 0 <= x + element[0] <= 2 and 0 <= x - element[0] <= 2 and 0 <= y + element[1] <= 2 and 0 <= y - element[
            1] <= 2:
            if board[x + element[0]][y + element[1]] == side and board[x - element[0]][y - element[1]] == side:
                return True

    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + 2 * i <= 2 and 0 <= y + 2 * j <= 2 and (i != 0 or j != 0):
                if board[x + i][y + j] == side and board[x + 2 * i][y + 2 * j] == side:
                    return True

    return False


def retry(event):
    retry_rec = pygame.draw.rect(window, (0, 0, 0), (200, 245, 150, 90))
    window.blit(retry_text, (235, 245))
    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        if retry_rec.collidepoint(pos):
            reset()
            game()


def game():
    quit = False
    x_turn = True
    gameover = False

    def side_swap():
        nonlocal x_turn
        if x_turn:
            x_turn = False
        else:
            x_turn = True

    def place(i, j, x, y, side):
        if side == 'x':
            board[i][j] = side
            window.blit(x_img, (x, y))
        else:
            board[i][j] = side
            window.blit(o_img, (x, y))

        if win(side, i, j):
            nonlocal gameover
            gameover = True

    while not quit:
        if x_turn:
            side = 'x'
        else:
            side = 'o'

        # pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if not gameover:
                    if first.collidepoint(pos):
                        if board[0][0] is None:
                            place(0, 0, 50, 50, side)
                            side_swap()

                    elif second.collidepoint(pos):
                        if board[0][1] is None:
                            place(0, 1, 225, 50, side)
                            side_swap()

                    elif third.collidepoint(pos):
                        if board[0][2] is None:
                            place(0, 2, 400, 50, side)
                            side_swap()

                    elif fourth.collidepoint(pos):
                        if board[1][0] is None:
                            place(1, 0, 50, 225, side)
                            side_swap()

                    elif fifth.collidepoint(pos):
                        if board[1][1] is None:
                            place(1, 1, 225, 225, side)
                            side_swap()

                    elif sixth.collidepoint(pos):
                        if board[1][2] is None:
                            place(1, 2, 400, 225, side)
                            side_swap()

                    elif seventh.collidepoint(pos):
                        if board[2][0] is None:
                            place(2, 0, 50, 400, side)
                            side_swap()

                    elif eighth.collidepoint(pos):
                        if board[2][1] is None:
                            place(2, 1, 225, 400, side)
                            side_swap()

                    elif ninth.collidepoint(pos):
                        if board[2][2] is None:
                            place(2, 2, 400, 400, side)
                            side_swap()

                    full = True
                    for row in board:
                        for element in row:
                            if element is None:
                                full = False
                    if full:
                        gameover = True

            if gameover:
                retry(event)

        pygame.display.update()


game()
pygame.quit()
