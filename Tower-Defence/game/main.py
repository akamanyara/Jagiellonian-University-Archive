import sys
import pygame

from enemy import Enemy # enemy class
from tower import Tower
from settings import PLAYER_HEALTH, PLAYER_MONEY, WAVES, TOWER_DATA, PATH, ENEMY_DATA

# initialization
pygame.init()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

# window size 
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# window title 
pygame.display.set_caption("Tower deffence")

# fps control clock 
clock = pygame.time.Clock()

# font
font = pygame.font.SysFont(None, 36)

#!--------------------- ENEMIES -----------------------

enemies_group = pygame.sprite.Group()

current_wave = 0
is_in_progress = False # check if the wave is ON right now
wave_queue = []

last_spawn_time = pygame.time.get_ticks()
spawn_delay = 1000

def create_enemy(enemy_type):
    data = ENEMY_DATA.get(enemy_type, ENEMY_DATA["basic"]) # default is "basic"
    
    return Enemy(
        color=data["color"], 
        path=PATH, 
        health_points=data["health"], 
        speed=data["speed"], 
        enemy_type=enemy_type, 
        reward=data["reward"]
    )

#!--------------------- TOWERS -----------------------

towers_group = pygame.sprite.Group()

placing_mode = False
preview_tower_params = None # for tower stats

#!----------------------- UI -------------------------

SIDEBAR_WIDHT = 200
GAME_WIDHT = SCREEN_WIDTH - SIDEBAR_WIDHT

# defining shop buttons
shop_buttons = [
    {"type": "Archer", "rect": pygame.Rect(GAME_WIDHT + 20, 50, 160, 60)},    
    {"type": "Sniper", "rect": pygame.Rect(GAME_WIDHT + 20, 150, 160, 60)},
    {"type": "Cannon", "rect": pygame.Rect(GAME_WIDHT + 20, 300, 160, 60)}
]

#!---------------- MAIN GAME LOOP -------------------- 
running = True
while running:
    
    PHASE = 1
    
    # EVENT CONTROL
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # SPACE - start wave
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                if not is_in_progress and current_wave < len(WAVES):
                    
                    wave_queue = list(WAVES[current_wave])
                    
                    is_in_progress = True
                    print(f"start of the wave {current_wave + 1}")
        
        
        # MOUSE - place tower
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            if event.button == 1:
                
                # STEP 1. Choose tower from shop
                if mouse_pos[0] > GAME_WIDHT:
                    for button in shop_buttons:
                        if button["rect"].collidepoint(mouse_pos):
                            # player choosed the tower
                            tower_type = button["type"]
                            data = TOWER_DATA[tower_type]
                            
                            if PLAYER_MONEY >= data["cost"]:
                                placing_mode = True
                                preview_tower_params = data
                                print(f"choosed {tower_type}")
                            else:
                                print("not enough money")
                
                # STEP 2. Place tower
                elif placing_mode:
                    if mouse_pos[0] <= GAME_WIDHT:
                        new_tower = Tower(
                            position=mouse_pos,
                            color=preview_tower_params["color"],
                            damage=preview_tower_params["damage"],
                            attack_speed=preview_tower_params["attack_speed"],
                            range_radius=preview_tower_params["range"],
                            cost=preview_tower_params["cost"]
                        )
                        towers_group.add(new_tower)
                        PLAYER_MONEY -= preview_tower_params["cost"]
                        placing_mode = False
                
            # cancel building tower or sell tower
            if event.button == 3:
                if placing_mode:
                    placing_mode = False
                    print("Building cancelled")
                
                else:
                    for tower in towers_group:
                        if tower.rect.collidepoint(mouse_pos):
                            refund = int(tower.cost * 0.2) # 20% of tower value refunded while selling
                            PLAYER_MONEY += refund
                            tower.kill()
                            break
    # LOGIC
    # spawn enemies
    if is_in_progress:
        current_time = pygame.time.get_ticks()
        
        if len(wave_queue) > 0:
            if (current_time - last_spawn_time) > spawn_delay:
                enemy_type = wave_queue.pop(0)
                new_enemy = create_enemy(enemy_type)
                enemies_group.add(new_enemy)
                last_spawn_time = current_time
        
        # check if wave is finished
        if len(wave_queue) == 0 and len(enemies_group) == 0:
            is_in_progress = False
            current_wave += 1
            print("SPACE to start next wave!")   
    
    lasers_to_draw = []
    
    for tower in towers_group:
        target_position = tower.attack(enemies_group)
        
        if target_position:
            # draw the attack line (start -> end)
            lasers_to_draw.append((tower.rect.center, target_position))
    
    enemies_group.update()
    
    for enemy in enemies_group:
        
        if enemy.finished:
            PLAYER_HEALTH -= 1
            enemy.kill()
            
            if PLAYER_HEALTH <= 0:
                print("GAME OVER!")
                running = False
        
        if enemy.health_points <= 0:
            PLAYER_MONEY += enemy.reward
            enemy.kill() 
            print("enemy killed")
                
    # DRAW 
    
    screen.fill(BLACK)   
    pygame.draw.lines(screen, WHITE, False, PATH, 50) # where, color, if closed, points, thickness
    pygame.draw.rect(screen, (25,25,25), (GAME_WIDHT, 0, SIDEBAR_WIDHT, SCREEN_HEIGHT))
    
    for button in shop_buttons:
        # button colour 
        pygame.draw.rect(screen, (100,100,100), button["rect"])
        
        # towers
        text_surface = font.render(button["type"], True, WHITE)
        text_rect = text_surface.get_rect(center=button["rect"].center)
        screen.blit(text_surface, text_rect)
    
    enemies_group.draw(screen)
    
    for enemy in enemies_group:
        enemy.draw_health_bar(screen)
    
    for tower in towers_group:
        tower.draw_range(screen)
    towers_group.draw(screen)
    
    for start_pos, end_pos in lasers_to_draw:
        pygame.draw.line(screen, (255,0,200), start_pos, end_pos, 2)
    
    if placing_mode:
        mouse_pos = pygame.mouse.get_pos()
        
        # draw range
        range_radius = preview_tower_params["range"]
        pygame.draw.circle(screen, (100,100,100), mouse_pos, range_radius, 1)
        
        # draw tower
        ghost_rect = pygame.Rect(0,0,40,40)
        ghost_rect.center = mouse_pos
        pygame.draw.rect(screen, preview_tower_params["color"], ghost_rect) 
    
    money_info = font.render(f"CASH: {PLAYER_MONEY}", True, WHITE)
    screen.blit(money_info, (1000,10))
    
    health_info = font.render(f"HP: {PLAYER_HEALTH}", True, WHITE)
    screen.blit(health_info, (10,10)) # show health info at the left corner 

    # wave info
    if current_wave < len(WAVES):
        if not is_in_progress:
            msg = f"Wave {current_wave+1}! Press SPACE to start."
        else:
            msg = F"Wave {current_wave+1}"
    else:
        msg = "Congratz! Finished all waves :D"

    wave_info = font.render(msg, True, WHITE)
    screen.blit(wave_info, (400,10))
    
    
    pygame.display.flip()
    clock.tick(60) # max 60 fps
    
# quit
pygame.quit()
sys.exit()