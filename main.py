import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Football Pong")

score1 = 0
score1_img = pygame.image.load("score/0.png")
score2 = 0
score2_img = pygame.image.load("score/0.png")

field = pygame.image.load("assets/field.png")

player1 = pygame.image.load("assets/player1.png")
player1_y = 310
player1_moveup = False
player1_movedown = False

player2 = pygame.image.load("assets/player2.png")
player2_y = 310

ball = pygame.image.load("assets/ball.png")
ball_x = 617
ball_y = 337
ball_dir = -3
ball_dir_y = 1

clock = pygame.time.Clock()  # Para controlar os frames por segundo (FPS)

def move_player():
    global player1_y

    if player1_moveup:
        player1_y -= 10
    if player1_movedown:
        player1_y += 10

    if player1_y < 0:
        player1_y = 0
    elif player1_y > 575:
        player1_y = 575

def move_player2():
    global player2_y
    player2_y = ball_y

def move_ball():
    global ball_x, ball_y, ball_dir, ball_dir_y
    global score1, score1_img, score2, score2_img

    ball_x += ball_dir
    ball_y += ball_dir_y

    # Colisões com os jogadores
    if ball_x < 120:
        if player1_y < ball_y + 23 < player1_y + 146:
            ball_dir *= -1

    if ball_x > 1100:
        if player2_y < ball_y + 23 < player2_y + 146:
            ball_dir *= -1

    # Colisões com as bordas superior e inferior
    if ball_y > 685 or ball_y <= 0:
        ball_dir_y *= -1

    # Pontuação
    if ball_x < -50:
        ball_x, ball_y = 617, 337
        ball_dir_y *= -1
        ball_dir *= -1
        score2 += 1
        score2_img = pygame.image.load(f'score/{score2}.png')

    elif ball_x > 1320:
        ball_x, ball_y = 617, 337
        ball_dir_y *= -1
        ball_dir *= -1
        score1 += 1
        score1_img = pygame.image.load(f'score/{score1}.png')

def draw():
    window.blit(field, (0, 0))
    window.blit(player1, (50, player1_y))
    window.blit(player2, (1150, player2_y))
    window.blit(ball, (ball_x, ball_y))
    window.blit(score1_img, (500, 50))
    window.blit(score2_img, (710, 50))

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_moveup = True
            if event.key == pygame.K_s:
                player1_movedown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_moveup = False
            if event.key == pygame.K_s:
                player1_movedown = False

    draw()
    move_ball()
    move_player()
    move_player2()
    pygame.display.update()
    clock.tick(60)  # Define o FPS para 60

pygame.quit()