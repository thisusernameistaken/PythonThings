import sys, pygame
class MainProgram():
    def __init__():
        pass
    def main():
    #----------------Set Up Window------------------#
        pygame.init()
        pygame.display.set_caption("first pygame")
        pygame.key.set_repeat(1,10)

        size = width, height = 640, 320
        screencolor = 255, 255, 255
        black = 0,0,0
        screen = pygame.display.set_mode(size)
    
    #------------------Game Objects-----------------#
        ball = pygame.image.load("ball.png")
        ballrect = ball.get_rect()
        player = pygame.image.load("player.png")
        playerrect = player.get_rect()
        back = pygame.image.load("background.png")
        backrect = back.get_rect()
        block = pygame.image.load("block.png")
        blockrect = block.get_rect()
        blockrect2 = block.get_rect()
    #---------------Set Obj Start Location-----------# 
        playerrect.topleft = (0, 128)
        blockrect.topleft = (0, 256)
        blockrect2.topleft = (64, 256)
    #-------------------Main Loop-------------------#
        running = True
        pygame.mouse.set_visible(False)
        while running == True:
            cD1()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                   (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        playerrect.x += - 5
                    elif event.key == pygame.K_d:
                        playerrect.x += 5
                    elif event.key == pygame.K_s:
                        playerrect.y += 5
                    elif event.key == pygame.K_w:
                        playerrect.y += - 5

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.line(back,black,playerrect.center, ballrect.center, 1)
                 
            ballrect.center = pygame.mouse.get_pos()
        
                
        #------------Place Sprites-----------------#        
            screen.fill(screencolor)
            screen.blit(back,backrect)
            screen.blit(ball, ballrect)
            screen.blit(player, playerrect)
            screen.blit(block, blockrect)
            screen.blit(block, blockrect2)
            pygame.display.flip()
        else:
            sys.exit
            pygame.quit()

    if __name__ == "__main__":
        main()
main1=MainProgram()
main1.main()
