import time

import pygame

with open(r"C:\Users\Admin\PycharmProjects\SocketToolsCLI\Aria Math.wav", "rb") as audioFile:
    pygame.init()
    sound = pygame.mixer.Sound(audioFile.read())
    sound.play()
    time.sleep(1000)

#
# StayAlive = True
# FullData = b''
# while StayAlive:
#     bufferData = conn.recv(10240)
#     randEmo = random.choice(["❤️", "😍", "🤩", "😁", "🥱", "🤑", "😳", "💩", "🤖", "👾", "🐏", "🐑", "🦈", "🦭"])
#     cli.Animationstr("Receiving bytes:  " + str(len(bufferData))+ f"  {str(randEmo)}", end="\r")
#     if len(bufferData) == 0:
#         StayAlive = False
#     FullData += bufferData
with open("wow.mp3", "wb") as f:
    f.write(FullData)