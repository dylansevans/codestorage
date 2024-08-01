import pygame
import random
import functools
pygame.init()



class Game:
    def __init__(self, difficulty):
        self.framerate = 180
        self.running = True
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        difficulty_settings = {
            "easy": {
                "pipes": {
                    "distance_center": 200,
                    "variation": 30,
                    "speed": 4,
                    "pipe-delay": 2,
                }
            }
        }
        self.dt = 0
        self.score = 0
        self.dimensions = {
            "x": self.screen.get_width(),
            "y": self.screen.get_height(),
        }
        self.settings = difficulty_settings[difficulty]
        self.scale = 124
        self.pipe_timer = 0
        self.bird = Bird(self.screen, self.scale)
        self.difficulty = difficulty
        self.pipes = [Pipe(self.dimensions, self.scale, self.settings["pipes"])]

    def manage_pipes(self, screen):
        for i in self.pipes:
            if i.move(self.dt) < 0:
                self.pipes.pop(0)
            else:
                i.draw(screen)
        
        if self.pipe_timer >= self.settings["pipes"]["pipe-delay"]:
            self.pipes.append(Pipe(self.dimensions, self.scale, self.settings["pipes"])) 
            self.pipe_timer = 0       

        self.pipe_timer += self.dt

    def check_collision(self):
        b = self.bird
        bc = [b.position.x, b.position.y]
        p = self.pipes[0]
        bounding_box = pygame.Rect(b.position.x - b.radius, b.position.y - b.radius, 2 * b.radius, 2 * b.radius)
        if bc[1] - b.radius < 0 or bc[1] + b.radius > self.dimensions["y"]:
            return True
        if bounding_box.colliderect(p.rectangles[0]):
            pcl = [p.rectangles[0].x, p.rectangles[0].y]
            pcr = [p.rectangles[0].x + p.width, p.rectangles[0].y]
            if (bc[0] - pcl[0]) ** 2 + (bc[1] - pcl[1]) ** 2 < b.radius ** 2 or (bc[0] - pcr[0]) ** 2 + (bc[1] - pcr[1]) ** 2 < b.radius ** 2 or (bc[0] + b.radius > pcl[0] and bc[1] > pcl[1]) or (bc[1] + b.radius > pcl[1] and bc[0] > pcl[0] and bc[0] < pcr[1]):
                self.pipes.pop(0)
                return True
            else:
                return False
        elif bounding_box.colliderect(p.rectangles[1]):
            pcl = [p.rectangles[1].x, p.height]
            pcr = [p.rectangles[1].x + p.width, p.height]
            if (bc[0] - pcl[0]) ** 2 + (bc[1] - pcl[1]) ** 2 < b.radius ** 2 or (bc[0] - pcr[0]) ** 2 + (bc[1] - pcr[1]) ** 2 < b.radius ** 2 or (bc[0] + b.radius > pcl[0] and bc[1] < pcl[1]) or (bc[1] - b.radius < pcl[1] and bc[0] > pcl[0] and bc[0] < pcr[1]):
                self.pipes.pop(0)                
                return True
            else:
                return False
        else:
            if b.position.x > p.rectangles[0].x and p.scored == False:
                self.score += 1
                p.scored = True
            return False

    def play_step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.bird.jump()
        self.screen.fill("white")
        self.manage_pipes(self.screen)

        self.bird.update(self.dt)
        self.bird.draw(self.screen)
        
        pygame.display.update()

        self.dt = self.clock.tick(self.framerate) / 1000



class Bird:
    def __init__(self, screen, scale):
        self.scale = scale
        self.jump_strength = -4 #negative because more negative is more up
        self.position = pygame.Vector2(screen.get_width() / 6, screen.get_height() / 2)
        self.velocity = pygame.Vector2(0, 0)
        self.gravity = pygame.Vector2(0, 9.8)
        self.radius = 20

    def update(self, dt):
        self.velocity += self.gravity * dt * self.scale
        self.position += self.velocity * dt

    def jump(self):
        self.velocity = pygame.Vector2(0, self.jump_strength  * self.scale)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)



class Pipe:
    def __init__(self, dimensions:list, scale:float, settings:object):
        self.speed = dimensions["x"] / 3
        self.width = 40
        self.scale = scale
        self.distance = settings["distance_center"] + (random.random() - .5) * settings["variation"]
        self.height = random.uniform(10, dimensions["y"] - 10 - self.distance)
        self.rectangles = [
            pygame.Rect(dimensions["x"], self.height + self.distance, self.width, dimensions["y"] - self.distance - self.height),
            pygame.Rect(dimensions["x"], 0, self.width, self.height),
        ]
        self.scored = False

    def move(self, dt):
        self.rectangles[0].move_ip(-1 * self.speed * dt, 0)
        self.rectangles[1].move_ip(-1 * self.speed * dt, 0)
        return self.rectangles[0].x + self.width

    def draw(self, screen):
        pygame.draw.rect(screen, "green", self.rectangles[0])
        pygame.draw.rect(screen, "green", self.rectangles[1])