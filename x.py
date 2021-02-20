import sys, pygame

pygame.init()
size= height, width= 1200,800
speed=[2,2]
screen= pygame.display.set_mode(size)

ball= pygame.image.load('/home/nityaa/Documents/PYTHON/game/images/heart-box.png')
ballrect= ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        ballrect = ballrect.move(speed)
        if ballrect.left<0 or ballrect.right> width:
            speed[0]= -speed[0]
        if ballrect.top<0 or ballrect.bottom> height:
            speed[1]= -speed[1]
        
        screen.fill((0,0,0))
        screen.blit(ball,ballrect)
        pygame.display.flip()
        
        


