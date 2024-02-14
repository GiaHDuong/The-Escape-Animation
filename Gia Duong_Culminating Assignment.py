# Gia Duong - Final Assessment _ Pygame: Animation
# Input:      N/A
# Processing: N/A
# Output:     Animation
# ===== EXTRACT FOLDER AND HIGHER VOLUME FOR BEST EXPERIENCE  =====

import pygame, time, math
from pygame.locals import *

# STEP_1: SETUP ANIMATION - INTITIALIZE VARIABLES.
pygame.init()
clock = pygame.time.Clock()
flags = SCALED | RESIZABLE
surface = pygame.display.set_mode((1025, 575), flags)
pygame.display.set_caption("Boat Moving")
# FontSetting
FstSceneFont1 = pygame.font.Font("BERNHC.TTF", 82)
FstSceneFont2 = pygame.font.Font("BERNHC.TTF", 62)
Scene2Font1 = pygame.font.Font("tahomabd.TTF", 20)
#MusicSetting
Scene1Sound = "firstScene.mp3"
Scene2Sound = "Scene2.wav"
Scene3Sound = "Scene3.wav"
Scene4Sound = "Scene4ab.mp3"
Scene5Sound = "Scene5.mp3"
Scene6Sound = "Scene6.mp3"
Scene7Sound = "Scene7.mp3"
Scene8Sound = "Scene8.mp3"
# ColorSetting
black = (0, 0, 0)
teal = (15, 89, 114)
white = (255, 255, 255)
golden = (228, 155, 84)
maroon = (147, 62, 84)
blueScene1 = (176, 212, 252)
blueSea = (76, 134, 151)
blueScene2 = (190, 220, 230)
pinkScene3 = (244, 214, 190)
lightpinkS8 = (253, 231, 207)
#VariablesSetting
chgX = 350
scene = 0
FPS = 20
#ScenesImagesBG
Scene2BG = pygame.image.load("2stScene_BGBase.png")
Scene2BGOverlay = pygame.image.load("2stScene_BGOverlay.png")
Scene6Cloud = pygame.image.load("Scene6_Cloud.png")
Scene6BG2 = pygame.image.load("Scene6_BG2.png")
Scene6BottVase = pygame.image.load("Scene6_BottVase.png")
# SET UP: MOVING SPRITES
#WaterDroppingScene1
class WaterDrop(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('1stScene_P1.png'))
        self.sprites.append(pygame.image.load('1stScene_P3.png'))
        self.sprites.append(pygame.image.load('1stScene_P5.png'))
        self.sprites.append(pygame.image.load('1stScene_P7.png'))
        self.sprites.append(pygame.image.load('1stScene_P8.png'))
        self.sprites.append(pygame.image.load('1stScene_P9.png'))
        self.sprites.append(pygame.image.load('1stScene_P10.png'))
        self.sprites.append(pygame.image.load('1stScene_P11.png'))
        self.sprites.append(pygame.image.load('1stScene_P12.png'))
        self.sprites.append(pygame.image.load('1stScene_P13.png'))
        self.sprites.append(pygame.image.load('1stScene_P14.png'))
        self.sprites.append(pygame.image.load('1stScene_P15.png'))
        self.sprites.append(pygame.image.load('1stScene_P16.png'))
        self.sprites.append(pygame.image.load('1stScene_P17.png'))
        self.sprites.append(pygame.image.load('1stScene_P18.png'))
        self.sprites.append(pygame.image.load('1stScene_P19.png'))
        self.sprites.append(pygame.image.load('1stScene_P20.png'))
        self.Water_Droping = 0
        self.image = self.sprites[self.Water_Droping]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def update(self):
        if self.count == FPS//self.FPS:
            self.Water_Droping += 1
            self.Water_Droping = self.Water_Droping % len(self.sprites)  ## Limits the variable from, going out of bounds of the array
            self.count = 0
        self.count = self.count + 1
        self.image = self.sprites[self.Water_Droping]
moving_sprites = pygame.sprite.Group()
WaterDrop = WaterDrop(0,0, 15)
#StarScene2
class Star(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('2stScene_Star1.png'))
        self.sprites.append(pygame.image.load('2stScene_Star2.png'))
        self.sprites.append(pygame.image.load('2stScene_Star3.png'))
        self.sprites.append(pygame.image.load('2stScene_Star4.png'))
        self.sprites.append(pygame.image.load('2stScene_Star5.png'))
        self.sprites.append(pygame.image.load('2stScene_Star6.png'))
        self.sprites.append(pygame.image.load('2stScene_Star7.png'))
        self.sprites.append(pygame.image.load('2stScene_Star8.png'))
        self.sprites.append(pygame.image.load('2stScene_Star9.png'))
        self.sprites.append(pygame.image.load('2stScene_Star10.png'))
        self.sprites.append(pygame.image.load('2stScene_Star11.png'))
        self.sprites.append(pygame.image.load('2stScene_Star12.png'))
        self.sprites.append(pygame.image.load('2stScene_Star13.png'))
        self.sprites.append(pygame.image.load('2stScene_Star14.png'))
        self.sprites.append(pygame.image.load('2stScene_Star15.png'))
        self.sprites.append(pygame.image.load('2stScene_Star16.png'))
        self.sprites.append(pygame.image.load('2stScene_Star17.png'))
        self.sprites.append(pygame.image.load('2stScene_Star18.png'))
        self.sprites.append(pygame.image.load('2stScene_Star19.png'))
        self.sprites.append(pygame.image.load('2stScene_Star20.png'))
        self.sprites.append(pygame.image.load('2stScene_Star21.png'))
        self.sprites.append(pygame.image.load('2stScene_Star22.png'))
        self.sprites.append(pygame.image.load('2stScene_Star23.png'))
        self.sprites.append(pygame.image.load('2stScene_Star24.png'))
        self.sprites.append(pygame.image.load('2stScene_Star25.png'))
        self.Star_Moving = 0
        self.image = self.sprites[self.Star_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def update(self):
        if self.count == FPS // self.FPS:
            self.Star_Moving += 1
            self.Star_Moving = self.Star_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.Star_Moving]
