import pygame
import random

# 定义屏幕大小和方格大小
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 20

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 初始化Pygame
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("贪食蛇游戏")

# 定义贪食蛇的初始位置和长度
snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
snake_length = 1

# 定义贪食蛇的初始移动方向
direction = (0, -GRID_SIZE)

# 生成食物的初始位置
food = (random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
        random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

# 设置游戏时钟
clock = pygame.time.Clock()

# 定义游戏结束的标志
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # 获取键盘输入，控制贪食蛇移动方向
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != (GRID_SIZE, 0):
        direction = (-GRID_SIZE, 0)
    elif keys[pygame.K_RIGHT] and direction != (-GRID_SIZE, 0):
        direction = (GRID_SIZE, 0)
    elif keys[pygame.K_UP] and direction != (0, GRID_SIZE):
        direction = (0, -GRID_SIZE)
    elif keys[pygame.K_DOWN] and direction != (0, -GRID_SIZE):
        direction = (0, GRID_SIZE)

    # 更新贪食蛇的位置
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = ((head_x + dx) % SCREEN_WIDTH, (head_y + dy) % SCREEN_HEIGHT)
    snake.insert(0, new_head)

    # 判断是否吃到食物
    if snake[0] == food:
        snake_length += 1
        food = (random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
    
    # 控制贪食蛇长度
    if len(snake) > snake_length:
        snake.pop()

    # 绘制游戏画面
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (food[0], food[1], GRID_SIZE, GRID_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # 刷新屏幕
    pygame.display.flip()

    # 控制游戏速度
    clock.tick(10)

# 退出游戏
pygame.quit()
