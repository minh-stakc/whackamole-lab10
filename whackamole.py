import pygame
import random
def change_value_up(pos):
    return (pos[0]*32, pos[1]*32)
def change_value_down(pos):
    return (pos[0]//32, pos[1]//32)
def random_pos():
    return (random.randrange(0, 20), random.randrange(0, 16))
def main():
    try:
        pygame.init()
        mole_pos = (0,0)
        mole_image = pygame.image.load("whackamole-template\mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            for x in range(32, 640, 32):
                pygame.draw.line(screen, (0,0,0), (x,0), (x,512), width=1)
            for y in range(32, 512, 32):
                pygame.draw.line(screen, (0,0,0), (0,y), (640,y), width=1)
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = change_value_down(event.pos)
                print(x,y)
                if (x,y) == change_value_down(mole_pos): 
                    print(True)
                    mole_pos = change_value_up(random_pos())
                else: print(False)
                print(mole_pos)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
