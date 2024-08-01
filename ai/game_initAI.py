import pygame
import random
pygame.init()



class Game:
    def __init__(self, difficulty, genomes, config, neat):
        self.nets = []
        self.birds = []
        self.ge = []
        
        
        self.scale = 124
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

        for _, g in genomes:
            net = neat.nn.FeedForwardNetwork.create(g, config)
            self.nets.append(net)
            self.birds.append(Bird(self.screen, self.scale))
            g.fitness = 0
            self.ge.append(g)
        #Bird(self.screen, self.scale)


        self.framerate = 180
        self.running = True
        
        difficulty_settings = {
            "easy": {
                "pipes": {
                    "distance_center": 220,
                    "variation": 20,
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
        self.pipe_timer = 0
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
        for x, b in enumerate(self.birds):
            bc = [b.position.x, b.position.y]
            p = self.pipes[0]
            bounding_box = pygame.Rect(b.position.x - b.radius, b.position.y - b.radius, 2 * b.radius, 2 * b.radius)
            if bc[1] - b.radius < 0 or bc[1] + b.radius > self.dimensions["y"]:
                self.ge[x].fitness -= 1
                self.birds.pop(x)
                self.nets.pop(x)
                self.ge.pop(x)
            if bounding_box.colliderect(p.rectangles[0]):
                pcl = [p.rectangles[0].x, p.rectangles[0].y]
                pcr = [p.rectangles[0].x + p.width, p.rectangles[0].y]
                if (bc[0] - pcl[0]) ** 2 + (bc[1] - pcl[1]) ** 2 < b.radius ** 2 or (bc[0] - pcr[0]) ** 2 + (bc[1] - pcr[1]) ** 2 < b.radius ** 2 or (bc[0] + b.radius > pcl[0] and bc[1] > pcl[1]) or (bc[1] + b.radius > pcl[1] and bc[0] > pcl[0] and bc[0] < pcr[1]):
                    self.ge[x].fitness -= 1
                    self.birds.pop(x)
                    self.nets.pop(x)
                    self.ge.pop(x)
                else:
                    self.ge[x].fitness += 5
            elif bounding_box.colliderect(p.rectangles[1]):
                pcl = [p.rectangles[1].x, p.height]
                pcr = [p.rectangles[1].x + p.width, p.height]
                if (bc[0] - pcl[0]) ** 2 + (bc[1] - pcl[1]) ** 2 < b.radius ** 2 or (bc[0] - pcr[0]) ** 2 + (bc[1] - pcr[1]) ** 2 < b.radius ** 2 or (bc[0] + b.radius > pcl[0] and bc[1] < pcl[1]) or (bc[1] - b.radius < pcl[1] and bc[0] > pcl[0] and bc[0] < pcr[1]):
                    self.pipes.pop(0)                
                    self.ge[x].fitness -= 1
                    self.birds.pop(x)
                    self.nets.pop(x)
                    self.ge.pop(x)
            else:
                if b.position.x > p.rectangles[0].x and p.scored == False:
                    self.score += 1
                    self.ge[x].fitness += 5
                    p.scored = True
                    return "SCORE"
                

    def play_step(self, action):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
        keys = pygame.key.get_pressed()

        self.screen.fill("white")
        self.manage_pipes(self.screen)
        for x, b in enumerate(self.birds):
            b.update(self.dt)
            b.draw(self.screen)
            self.ge[x].fitness += .016

            output = self.nets[x].activate((b.position.y, abs(b.position.y - self.pipes[0].rectangles[0].y), abs(b.position.y - self.pipes[0].rectangles[1] - self.pipes[0].height)))
            if output[0] > 0.5:
                b.jump()

        collided = self.check_collision()

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