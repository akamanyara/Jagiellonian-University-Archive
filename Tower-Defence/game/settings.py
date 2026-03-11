PLAYER_HEALTH = 10
PLAYER_MONEY = 100

# COLORS
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

PATH = [
    (0, 150),
    (300, 150),
    (300, 650),
    (500, 650),
    (500, 150),
    (900, 150),
    (900, 650),
    (1200, 650)
]

TOWER_DATA = {
    
    "Archer": { # lower damage, normal range
        "color": (255, 255, 100),       
        "damage": 3,               
        "attack_speed": 40,         
        "range": 130,               
        "cost": 50
    },
    
    "Sniper": { # high range, medium damage
        "color": (100, 255, 255),       
        "damage": 10,                
        "attack_speed": 120,         
        "range": 300,               
        "cost": 150
    },
    
    "Cannon": { # high damage, low range
        "color": (125, 125, 125),       
        "damage": 25,                
        "attack_speed": 150,         
        "range": 70,               
        "cost": 300
    },
}

ENEMY_DATA = {
    "basic": {
        "color": RED,
        "health": 15,
        "speed": 3,
        "reward": 50
    },
    "fast": {
        "color": BLUE,
        "health": 10,
        "speed": 7,
        "reward": 100
    },
    "tank": {
        "color": GREEN,
        "health": 50,
        "speed": 1,
        "reward": 200
    }
}

WAVES = [
    # POZIOM ŁATWY (1-5)
    ["basic", "basic", "basic"],                                            # Wave 1
    ["basic", "basic", "basic", "basic", "basic"],                          # Wave 2
    ["basic", "basic", "fast", "basic", "fast"],                            # Wave 3
    ["basic", "fast", "basic", "fast", "basic", "fast"],                    # Wave 4
    ["tank", "basic", "basic", "tank", "basic"],                            # Wave 5
    
    # POZIOM ŚREDNI (6-10)
    ["fast", "fast", "fast", "fast", "fast"],                               # Wave 6
    ["basic", "basic", "tank", "tank", "basic", "basic"],                   # Wave 7
    ["fast", "tank", "fast", "tank", "fast"],                               # Wave 8
    ["tank", "tank", "tank", "basic", "basic", "basic"],                    # Wave 9
    ["fast", "fast", "fast", "fast", "fast", "fast", "fast", "fast"],       # Wave 10
    
    # POZIOM TRUDNY (11-15)
    ["tank", "tank", "tank", "tank", "tank"],                               # Wave 11
    ["basic", "fast", "tank", "basic", "fast", "tank", "basic", "fast"],    # Wave 12
    ["fast", "fast", "fast", "fast", "fast", "fast", "fast", "fast", "fast", "fast"], # Wave 13
    ["tank", "tank", "fast", "fast", "tank", "tank", "fast", "fast"],       # Wave 14
    ["basic"] * 20,                                                         # Wave 15

    # POZIOM EKSTREMALNY (16-20)
    ["tank", "fast", "tank", "fast", "tank", "fast", "tank", "fast"],       # Wave 16
    ["tank", "tank", "tank", "tank", "tank", "tank", "tank", "tank"],       # Wave 17
    ["fast"] * 15,                                                          # Wave 18
    ["tank", "tank", "tank", "fast", "fast", "fast", "basic", "basic", "basic", "tank"], # Wave 19
    ["tank", "tank", "tank", "tank", "tank", "fast", "fast", "fast", "fast", "fast", "tank", "tank"] # Wave 20 (BOSS)
]

