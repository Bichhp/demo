import pygame
import time
import math
pygame.init()
screen =pygame.display.set_mode((600,600))
GREY=(150,150,150)
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
runing=True
start=False
total_secs=0
total=0

r_secs=90
r_min=40
nhac=pygame.mixer.Sound('C:/Users/PC/Downloads/daucoloilam.mp3.mp3')

clock=pygame.time.Clock()

font=pygame.font.SysFont('sans', 50)
text_1=font.render('+',True, BLACK)
text_2=font.render('-',True, BLACK)
text_3=font.render('+',True, BLACK)
text_4=font.render('-',True, BLACK)
text_5=font.render('Start',True, BLACK)
text_6=font.render('Reset',True, BLACK)

while runing:
    clock.tick(60)
    screen.fill(GREY)
    mouse_x, mouse_y=pygame.mouse.get_pos()
    pygame.draw.rect(screen, WHITE,(100,50,50,50))
    pygame.draw.rect(screen, WHITE,(100,200,50,50))
    pygame.draw.rect(screen, WHITE,(200,50,50,50))
    pygame.draw.rect(screen, WHITE,(200,200,50,50))
    pygame.draw.rect(screen, WHITE,(300,50,150,50))
    pygame.draw.rect(screen, WHITE,(300,150,150,50))
    screen.blit(text_1, (100,50))
    screen.blit(text_2, (100,200))
    screen.blit(text_3, (200,50))
    screen.blit(text_4, (200,200))
    screen.blit(text_5, (300,50))
    screen.blit(text_6, (300,150))
    pygame.draw.rect(screen, BLACK, (50,520,400,50)) #thanh lùi
    pygame.draw.rect(screen, WHITE, (60,530,380,30)) #thanh lùi
    pygame.draw.circle(screen, BLACK, (250,400), 100)
    pygame.draw.circle(screen, WHITE, (250,400), 95)
    pygame.draw.circle(screen, BLACK, (250,400), 5)
    
    #pygame.draw.line(screen, BLACK, (250,400), (250,310))
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runing=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                pygame.mixer.pause()
               
    
                if 100<mouse_x< 150 and 50<mouse_y<100:
                    total_secs+=60
                    total=total_secs

                    print('Press + min')
                if 100<mouse_x< 150 and 200<mouse_y<250:
                    total_secs-=60
                    total=total_secs
                    print('Press - min')
                if 200<mouse_x< 250 and 50<mouse_y<100:
                    total_secs+=1
                    total=total_secs

                    print('Press + secs')
                if 200<mouse_x< 250 and 200<mouse_y<250:
                    total_secs-=1
                    total=total_secs

                    print('Press - secs')   

                if (300<mouse_x< 450) and (50<mouse_y<100):
                    start=True
                    total=total_secs
                    print(' Press Start')
                    
                if 300<mouse_x< 400 and 150<mouse_y<200:
                    total_secs=0
                   
                    print('press Reset')
            #print('total_secs:'+str(total_secs))    
    
    if start:
        total_secs-=1
        if total_secs==0:
            start=False
            pygame.mixer.Sound.play(nhac)
        time.sleep(0.05)
    if total_secs<=0:
        total_secs=0
        start=0
       
    mins=int(total_secs/60)
    secs=total_secs-mins*60
      
    time1=str(mins)+":" +str(secs)
    text_time=font.render(time1, True, BLACK)
    screen.blit(text_time, (120,120))
  
    x_secs=250+90*math.sin(6*secs*math.pi/180)
    y_secs=400-90*math.cos(6*secs*math.pi/180)
    pygame.draw.line(screen, BLACK, (250,400), (int(x_secs), int(y_secs)))
 
    x_min=250+40*math.sin(6*mins*math.pi/180)
    y_min=400-40*math.cos(6*mins*math.pi/180)
    pygame.draw.line(screen, RED, (250,400), (int(x_min), int(y_min)))
  
    if total!=0:
        pygame.draw.rect(screen, RED, (60,530, int(380*(total_secs/total)),30))
                   
    pygame.display.flip()
pygame.quit()
