import pygame

class Tower(pygame.sprite.Sprite):
    def __init__ (self, position, color, damage, attack_speed, range_radius, cost):
        super().__init__()
        
        # PARAMETERS
        self.color = color
        self.damage = damage
        self.range_radius = range_radius
        self.cost = cost
        
        self.attack_speed = attack_speed
        #self.last_attack = pygame.time.get_ticks()
        self.cooldown_timer = 0
        
        # LOOKS
        self.image = pygame.Surface((40,40))
        self.image.fill(color)
        
        # POSITION
        self.rect = self.image.get_rect()
        self.rect.center = position
        
    def update(self):
        return
    
    def attack(self, enemies_group):
        
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1
            return None
        
        # look for the enemy
        for enemy in enemies_group:
            
            tower_position = pygame.math.Vector2(self.rect.center)
            enemy_position = enemy.position
            
            distance = tower_position.distance_to(enemy_position)
            
            # it's in the range 
            if distance <= self.range_radius:
                
                enemy.health_points -= self.damage
                self.cooldown_timer = self.attack_speed
                
                return enemy.rect.center
        return None
    
    def draw_range(self, screen):
        ''' gives player knowledge of how tower range will look like '''
        
        range_surface = pygame.Surface((self.range_radius * 2, self.range_radius * 2), pygame.SRCALPHA)
        
        # pygame.draw.circle(surface, color, center, radius, width)
        
        # transparent circle
        pygame.draw.circle(range_surface, (128,128,128,100), (self.range_radius, self.range_radius), self.range_radius)
        
        # visible border
        pygame.draw.circle(range_surface, (255,255,255), (self.range_radius, self.range_radius), self.range_radius, 2)
        
        # put it on the screen
        screen.blit(range_surface, (self.rect.centerx - self.range_radius, self.rect.centery - self.range_radius))