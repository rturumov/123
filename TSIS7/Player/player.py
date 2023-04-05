import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("PyGame Player")

playlist = ['c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - Smells Like Teen Spirit.mp3',
            'c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - In Bloom.mp3',
            'c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - Come As You Are.mp3',
            'c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - Breed.mp3',
            'c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - Lithium.mp3',
            'c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - Polly.mp3',
            'c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - Territorial Pissings.mp3',
            'c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - Drain You.mp3',
            'c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - Lounge Act.mp3',
            'c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - Stay Away.mp3',
            'c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - On A Plain.mp3',
            'c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - Something In The Way.mp3',
            'c:/Users/User/Desktop/pp2/pp2-22B030603/TSIS7/Player/Nirvana - Endless, Nameless.mp3']

i = 0
j = 0

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                i += 1
                if i == 1:
                    pygame.mixer.music.load(playlist[0])
                    pygame.mixer.music.play()
                elif i % 2 == 0:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                j += 1
                i = 1
                if j < len(playlist):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                else:
                    j = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                
            elif event.key == pygame.K_LEFT:
                j -= 1
                i = 1
                if j > -len(playlist):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                else:
                    j = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(playlist[j])
                    pygame.mixer.music.play()
                
                