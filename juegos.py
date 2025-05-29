import pygame
import noise
import numpy as np
import random

# Configuración inicial
WIDTH, HEIGHT = 800, 600
SCALE = 50  # Tamaño de los píxeles del mapa
NPC_COUNT = 10

class NPC:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    
    def move(self):
        self.x = (self.x + random.choice([-1, 0, 1])) % WIDTH
        self.y = (self.y + random.choice([-1, 0, 1])) % HEIGHT
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 3)

def generate_terrain(width, height, scale):
    """Genera un mapa de terreno usando Perlin Noise."""
    terrain = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            terrain[x][y] = noise.pnoise2(x/scale, y/scale, octaves=6, persistence=0.5, lacunarity=2.0)
    return terrain

def draw_terrain(screen, terrain):
    """Dibuja el terreno en la pantalla."""
    for x in range(WIDTH):
        for y in range(HEIGHT):
            color_value = int((terrain[x][y] + 1) * 127)  # Normalizar entre 0 y 255
            color = (color_value, color_value, color_value)
            screen.set_at((x, y), color)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Generador de Terreno con NPCs")
    clock = pygame.time.Clock()
    
    terrain = generate_terrain(WIDTH, HEIGHT, SCALE)
    npcs = [NPC() for _ in range(NPC_COUNT)]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_terrain(screen, terrain)
        for npc in npcs:
            npc.move()
            npc.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()

