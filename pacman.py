import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Лабиринт
maze = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "######.##### ## #####.######",
    "######.##          ##.######",
    "######.## ######## ##.######",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#...##................##...#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################",
]

# Класс для Pac-Man
class PacMan:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.direction = "STOP"

    def move(self):
        if self.direction == "UP" and maze[self.y - 1][self.x] != "#":
            self.y -= 1
        elif self.direction == "DOWN" and maze[self.y + 1][self.x] != "#":
            self.y += 1
        elif self.direction == "LEFT" and maze[self.y][self.x - 1] != "#":
            self.x -= 1
        elif self.direction == "RIGHT" and maze[self.y][self.x + 1] != "#":
            self.x += 1

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

# Класс для врагов
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def move(self):
        if self.direction == "UP" and maze[self.y - 1][self.x] != "#":
            self.y -= 1
        elif self.direction == "DOWN" and maze[self.y + 1][self.x] != "#":
            self.y += 1
        elif self.direction == "LEFT" and maze[self.y][self.x - 1] != "#":
            self.x -= 1
        elif self.direction == "RIGHT" and maze[self.y][self.x + 1] != "#":
            self.x += 1
        else:
            self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

# Функция для рисования лабиринта
def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "#":
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == ".":
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 3)

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()
    pacman = PacMan()
    enemies = [Enemy(10, 10), Enemy(15, 15), Enemy(20, 20)]  # Добавляем несколько врагов
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pacman.direction = "UP"
                elif event.key == pygame.K_DOWN:
                    pacman.direction = "DOWN"
                elif event.key == pygame.K_LEFT:
                    pacman.direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    pacman.direction = "RIGHT"

        pacman.move()

        # Проверка столкновения с точками
        if maze[pacman.y][pacman.x] == ".":
            maze[pacman.y] = maze[pacman.y][:pacman.x] + " " + maze[pacman.y][pacman.x + 1:]
            score += 1

        # Движение врагов
        for enemy in enemies:
            enemy.move()

        # Проверка столкновения с врагами
        for enemy in enemies:
            if pacman.x == enemy.x and pacman.y == enemy.y:
                running = False  # Игра заканчивается при столкновении

        screen.fill(BLACK)
        draw_maze()
        pacman.draw()

        for enemy in enemies:
            enemy.draw()

        # Отображение очков
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()