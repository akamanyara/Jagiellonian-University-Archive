import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, path, health_points, speed, enemy_type, reward):
        super().__init__()
        
        # enemy looks
        self.image = pygame.Surface((40,40)) # size 
        self.image.fill(color)
        
        # enemy position
        self.path = path
        self.target_index = 0
        
        start_x, start_y = self.path[0]
        
        self.position = pygame.math.Vector2(start_x, start_y) # for precision
        
        # drawing
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        
        # enemy stats
        self.health_points = health_points
        self.max_health = health_points
        self.speed = speed
        self.enemy_type = enemy_type
        self.reward = reward
        
        self.finished = False
    
    def update(self):
        self.move()
    
    def move(self):
        
        # check if the path is finished
        if self.target_index >= len(self.path):
            self.finished = True
            return
        
        target_point = self.path[self.target_index]
        target_vector = pygame.math.Vector2(target_point)
        
        direction_vector = target_vector - self.position
        distance = direction_vector.length() # distance from target
        
        # if enemy is close to target point
        if distance <= self.speed:
            self.target_index += 1
            
            if self.target_index >= len(self.path):
                self.finished = True
            else:
                self.position = target_vector
        
        # if enemy is far from target point (move)
        else:
            if distance > 0: # avoid the division by 0
                direction_vector = direction_vector.normalize()
            
            self.position += direction_vector * self.speed
            
        self.rect.center = self.position # graphics reset
        
    def draw_health_bar(self, screen):
        
        # count the hp %
        ratio = self.health_points / self.max_health
        
        bar_width = 40
        bar_height = 5
        
        # position above the enemy
        x = self.rect.x
        y = self.rect.y - 10
        
        # draw
        pygame.draw.rect(screen, (255,0,0), (x, y, bar_width, bar_height))
        pygame.draw.rect(screen, (0,255,0), (x, y, bar_width * ratio, bar_height))