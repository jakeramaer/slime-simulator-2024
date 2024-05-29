import pygame
import numpy as np
import math

from pygame import key

# TODO:
# 1. pixel size
# 2. modulo vs collision with wall?
# 3. real time parameter input

# Parameters #####################################################################

width = 200
height = 150
grid_size = 4
show_dots = False
show_sensors = False
radius = 100
n = 100
col = np.array([255,255,255])
decay_rate = 0.18
sensitivity = 0.19
max_deposit = 10
deposit_amount = 8
dots = []
grid = np.zeros([width, height])
food = np.zeros([width, height])

# for i in range(50, 60):
#     for j in range(50, 60):
#         food[i, j] = 1.0

# Class definitions ##############################################################

class dot:
    def __init__(self, id, pos, angle, col):
        self.id = id
        self.pos = pos
        self.angle = angle
        self.vel = [math.cos(self.angle), math.sin(self.angle)]
        self.radius = 5
        self.col = col

        self.sensor_size = 2
        self.sensor_angle = 30
        self.sensor_distance = 3

    def get_deposits(self, grid, x, y, w, h):
        deposits = 0
        for i in range(x, x+w):
            for j in range(y, y+h):
                if 0 < i < width and 0 < j < height: 
                    deposits += grid[i, j]

        if show_sensors:
            rect = pygame.Rect(
                x * grid_size, y * grid_size, w * grid_size, h * grid_size
            )
            pygame.draw.rect(screen, (0, 0, 255), rect)
        return deposits


    def sense(self):
        # Sense trails left by other dots
        F = self.get_deposits(
            grid, 
            int(self.pos[0] + (self.sensor_distance * math.cos(self.angle)) - self.sensor_size/2),
            int(self.pos[1] + (self.sensor_distance * math.sin(self.angle)) - self.sensor_size/2),
            self.sensor_size,
            self.sensor_size
        )
        FL = self.get_deposits(
            grid, 
            int(self.pos[0] + (self.sensor_distance * math.cos(self.angle - math.radians(self.sensor_angle))) - self.sensor_size/2),
            int(self.pos[1] + (self.sensor_distance * math.sin(self.angle - math.radians(self.sensor_angle))) - self.sensor_size/2),
            self.sensor_size,
            self.sensor_size
        )
        FR = self.get_deposits(
            grid, 
            int(self.pos[0] + (self.sensor_distance * math.cos(self.angle + math.radians(self.sensor_angle))) - self.sensor_size/2),
            int(self.pos[1] + (self.sensor_distance * math.sin(self.angle + math.radians(self.sensor_angle))) - self.sensor_size/2),
            self.sensor_size,
            self.sensor_size
        )
        
        if show_dots:
            pygame.draw.circle(screen, [0, 255, 0], [self.pos[0] * grid_size, self.pos[1] * grid_size], grid_size/2)
        return F, FR, FL

    def move(self, F, FR, FL):
        if FR > FL:
            self.angle += sensitivity
        elif FL > FR:
            self.angle -= sensitivity
        else:
            if np.random.uniform() > 0.5:
                self.angle += sensitivity
            else:
                self.angle -= sensitivity


        self.pos[0] = (self.pos[0] + math.cos(self.angle)) % width
        self.pos[1] = (self.pos[1] + math.sin(self.angle)) % height

    def deposit(self):
        grid[int(self.pos[0]), int(self.pos[1])] = min(
            grid[int(self.pos[0]), int(self.pos[1])] + deposit_amount,
            max_deposit
        )

    def update(self):
        F, FL, FR = self.sense()
        self.move(F, FL, FR)
        self.deposit()
        

# Helper Functions ################################################################

def update(grid):
    # Update dots
    for dot in dots:
        dot.update()
    # Update grid
    np.maximum(np.zeros(grid.shape), grid - decay_rate, out=grid)

def draw(grid, dots):
    # max_value = np.amax(grid)
    if not show_dots:
        for i, j in np.ndindex(grid.shape):
            col = [grid[i, j] * (255 / max_deposit), 0, 0]
            rect = pygame.Rect(
                i * grid_size, j * grid_size, grid_size, grid_size
            )
            pygame.draw.rect(screen, col, rect)

            # if food[i, j] == 1:
            #     pygame.draw.rect(screen, [255, 255, 255], rect)


    # draw dots
    # for dot in dots:
    #     pygame.draw.circle(screen, [255,255,255], dot.pos, 2)

def make_dot(dots, pos, amount):
    for i in range(amount):
        angle = np.random.uniform(0, 2 * math.pi)
        # pos = [np.random.randint(0, width), np.random.randint(0, height)]
        # pos = [
        #     width/2 + math.cos(angle)*radius,
        #     height/2 + math.sin(angle)*radius
        # ]
        # angle = (angle + math.pi) % (math.pi*2)
        pos = [int(width/2), int(height/2)]
        # angle = np.random.uniform(0, 2 * math.pi)
        col = np.array([255,255,255])
        new_dot = dot(len(dots) + 1 + i, pos, angle, col)
        dots.append(new_dot)

# Start game ######################################################################

pygame.init()
screen = pygame.display.set_mode((width * grid_size, height * grid_size))
pygame.display.set_caption('slime')
clock = pygame.time.Clock()

crashed = False
time_elapsed = 0

# Main loop
while not crashed:
    screen.fill([0,0,0])

    dt = clock.tick(60) 
    time_elapsed += dt
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            # Show underlying particles / sensors
            if keys[pygame.K_q]:
                show_sensors = 1 - show_sensors
            if keys[pygame.K_w]:
                show_dots = 1 - show_dots
            # Add more dots
            if keys[pygame.K_2]:
                pos = [int(width/2), int(height/2)]
                make_dot(dots, pos, 100)
            if keys[pygame.K_1]:
                pos = [int(width/2), int(height/2)]
                make_dot(dots, pos, 1)
            # Reset
            if keys[pygame.K_r]:
                dots = []
                decay_rate = 0.18
                sensitivity = 0.19      
            # Value adjustment
            if keys[pygame.K_a]:
                decay_rate = decay_rate * 2
                print("decay_rate = ", decay_rate)
            if keys[pygame.K_z]:
                decay_rate = decay_rate / 2
                print("decay_rate = ", decay_rate)
            if keys[pygame.K_s]:
                sensitivity = sensitivity * 2
                print("sensitivity = ", sensitivity)
            if keys[pygame.K_x]:
                sensitivity = sensitivity / 2
                print("sensitivity = ", sensitivity)
    
    update(grid)
    draw(grid, dots)
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()