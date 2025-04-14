import pygame
import time

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load("./assets/power down.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

# Wait while the music plays
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
