import time

import pygame

with open(r"C:\Users\Admin\PycharmProjects\SocketToolsCLI\Aria Math.wav", "rb") as audioFile:
    pygame.init()
    sound = pygame.mixer.Sound(audioFile.read())
    sound.play()
    time.sleep(1000)