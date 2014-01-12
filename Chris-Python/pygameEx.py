import sys, pygame #imports stuff

def main():#Make a method
    pygame.init()#begins it

    pygame.display.set_caption('Pygame Example')
    
    size = width, height = 640, 320 #sets the size of the window
    black = 0, 0, 0#makes a color (dont really need)
    screen = pygame.display.set_mode(size)# puts the screen size to the display
    ball = pygame.image.load("ball.png")#example: load an image
    ballrect = ball.get_rect()
    running=True#sets mainloop
    #---------------MainLoop---------------#
    while running ==True:
 #       ballrect=pygame.mouse.get_cursor()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
             #Checks if the program is exited
                running=False# Stops the mainloop
            if event.type==pygame.KEYUP and event.key == pygame.K_UP:
                ballrect.y-=50
                print ballrec
                print pygame.mouse.get_cursor()
        screen.fill(black)# puts background color
        screen.blit(ball, ballrect)#adds image to screen
        pygame.display.flip()#relods the screen for updates every second
    else :
        sys.exit
        pygame.quit()
        
if __name__ == '__main__':
    main() #Call the method
