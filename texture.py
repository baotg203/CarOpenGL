import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


#creating a list of texture names that will be used to identify each texture.
texture_names = [i for i in range(0, 20)]

# assigning a unique integer identifier to each texture using global constants, which makes it easier to refer to textures throughout the code.
STAR = 0
CAR = 1
HEALTH = 2
EXIT_RED = 3
EXIT_YELLOW = 4
START_RED = 5
START_YELLOW = 6
START_SCREEN = 7
BACK_YELLOW = 8
BACK_RED = 9
BOMB = 10
PLAY_AGAIN = 11
TRY_AGAIN_YEL = 12
TRY_AGAIN_RED = 13
EXIT2_YEL = 14
EXIT2_RED = 15
FINISH_LINE = 16
YOU_WIN = 17
HOME_YEL = 18
HOME_RED = 19


def load_texture():
    """
    enables 2D texture mapping for OpenGL, loads all the texture images and stores them as a list of texture binary data.
    It then generates a unique texture name for each image and sets up the texture parameters for each texture using the setup_texture() function.
    """
    glEnable(GL_TEXTURE_2D)

    images = []

    # Load images from files
    images.append(pygame.image.load("Texture/star.png"))
    images.append(pygame.image.load("Texture/car.png"))
    images.append(pygame.image.load("Texture/health.png"))
    images.append(pygame.image.load("Texture/exit_red.png"))
    images.append(pygame.image.load("Texture/exit_yellow.png"))
    images.append(pygame.image.load("Texture/start_red.png"))
    images.append(pygame.image.load("Texture/start_yellow.png"))
    images.append(pygame.image.load("Texture/start_screen.png"))
    images.append(pygame.image.load("Texture/back_yellow.png"))
    images.append(pygame.image.load("Texture/back_red.png"))
    images.append(pygame.image.load("Texture/bomb.png"))
    images.append(pygame.image.load("Texture/game_over.png"))
    images.append(pygame.image.load("Texture/try_again_yellow.png"))
    images.append(pygame.image.load("Texture/try_again_red.png"))
    images.append(pygame.image.load("Texture/exit2_yellow.png"))
    images.append(pygame.image.load("Texture/exit2_red.png"))
    images.append(pygame.image.load("Texture/finish_line.jpg"))
    images.append(pygame.image.load("Texture/you_win.png"))
    images.append(pygame.image.load("Texture/Home_yel.png"))
    images.append(pygame.image.load("Texture/Home_red.png"))

    # Convert the images to raw binary image data
    textures = [pygame.image.tostring(img,"RGBA", 1) for img in images]

    # Generate texture IDs
    glGenTextures(len(images), texture_names)

    # Bind each texture and set texture parameters
    for i in range(len(images)):
        setup_texture(textures[i],
                      texture_names[i],
                      images[i].get_width(),
                      images[i].get_height())


def setup_texture(binary_img, texture_iden, width, height):
    """
    binds the texture to the texture identifier, sets texture parameters, and then loads the texture binary data.
    """
    glBindTexture(GL_TEXTURE_2D, texture_iden)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width,
                 height, 0, GL_RGBA, GL_UNSIGNED_BYTE, binary_img)
        