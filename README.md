# SnakeGame
**SnakeGame** is a simple game-project created by using [PyGame](https://www.pygame.org/news).

## Details
### Libraries
<details>
  <summary>📚 Click to see libraries were additionaly used in this project</summary>
  
  - **enum** *used to create custom Enum classes*
    <details>
        <summary>Click to see code</summary>
        
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
    </details>
    
  - **random** *used to randomly place yammy*
    <details>
        <summary>Click to see code</summary>
        
        def get_random_free_coordinates(self):
            x, y = 0, 0
            while self.cells[x][y].entityType != EntityType.GRASS:
                x, y = randint(1, 8), randint(1, 8)
            return x, y
    </details>
    
  - **os** *used to correctly define assets path regardless of operating system*
    <details>
        <summary>Click to see code</summary>
        
        PICKUP_SOUND = pygame.mixer.Sound(os.path.join("Assets", "pickup.wav"))
        HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "hit.wav"))

        GRASS_IMAGE = pygame.image.load(os.path.join("Assets", "grass.png"))
        FENCE_IMAGE = pygame.image.load(os.path.join("Assets", "fence_straight.png"))
        ANGLED_FENCE_IMAGE = pygame.image.load(os.path.join("Assets", "fence_angled.png"))
        SNAKE_HEAD_IMAGE = pygame.image.load(os.path.join("Assets", "snake_head.png"))
        SNAKE_HEAD_DEAD_IMAGE = pygame.image.load(os.path.join("Assets", "snake_head_dead.png"))
        SNAKE_BODY_IMAGE = pygame.image.load(os.path.join("Assets", "snake_body.png"))
        YAMMY_IMAGE = pygame.image.load(os.path.join("Assets", "yammy.png"))
    </details>

 </details>

### Game Assets
All the assets were drawn by myself. Each asset matches the **64*64** size.
<details>
  <summary>🖼️ Click to see Assets</summary>
  
  - grass.png
  
    ![grass](/Assets/grass.png)
   
  - fence_angled.png
  
    ![fence_angled](/Assets/fence_angled.png)
  
  - fence_straight.png
  
    ![fence_straight](/Assets/fence_straight.png)
  
  - snake_head.png
  
    ![snake_head](/Assets/snake_head.png)

  - snake_head_dead.png
  
    ![snake_head_dead](/Assets/snake_head_dead.png)
  
  - snake_body.png
  
    ![snake_body](/Assets/snake_body.png)

  - yammy.png
  
    ![Yammy](/Assets/yammy.png)
</details>

## Game Preview
![snake](https://user-images.githubusercontent.com/59295777/217119621-a8ffee4e-f45a-4b56-b336-c2a33275dcc9.gif)

## TODO/Ideas
- End screen
- Win screen
- Angled snake
- Score system