Star_Moving = pygame.sprite.Group()
Star = Star(0,0, 5)
#KidLegScene2
class KidLeg(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('2stScene_Human1-9.png'))
        self.sprites.append(pygame.image.load('2stScene_Human1-9.png'))
        self.sprites.append(pygame.image.load('2stScene_Human1-9.png'))
        self.sprites.append(pygame.image.load('2stScene_Human1-9.png'))
        self.sprites.append(pygame.image.load('2stScene_Human1-9.png'))
        self.sprites.append(pygame.image.load('2stScene_Human1-9.png'))
        self.sprites.append(pygame.image.load('2stScene_Human1-9.png'))
        self.sprites.append(pygame.image.load('2stScene_Human1-9.png'))
        self.sprites.append(pygame.image.load('2stScene_Human1-9.png'))
        self.sprites.append(pygame.image.load('2stScene_Human10.png'))
        self.sprites.append(pygame.image.load('2stScene_Human11.png'))
        self.sprites.append(pygame.image.load('2stScene_Human12.png'))
        self.sprites.append(pygame.image.load('2stScene_Human13.png'))
        self.sprites.append(pygame.image.load('2stScene_Human14.png'))
        self.sprites.append(pygame.image.load('2stScene_Human15.png'))
        self.sprites.append(pygame.image.load('2stScene_Human16.png'))
        self.sprites.append(pygame.image.load('2stScene_Human17.png'))
        self.sprites.append(pygame.image.load('2stScene_Human18.png'))
        self.sprites.append(pygame.image.load('2stScene_Human19.png'))
        self.sprites.append(pygame.image.load('2stScene_Human20.png'))
        self.sprites.append(pygame.image.load('2stScene_Human21.png'))
        self.sprites.append(pygame.image.load('2stScene_Human22.png'))
        self.sprites.append(pygame.image.load('2stScene_Human23.png'))
        self.sprites.append(pygame.image.load('2stScene_Human24.png'))
        self.sprites.append(pygame.image.load('2stScene_Human25.png'))
        self.sprites.append(pygame.image.load('2stScene_Human26.png'))
        self.sprites.append(pygame.image.load('2stScene_Human27.png'))
        self.sprites.append(pygame.image.load('2stScene_Human28.png'))
        self.Kid_Moving = 0
        self.image = self.sprites[self.Kid_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def update(self):
        if self.count == FPS//self.FPS:
            self.Kid_Moving += 1
            self.Kid_Moving = self.Kid_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.Kid_Moving]
