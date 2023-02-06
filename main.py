from enum import Enum

import pygame
import os

pygame.mixer.init()

FPS = 60

WIDTH, HEIGHT = 640, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnakeGame!")

CELL_SIZE = 64

SNAKE_SPEED = 2
MOVE_TIME = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_TIME, int(2000 / SNAKE_SPEED))

PICKUP_SOUND = pygame.mixer.Sound(os.path.join("Assets", "pickup.wav"))
HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "hit.wav"))

GRASS_IMAGE = pygame.image.load(os.path.join("Assets", "grass.png"))
FENCE_IMAGE = pygame.image.load(os.path.join("Assets", "fence_straight.png"))
ANGLED_FENCE_IMAGE = pygame.image.load(os.path.join("Assets", "fence_angled.png"))
SNAKE_HEAD_IMAGE = pygame.image.load(os.path.join("Assets", "snake_head.png"))
SNAKE_BODY_IMAGE = pygame.image.load(os.path.join("Assets", "snake_body.png"))
YAMMY_IMAGE = pygame.image.load(os.path.join("Assets", "yammy.png"))


class Direction(Enum):
    NONE = 0
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4


class EntityType(Enum):
    NONE = 0
    GRASS = 1
    FENCE = 2
    ANGLED_FENCE = 3
    SNAKE_HEAD = 4
    SNAKE_BODY = 5
    YAMMY = 6


class Entity:
    x = None
    y = None
    direction = Direction.UP
    image = None
    entityType = None

    def __init__(self, x, y, direction=Direction.UP, entityType=EntityType.NONE):
        self.x = x
        self.y = y
        self.entityType = entityType

        if self.entityType == EntityType.GRASS:
            self.image = GRASS_IMAGE
        elif self.entityType == EntityType.FENCE:
            self.image = FENCE_IMAGE
        elif self.entityType == EntityType.ANGLED_FENCE:
            self.image = ANGLED_FENCE_IMAGE
        elif self.entityType == EntityType.SNAKE_HEAD:
            self.image = SNAKE_HEAD_IMAGE
        elif self.entityType == EntityType.SNAKE_BODY:
            self.image = SNAKE_BODY_IMAGE
        elif self.entityType == EntityType.YAMMY:
            self.image = YAMMY_IMAGE

        self.change_direction(direction)

    def change_direction(self, direction):
        # When direction changes, entity image rotates
        rotation_angle = 90 * (self.direction.value - direction.value)
        self.image = pygame.transform.rotate(self.image, rotation_angle)
        self.direction = direction

    def move_to(self, x_pos, y_pos):
        # Defining the direction possible only in horizontal/vertical moving
        if self.x == x_pos or self.y == y_pos:
            if x_pos > self.x:
                self.change_direction(Direction.RIGHT)
            if x_pos < self.x:
                self.change_direction(Direction.LEFT)
            if y_pos > self.y:
                self.change_direction(Direction.DOWN)
            if y_pos < self.y:
                self.change_direction(Direction.UP)

        self.x, self.y = x_pos, y_pos


class Snake:
    head = None
    body = None

    def __init__(self, x=1, y=1, direction=Direction.RIGHT):
        self.head = Entity(x, y, direction, EntityType.SNAKE_HEAD)
        self.body = []

    def move(self):
        if self.head.direction == Direction.RIGHT:
            self.head.x += 1
        elif self.head.direction == Direction.LEFT:
            self.head.x -= 1
        elif self.head.direction == Direction.DOWN:
            self.head.y += 1
        elif self.head.direction == Direction.UP:
            self.head.y -= 1


class GameField:
    cells = None
    snake = None

    def __init__(self, snake: Snake):
        self.cells = [[None for i in range(10)] for i in range(10)]
        self.snake = snake

        for x in range(10):
            for y in range(10):
                if x in [0, 9]:
                    if y == 0 and x == 0:
                        temp = Entity(x, y, Direction.UP, EntityType.ANGLED_FENCE)
                    elif y == 0 and x == 9:
                        temp = Entity(x, y, Direction.RIGHT, EntityType.ANGLED_FENCE)
                    elif y == 9 and x == 9:
                        temp = Entity(x, y, Direction.DOWN, EntityType.ANGLED_FENCE)
                    elif y == 9 and x == 0:
                        temp = Entity(x, y, Direction.LEFT, EntityType.ANGLED_FENCE)
                    else:
                        temp = Entity(x, y, Direction.UP, EntityType.FENCE)
                elif y in [0, 9]:
                    temp = Entity(x, y, Direction.RIGHT, EntityType.FENCE)
                else:
                    temp = Entity(x, y, Direction.UP, EntityType.GRASS)
                self.cells[x][y] = temp

            self.cells[snake.head.x][snake.head.y] = snake.head
            for body_part in snake.body:
                self.cells[body_part.x][body_part.y] = body_part

    def update_snake(self):
        self.cells[self.snake.head.x][self.snake.head.y] = self.snake.head
        for body_part in self.snake.body:
            self.cells[body_part.x][body_part.y] = body_part



def draw_window(game_field: GameField):
    for cells in game_field.cells:
        for cell in cells:
            WIN.blit(cell.image, (cell.x * CELL_SIZE, cell.y * CELL_SIZE))
    pygame.display.update()


def main():
    snake = Snake()
    gameField = GameField(snake)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            # Quitting the game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_a, pygame.K_LEFT]:
                    snake.head.change_direction(Direction.LEFT)
                if event.key in [pygame.K_w, pygame.K_UP]:
                    snake.head.change_direction(Direction.UP)
                if event.key in [pygame.K_d, pygame.K_RIGHT]:
                    snake.head.change_direction(Direction.RIGHT)
                if event.key in [pygame.K_s, pygame.K_DOWN]:
                    snake.head.change_direction(Direction.DOWN)
            # Moving the snake
            # This event occurs each 2000 / SNAKE_SPEED ms
            if event.type == MOVE_TIME:
                snake.move()
                gameField.__init__(snake)

        draw_window(gameField)


if __name__ == "__main__":
    main()