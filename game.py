import pygame

pygame.init() # инициализируем
win = pygame.display.set_mode((500, 500)) # задаем размер экрана

pygame.display.set_caption("MEKAN GAME")  #Текст вспылающий при входе на экран
"""
Создаем 5 переменных, 
характеристика игрока его расположение, высота и ширина а так же его скорость
"""
walkleft = [pygame.image.load('pygame_left_1.png'),
pygame.image.load('pygame_left_2.png'), pygame.image.load('pygame_left_3.png'),
pygame.image.load('pygame_left_4.png'), pygame.image.load('pygame_left_5.png'),
pygame.image.load('pygame_left_6.png')]

walkright = [pygame.image.load('pygame_right_1.png'),
pygame.image.load('pygame_right_2.png'), pygame.image.load('pygame_right_3.png'),
pygame.image.load('pygame_right_4.png'), pygame.image.load('pygame_right_5.png'),
pygame.image.load('pygame_right_6.png')]

bg = pygame.image.load('pygame_bg.jpg')
playerStand = pygame.image.load('pygame_idle.png')

clock = pygame.time.Clock()

x = 50
y = 425
width = 60
height = 71
speed = 5

isJump = False
JumpCount = 10

left = False
right = False
animCount = 0

def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkleft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkright[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    pygame.display.update()

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()   #скорость передвежение
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
        right = True
        left = False
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if JumpCount >= -10:
            if JumpCount < 0:
                y += (JumpCount ** 2) / 2
            else:
                y -= (JumpCount ** 2) / 2
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10
    win.fill((0, 0, 0))  # после передвежение не остовляет следы

    drawWindow()

pygame.quit()