Kid_Moving = pygame.sprite.Group()
KidLeg = KidLeg(0,0, 6)
#GrabScene2
class GrabS2(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab1-21.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab22.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab23.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab24.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab25.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab26.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab27.png'))
        self.sprites.append(pygame.image.load('2stScene_Grab28.png'))
        self.Grab_MovingS2 = 0
        self.image = self.sprites[self.Grab_MovingS2]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def update(self):
        if self.count == FPS//self.FPS:
            self.Grab_MovingS2 += 1
            self.Grab_MovingS2 = self.Grab_MovingS2 % len(self.sprites)
            self.count = 0
        self.count = self.count + 1
        self.image = self.sprites[self.Grab_MovingS2]
Grab_MovingS2 = pygame.sprite.Group()
GrabS2 = GrabS2(0, 0, 6)
#CoconutScene2
class Coconut(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut1-22.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut23.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut24.png'))
        self.sprites.append(pygame.image.load('2stScene_Coconut25.png'))
        self.Coconut_Moving = 0
        self.image = self.sprites[self.Coconut_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def update(self):
        if self.count == FPS // self.FPS:
            self.Coconut_Moving += 1
            self.Coconut_Moving = self.Coconut_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.Coconut_Moving]
Coconut_Moving = pygame.sprite.Group()
Coconut = Coconut(0, 0, 6)
#GrabScene3
class GrabS3(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene3_Grab1.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab2.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab3.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab4.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab5.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab6.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab7.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab8.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab9.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab10.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab11.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab12.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab13.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab14.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab15.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab16-22.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab16-22.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab16-22.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab16-22.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab16-22.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab16-22.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab16-22.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab23.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab24.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab25.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab26.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab27-29.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab27-29.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab27-29.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab30.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab31.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab32.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab33.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab34-37.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab34-37.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab34-37.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab34-37.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab39.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab40.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab41.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab42.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab43.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab44.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab45.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab46.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab47.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab48.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab49.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab50.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab51.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab52.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab53.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab54.png'))
        self.sprites.append(pygame.image.load('Scene3_Grab55.png'))
        self.Grab_MovingS3 = 0
        self.image = self.sprites[self.Grab_MovingS3]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.Grab_MovingS3 += 1
            self.Grab_MovingS3 = self.Grab_MovingS3 % len(self.sprites)
            self.count = 0
        self.count = self.count + 1
        self.image = self.sprites[self.Grab_MovingS3]
Grab_MovingS3 = pygame.sprite.Group()
GrabS3 = GrabS3(0, 0, 6.7)
#VaseBottleScene3
class BottVaseS3(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene3_BottVase1.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase2.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase3.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase4.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase5-34.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase35.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase36.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase37.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase38.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase39.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase40.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase41.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase42.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase43.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase44.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase45.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase46.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase47.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase48.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase49.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase50.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase51.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase52.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase53.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase54.png'))
        self.sprites.append(pygame.image.load('Scene3_BottVase55.png'))
        self.BottVase_MovingS3 = 0
        self.image = self.sprites[self.BottVase_MovingS3]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def update(self):
        if self.count == FPS // self.FPS:
            self.BottVase_MovingS3 += 1
            self.BottVase_MovingS3 = self.BottVase_MovingS3 % len(self.sprites)
            self.count = 0
        self.count = self.count + 1
        self.image = self.sprites[self.BottVase_MovingS3]
BottVase_MovingS3 = pygame.sprite.Group()
BottVaseS3 = BottVaseS3(0, 0, 6.7)
#ElementS3
class ElementS3(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene3_Elements1.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements2.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements3.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements4.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.sprites.append(pygame.image.load('Scene3_Elements5-55.png'))
        self.Element_MovingS3 = 0
        self.image = self.sprites[self.Element_MovingS3]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.Element_MovingS3 += 1
            self.Element_MovingS3 = self.Element_MovingS3 % len(self.sprites)
            self.count = 0
        self.count = self.count + 1
        self.image = self.sprites[self.Element_MovingS3]
Element_MovingS3 = pygame.sprite.Group()
ElementS3 = ElementS3(0, 0, 6.7)
#BGScene4
class BackgroundS4(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene4a_BG.png'))
        self.sprites.append(pygame.image.load('Scene4a_BG.png'))
        self.sprites.append(pygame.image.load('Scene4a_BG.png'))
        self.sprites.append(pygame.image.load('Scene4a_BG.png'))
        self.sprites.append(pygame.image.load('Scene4a_BG.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG1.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG2.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG3.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG4.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BG5-16.png'))
        self.BackGroundS4_Moving = 0
        self.image = self.sprites[self.BackGroundS4_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.BackGroundS4_Moving += 1
            self.BackGroundS4_Moving = self.BackGroundS4_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.BackGroundS4_Moving]
BackGroundS4_Moving = pygame.sprite.Group()
BackgroundS4 = BackgroundS4(0, 0, 4.5)
#ElementScene4
class ElementS4(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene4a_Element.png'))
        self.sprites.append(pygame.image.load('Scene4a_Element.png'))
        self.sprites.append(pygame.image.load('Scene4a_Element.png'))
        self.sprites.append(pygame.image.load('Scene4a_Element.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element1.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element2.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element3.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element4.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_Element5-16.png'))
        self.ElementS4_Moving = 0
        self.image = self.sprites[self.ElementS4_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.ElementS4_Moving += 1
            self.ElementS4_Moving = self.ElementS4_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.ElementS4_Moving]
ElementS4_Moving = pygame.sprite.Group()
ElementS4 = ElementS4(0, 0, 4)
#BottleVaseS4
class BottVaseS4(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene4a_BottVase.png'))
        self.sprites.append(pygame.image.load('Scene4a_BottVase.png'))
        self.sprites.append(pygame.image.load('Scene4a_BottVase.png'))
        self.sprites.append(pygame.image.load('Scene4a_BottVase.png'))
        self.sprites.append(pygame.image.load('Scene4a_BottVase.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase1.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase2.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase3.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase4.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase5-16.png'))
        self.sprites.append(pygame.image.load('Scene4b_BottVase5-16.png'))
        self.BottVaseS4_Moving = 0
        self.image = self.sprites[self.BottVaseS4_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.BottVaseS4_Moving += 1
            self.BottVaseS4_Moving = self.BottVaseS4_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.BottVaseS4_Moving]
BottVaseS4_Moving = pygame.sprite.Group()
BottVaseS4 = BottVaseS4(0, 0, 4)
#KidScene4
class KidS4(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene4a_Kid1.png'))
        self.sprites.append(pygame.image.load('Scene4a_Kid2.png'))
        self.sprites.append(pygame.image.load('Scene4a_Kid3.png'))
        self.sprites.append(pygame.image.load('Scene4a_Kid4.png'))
        self.sprites.append(pygame.image.load('Scene4a_Kid5.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid1.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid2.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid3.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid4.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid5.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid6.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid7.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid8.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid9.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid10.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid11.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid12.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid13.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid14.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid15.png'))
        self.sprites.append(pygame.image.load('Scene4b_Kid16.png'))
        self.KidS4_Moving = 0
        self.image = self.sprites[self.KidS4_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.KidS4_Moving += 1
            self.KidS4_Moving = self.KidS4_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.KidS4_Moving]
KidS4_Moving = pygame.sprite.Group()
KidS4 = KidS4(0, 0, 4)
#BackGroundScene5
class BGS5(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene5_BG1.png'))
        self.sprites.append(pygame.image.load('Scene5_BG2.png'))
        self.sprites.append(pygame.image.load('Scene5_BG3.png'))
        self.sprites.append(pygame.image.load('Scene5_BG4.png'))
        self.sprites.append(pygame.image.load('Scene5_BG5.png'))
        self.sprites.append(pygame.image.load('Scene5_BG6.png'))
        self.sprites.append(pygame.image.load('Scene5_BG7.png'))
        self.sprites.append(pygame.image.load('Scene5_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene5_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene5_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene5_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene5_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene5_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene5_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene5_BG8-15.png'))
        self.BGS5_Moving = 0
        self.image = self.sprites[self.BGS5_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.BGS5_Moving += 1
            self.BGS5_Moving = self.BGS5_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.BGS5_Moving]
BGS5_Moving = pygame.sprite.Group()
BGS5 = BGS5(0, 0, 5.5)
#GrabScene5
class GrabS5(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene5_Grab1.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab2.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab3.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab4.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab5.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab6.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab7.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab8.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab9.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab10.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab11.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab12.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab13.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab14.png'))
        self.sprites.append(pygame.image.load('Scene5_Grab15.png'))
        self.GrabS5_Moving = 0
        self.image = self.sprites[self.GrabS5_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.GrabS5_Moving += 1
            self.GrabS5_Moving = self.GrabS5_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.GrabS5_Moving]
GrabS5_Moving = pygame.sprite.Group()
GrabS5 = GrabS5(0, 0, 5.5)
#DoorScene6
class DoorS6(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene6_Door1-2.png'))
        self.sprites.append(pygame.image.load('Scene6_Door1-2.png'))
        self.sprites.append(pygame.image.load('Scene6_Door3.png'))
        self.sprites.append(pygame.image.load('Scene6_Door4-15.png'))
        self.sprites.append(pygame.image.load('Scene6_Door4-15.png'))
        self.sprites.append(pygame.image.load('Scene6_Door4-15.png'))
        self.sprites.append(pygame.image.load('Scene6_Door4-15.png'))
        self.sprites.append(pygame.image.load('Scene6_Door4-15.png'))
        self.sprites.append(pygame.image.load('Scene6_Door4-15.png'))
        self.sprites.append(pygame.image.load('Scene6_Door4-15.png'))
        self.sprites.append(pygame.image.load('Scene6_Door4-15.png'))
        self.sprites.append(pygame.image.load('Scene6_Door4-15.png'))
        self.sprites.append(pygame.image.load('Scene6_Door4-15.png'))
        self.sprites.append(pygame.image.load('Scene6_Door4-15.png'))
        self.sprites.append(pygame.image.load('Scene6_Door4-15.png'))
        self.sprites.append(pygame.image.load('Scene6_Door16.png'))
        self.sprites.append(pygame.image.load('Scene6_Door17.png'))
        self.sprites.append(pygame.image.load('Scene6_Door18.png'))
        self.sprites.append(pygame.image.load('Scene6_Door19-23.png'))
        self.sprites.append(pygame.image.load('Scene6_Door19-23.png'))
        self.sprites.append(pygame.image.load('Scene6_Door19-23.png'))
        self.sprites.append(pygame.image.load('Scene6_Door19-23.png'))
        self.sprites.append(pygame.image.load('Scene6_Door19-23.png'))
        self.DoorS6_Moving = 0
        self.image = self.sprites[self.DoorS6_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.DoorS6_Moving += 1
            self.DoorS6_Moving = self.DoorS6_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.DoorS6_Moving]
DoorS6_Moving = pygame.sprite.Group()
DoorS6 = DoorS6(0, 0, 5)
#KidScene6
class KidS6(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene6_Kid1.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid2.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid3.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid4.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid5.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid6.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid7.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid8.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid9.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid10.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid11.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid12.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid13.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid14.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid15.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid16.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid17.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid18.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid19.png'))
        self.sprites.append(pygame.image.load('Scene6_Kid20.png'))
        self.sprites.append(pygame.image.load('2stScene_Human1-9.png'))
        self.sprites.append(pygame.image.load('2stScene_Human1-9.png'))
        self.sprites.append(pygame.image.load('2stScene_Human1-9.png'))
        self.KidS6_Moving = 0
        self.image = self.sprites[self.KidS6_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.KidS6_Moving += 1
            self.KidS6_Moving = self.KidS6_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.KidS6_Moving]
KidS6_Moving = pygame.sprite.Group()
KidS6 = KidS6(0, 0, 5)
#BackGroundScene7
class BGS7(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene7_BG1-5.png'))
        self.sprites.append(pygame.image.load('Scene7_BG1-5.png'))
        self.sprites.append(pygame.image.load('Scene7_BG1-5.png'))
        self.sprites.append(pygame.image.load('Scene7_BG1-5.png'))
        self.sprites.append(pygame.image.load('Scene7_BG1-5.png'))
        self.sprites.append(pygame.image.load('Scene7_BG6.png'))
        self.sprites.append(pygame.image.load('Scene7_BG7.png'))
        self.sprites.append(pygame.image.load('Scene7_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene7_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene7_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene7_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene7_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene7_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene7_BG8-15.png'))
        self.sprites.append(pygame.image.load('Scene7_BG8-15.png'))
        self.BGS7_Moving = 0
        self.image = self.sprites[self.BGS7_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.BGS7_Moving += 1
            self.BGS7_Moving = self.BGS7_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.BGS7_Moving]
BGS7_Moving = pygame.sprite.Group()
BGS7 = BGS7(0, 0, 5)
#GrabScene7
class GrabS7(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene7_Grab1.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab2.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab3.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab4.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab5.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab6.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab7.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab8.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab9.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab10.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab11.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab12.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab13.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab14.png'))
        self.sprites.append(pygame.image.load('Scene7_Grab15.png'))
        self.GrabS7_Moving = 0
        self.image = self.sprites[self.GrabS7_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.GrabS7_Moving += 1
            self.GrabS7_Moving = self.GrabS7_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.GrabS7_Moving]
GrabS7_Moving = pygame.sprite.Group()
GrabS7 = GrabS7(0, 0, 5)
#GrabS8
class GrabS8(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene8_Grab1.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab2.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab3.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab4.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab5.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab6.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab7.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab8.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab9.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab10.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab11.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab12.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab13.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab14.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab15.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab16.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab17.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab18.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab19.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab20.png'))
        self.sprites.append(pygame.image.load('Scene8_Grab21.png'))
        self.GrabS8_Moving = 0
        self.image = self.sprites[self.GrabS8_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.GrabS8_Moving += 1
            self.GrabS8_Moving = self.GrabS8_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.GrabS8_Moving]
GrabS8_Moving = pygame.sprite.Group()
GrabS8 = GrabS8(0, 0, 5)
#BackGroundScene8
class BGS8(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('Scene8_BG1-2.png'))
        self.sprites.append(pygame.image.load('Scene8_BG1-2.png'))
        self.sprites.append(pygame.image.load('Scene8_BG3.png'))
        self.sprites.append(pygame.image.load('Scene8_BG4.png'))
        self.sprites.append(pygame.image.load('Scene8_BG5.png'))
        self.sprites.append(pygame.image.load('Scene8_BG6.png'))
        self.sprites.append(pygame.image.load('Scene8_BG7.png'))
        self.sprites.append(pygame.image.load('Scene8_BG8.png'))
        self.sprites.append(pygame.image.load('Scene8_BG9.png'))
        self.sprites.append(pygame.image.load('Scene8_BG10.png'))
        self.sprites.append(pygame.image.load('Scene8_BG11.png'))
        self.sprites.append(pygame.image.load('Scene8_BG12.png'))
        self.sprites.append(pygame.image.load('Scene8_BG13.png'))
        self.sprites.append(pygame.image.load('Scene8_BG14.png'))
        self.sprites.append(pygame.image.load('Scene8_BG15.png'))
        self.sprites.append(pygame.image.load('Scene8_BG16-21.png'))
        self.sprites.append(pygame.image.load('Scene8_BG16-21.png'))
        self.sprites.append(pygame.image.load('Scene8_BG16-21.png'))
        self.sprites.append(pygame.image.load('Scene8_BG16-21.png'))
        self.sprites.append(pygame.image.load('Scene8_BG16-21.png'))
        self.sprites.append(pygame.image.load('Scene8_BG16-21.png'))
        self.BGS8_Moving = 0
        self.image = self.sprites[self.BGS8_Moving]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.BGS8_Moving += 1
            self.BGS8_Moving = self.BGS8_Moving % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.BGS8_Moving]
BGS8_Moving = pygame.sprite.Group()
BGS8 = BGS8(0, 0, 5)
#TheEndScene
class TheEndScene(pygame.sprite.Sprite):
    global FPS
    def __init__(self, pos_x, pos_y, cFPS):
        self.FPS = cFPS;
        self.count = 0;
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.sprites.append(pygame.image.load('TheEndScene.png'))
        self.EndScene = 0
        self.image = self.sprites[self.EndScene]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.count == FPS // self.FPS:
            self.EndScene += 1
            self.EndScene = self.EndScene % len(self.sprites)
            self.count = 0
        self.count += 1
        self.image = self.sprites[self.EndScene]
EndScene = pygame.sprite.Group()
TheEndScene = TheEndScene(0, 0, 1)

# STEP_2: SETUP GAME LOOP AND POOL FOR EVENTS.
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
        break
    if scene == 0:
        pygame.mixer.music.load(Scene1Sound)
        pygame.mixer.music.play(0)
        scene = 1
    if chgX > 10:
        chgX = chgX - 4
    elif chgX == 10:
        moving_sprites.add(WaterDrop)
        if WaterDrop.Water_Droping <= 16:
            moving_sprites.update()
    if WaterDrop.Water_Droping == 16:
        scene = 2
    if scene == 2:
        Star_Moving.add(Star)
        Kid_Moving.add(KidLeg)
        Grab_MovingS2.add(GrabS2)
        Coconut_Moving.add(Coconut)
        if Star.Star_Moving == 1 :
            pygame.mixer.music.load(Scene2Sound)
            pygame.mixer.music.play(0)
        if Star.Star_Moving <= 23:
            Star_Moving.update()
        if KidLeg.Kid_Moving <= 26:
            Kid_Moving.update()
        if GrabS2.Grab_MovingS2 <= 26:
            Grab_MovingS2.update()
        if Coconut.Coconut_Moving <= 23:
            Coconut_Moving.update()
    if KidLeg.Kid_Moving == 27:
        scene = 3
    if scene == 3:
        Grab_MovingS3.add(GrabS3)
        BottVase_MovingS3.add(BottVaseS3)
        Element_MovingS3.add(ElementS3)
        if GrabS3.Grab_MovingS3 == 0:
            pygame.mixer.music.load(Scene3Sound)
            pygame.mixer.music.play(0)
        #if GrabS3.Grab_MovingS3 == 13:
            #Scene2Text1 = Scene2Dont1.render("Oh No", 1, white)
        if GrabS3.Grab_MovingS3 <= 52:
            Grab_MovingS3.update()
        if BottVaseS3.BottVase_MovingS3 <= 52:
            BottVase_MovingS3.update()
        if ElementS3.Element_MovingS3 <= 52:
            Element_MovingS3.update()
    if GrabS3.Grab_MovingS3 == 53:
        scene = 4
    if scene == 4:
        BackGroundS4_Moving.add(BackgroundS4)
        ElementS4_Moving.add(ElementS4)
        BottVaseS4_Moving.add(BottVaseS4)
        KidS4_Moving.add(KidS4)
        if BackgroundS4.BackGroundS4_Moving == 1:
            pygame.mixer.music.load(Scene4Sound)
            pygame.mixer.music.play(0)
        if BackgroundS4.BackGroundS4_Moving <= 19:
            BackGroundS4_Moving.update()
        if ElementS4.ElementS4_Moving <= 19:
            ElementS4_Moving.update()
        if BottVaseS4.BottVaseS4_Moving <= 19:
            BottVaseS4_Moving.update()
        if KidS4.KidS4_Moving <= 19:
            KidS4_Moving.update()
    if BackgroundS4.BackGroundS4_Moving == 20:
        scene = 5
    if scene == 5:
        BGS5_Moving.add(BGS5)
        GrabS5_Moving.add(GrabS5)
        if BGS5.BGS5_Moving == 1:
            pygame.mixer.music.load(Scene5Sound)
            pygame.mixer.music.play(0)
        if BGS5.BGS5_Moving <= 13:
            BGS5_Moving.update()
        if GrabS5.GrabS5_Moving <= 13:
            GrabS5_Moving.update()
    if BGS5.BGS5_Moving == 14:
        scene = 6
    if scene == 6:
        DoorS6_Moving.add(DoorS6)
        KidS6_Moving.add(KidS6)
        if DoorS6.DoorS6_Moving == 1:
            pygame.mixer.music.load(Scene6Sound)
            pygame.mixer.music.play(0)
        if DoorS6.DoorS6_Moving <= 21:
            DoorS6_Moving.update()
        if KidS6.KidS6_Moving <= 21:
            KidS6_Moving.update()
    if DoorS6.DoorS6_Moving == 22:
        scene = 7
    if scene == 7:
        BGS7_Moving.add(BGS7)
        GrabS7_Moving.add(GrabS7)
        if BGS7.BGS7_Moving == 1:
            pygame.mixer.music.load(Scene7Sound)
            pygame.mixer.music.play(0)
        if BGS7.BGS7_Moving <= 13:
            BGS7_Moving.update()
        if GrabS7.GrabS7_Moving <= 13:
            GrabS7_Moving.update()
    if BGS7.BGS7_Moving == 14:
        scene = 8
    if scene == 8:
        GrabS8_Moving.add(GrabS8)
        BGS8_Moving.add(BGS8)
        if GrabS8.GrabS8_Moving == 1:
            pygame.mixer.music.load(Scene8Sound)
            pygame.mixer.music.play(0)
        if GrabS8.GrabS8_Moving <= 19:
            GrabS8_Moving.update()
        if BGS8.BGS8_Moving <= 19:
            BGS8_Moving.update()
    if GrabS8.GrabS8_Moving == 20:
        scene = 9
    if scene == 9:
        EndScene.add(TheEndScene)
        if TheEndScene.EndScene <= 15:
            EndScene.update()

# STEP_3: UPDATE GAME AND OBJECTS
    if scene == 1:
        BGColor = blueScene1
        sea = (0, 419, 1025, 575)
        # BoatDrawing
        boatBody = ((chgX + 637.5, 381.25), (chgX + 637.5, 396.875), (chgX + 662.5, 421.875), (chgX + 875, 421.875),
                    (chgX + 881.25, 396.875), (chgX + 881.25, 381.25),
                    (chgX + 828.125, 381.25), (chgX + 821.875, 390.625), (chgX + 712.5, 390.625),
                    (chgX + 706.25, 381.25), (chgX + 637.5, 381.25))
        boatLine1 = ((chgX + 637.5, 381.25), (chgX + 637.5, 396.875), (chgX + 881.25, 396.875), (chgX + 881.25, 381.25),
                     (chgX + 828.125, 381.25), (chgX + 821.875, 390.625),
                     (chgX + 712.5, 390.625), (chgX + 706.25, 381.25), (chgX + 637.5, 381.25))
        boatLine2 = ((chgX + 641, 400), (chgX + 650, 408), (chgX + 879.25, 408), (chgX + 881, 400))
        boatTop = ((chgX + 831.25, 340.625), (chgX + 843.75, 356.25), (chgX + 843.75, 385), (chgX + 875, 385),
                   (chgX + 875, 356.25), (chgX + 887.5, 340.625))
        shipment1a = (chgX + 718.75, 325, 28.125, 21.875)
        shipment1b = (chgX + 746.875, 325, 28.125, 21.875)
        shipment2a = (chgX + 690.625, 346.875, 29, 21.875)
        shipment2b = (chgX + 718.75, 346.875, 28.125, 21.875)
        shipment2c = (chgX + 746.875, 346.875, 28.125, 21.875)
        shipment2d = (chgX + 774.75, 346.875, 28.125, 21.875)
        shipment3a = (chgX + 662.5, 367.95, 28.125, 23.875)
        shipment3b = (chgX + 690.625, 367.95, 29, 23.875)
        shipment3c = (chgX + 718.75, 367.95, 28.125, 23.875)
        shipment3d = (chgX + 746.875, 367.95, 28.125, 23.875)
        shipment3e = (chgX + 774.75, 367.95, 28.125, 23.875)
        shipment3f = (chgX + 802.75, 367.95, 28.125, 23.875)
        # FontDrawing
        Scene1Word1 = FstSceneFont1.render("THE ESCAPING", 1, white)
        Scene1Word2 = FstSceneFont2.render("@GiaD", 1, white)
    elif scene == 2:
        BGColor = blueScene2
        Scene2Text1 = Scene2Font1.render("What a nice vacation!... But, Huh?", 1, black)
    elif scene == 3:
        BGColor = pinkScene3
        Scene3Text1 = Scene2Font1.render("Where am I? I don't wanna be here!", 1, black)
    elif scene == 4:
        BGColor == pinkScene3
        Scene4Text1 = Scene2Font1.render("Hehe. You're dead with me, Grab.", 1, white)
    elif scene == 5:
        BGColor = pinkScene3
        Scene5Text1 = Scene2Font1.render("Hic... That kid is so scared.", 1, black)
    elif scene == 6:
        BGColor = blueScene1
        Scene6Text1 = Scene2Font1.render("Oh, someone outside?", 1, white)
    elif scene == 7:
        BGColor = pinkScene3
        Scene7Text1 = Scene2Font1.render("He's gone, now is my chance!", 1, black)
    elif scene == 8:
        BGColor = lightpinkS8
        Scene8Text1 = Scene2Font1.render("Let's Escaping!", 1, black)
    elif scene == 9:
        BGColor = pinkScene3

# STEP_4: DRAW ON EACH SURFACE
    if scene == 1:
        surface.fill(BGColor)
        pygame.draw.rect(surface, blueSea, sea, 0)
        #pygame.draw.line(surface, black, (650, 325), (650, 350), 4)  # Black Line where boat suppose to stop
        pygame.draw.line(surface, white, (chgX + 850, 325), (chgX + 850, 350), 4)
        pygame.draw.line(surface, white, (chgX + 862.5, 312.5), (chgX + 862.5, 350), 4)
        pygame.draw.line(surface, white, (chgX + 643.75, 343.75), (chgX + 643.75, 381.25), 4)
        pygame.draw.line(surface, white, (chgX + 652.75, 373.75), (chgX + 652.75, 381.25), 4)
        pygame.draw.rect(surface, golden, shipment1a, 0)
        pygame.draw.rect(surface, maroon, shipment1b, 0)
        pygame.draw.rect(surface, golden, shipment2a, 0)
        pygame.draw.rect(surface, maroon, shipment2b, 0)
        pygame.draw.rect(surface, black, shipment2c, 0)
        pygame.draw.rect(surface, black, shipment2d, 0)
        pygame.draw.rect(surface, maroon, shipment3a, 0)
        pygame.draw.rect(surface, black, shipment3b, 0)
        pygame.draw.rect(surface, golden, shipment3c, 0)
        pygame.draw.rect(surface, maroon, shipment3d, 0)
        pygame.draw.rect(surface, golden, shipment3e, 0)
        pygame.draw.rect(surface, maroon, shipment3f, 0)
        pygame.draw.polygon(surface, black, boatBody, 0)
        pygame.draw.polygon(surface, white, boatTop, 0)
        pygame.draw.polygon(surface, teal, boatLine1, 0)
        pygame.draw.polygon(surface, teal, boatLine2, 0)
        pygame.draw.line(surface, blueScene1, (chgX + 840.625, 346.875), (chgX + 878.125, 346.875), 3)
        pygame.draw.line(surface, blueScene1, (chgX + 846.875, 376.5), (chgX + 871.875, 376.5), 3)
        # FontDisplay
        surface.blit(Scene1Word1, ([190, 137.5]))
        surface.blit(Scene1Word2, ([310, 230.5]))
    elif scene == 2:
        surface.fill(BGColor)
        surface.blit(Scene2BG, (0,0))
    elif scene == 3:
        surface.fill(BGColor)
    elif scene == 4:
        surface.fill(BGColor)
    elif scene == 5:
        surface.fill(BGColor)
    elif scene == 6:
        surface.fill(BGColor)
    elif scene == 7:
        surface.fill(BGColor)
    elif scene == 8:
        surface.fill(BGColor)
    else:
        if scene == 9:
            scene = 0
            #print(3)
            chgX = 350
            WaterDrop.Water_Droping = 0
            Star.Star_Moving = 0
            KidLeg.Kid_Moving = 0
            GrabS2.Grab_MovingS2 = 0
            Coconut.Coconut_Moving = 0
            GrabS3.Grab_MovingS3 = 0
            BottVaseS3.BottVase_MovingS3 = 0
            ElementS3.Element_MovingS3 = 0
            BackgroundS4.BackGroundS4_Moving = 0
            ElementS4.ElementS4_Moving = 0
            BottVaseS4.BottVaseS4_Moving = 0
            KidS4.KidS4_Moving = 0
            BGS5.BGS5_Moving = 0
            GrabS5.GrabS5_Moving = 0
            DoorS6.DoorS6_Moving = 0
            KidS6.KidS6_Moving = 0
            BGS7.BGS7_Moving = 0
            GrabS7.GrabS7_Moving = 0
            GrabS8.GrabS8_Moving = 0
            BGS8.BGS8_Moving = 0
            TheEndScene.EndScene = 0

# STEP5: SHOW/ DISPLAY SURFACE
# Step 5:  Show/display surface
    if scene == 1:
        moving_sprites.draw(surface)
    if scene == 2:
        Kid_Moving.draw(surface)
        surface.blit(Scene2BGOverlay, (0, 0))
        Grab_MovingS2.draw(surface)
        Star_Moving.draw(surface)
        Coconut_Moving.draw(surface)
        surface.blit(Scene2Text1, ([370, 530]))
    if scene == 3:
        Grab_MovingS3.draw(surface)
        BottVase_MovingS3.draw(surface)
        Element_MovingS3.draw(surface)
        surface.blit(Scene3Text1, ([320, 540]))
    if scene == 4:
        BackGroundS4_Moving.draw(surface)
        KidS4_Moving.draw(surface)
        ElementS4_Moving.draw(surface)
        BottVaseS4_Moving.draw(surface)
        surface.blit(Scene4Text1, ([350, 540]))
    if scene == 5:
        BGS5_Moving.draw(surface)
        GrabS5_Moving.draw(surface)
        surface.blit(Scene5Text1, ([420, 520]))
    if scene == 6:
        surface.blit(Scene6Cloud, (0, 0))
        DoorS6_Moving.draw(surface)
        KidS6_Moving.draw(surface)
        surface.blit(Scene6BG2, (0, 0))
        surface.blit(Scene6BottVase, (0, 0))
        surface.blit(Scene6Text1, ([400, 500]))
    if scene == 7:
        BGS7_Moving.draw(surface)
        GrabS7_Moving.draw(surface)
        surface.blit(Scene7Text1, ([370, 530]))
    if scene == 8:
        BGS8_Moving.draw(surface)
        GrabS8_Moving.draw(surface)
        surface.blit(Scene8Text1, ([450, 520]))
    if scene == 9:
        surface.fill(BGColor)
        EndScene.draw(surface)
    pygame.display.flip()
    clock.tick(FPS)
pygame.display.quit()
quit()
