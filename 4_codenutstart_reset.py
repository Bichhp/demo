import pygame
import time
import math

pygame.init()

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('Dong ho dem nguoc')
GREY=(150,150,150)
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
font=pygame.font.SysFont('sans',40)
text1=font.render('+', True, BLACK)
text2=font.render('-', True, BLACK)
text_sta=font.render('Start', True, BLACK)
text_re=font.render('Reset', True, BLACK)
total_secs=0
total=0
runing=True
start=False
clock=pygame.time.Clock()
while runing:
    clock.tick(60)
    screen.fill((GREY))
    pygame.draw.rect(screen, WHITE, (100,50, 50,50))
    screen.blit(text1, (110,55))
    pygame.draw.rect(screen, WHITE, (200,50, 50,50))
    screen.blit(text1, (210,55))
    pygame.draw.rect(screen, WHITE, (100,200, 50,50))
    screen.blit(text2, (110,205))
    pygame.draw.rect(screen, WHITE, (200,200, 50,50))
    screen.blit(text2, (210,205))
    pygame.draw.rect(screen, WHITE, (300,50, 100,50))
    screen.blit(text_sta, (300,50))
    pygame.draw.rect(screen, WHITE, (300,200, 100,50))
    screen.blit(text_re, (300,200))
    
    pygame.draw.circle(screen, BLACK, (250,400), 100)
    pygame.draw.circle(screen, WHITE, (250,400), 95)
    pygame.draw.circle(screen, BLACK, (250,400), 5)
    pygame.draw.line(screen, BLACK, (250, 400), (250,  310))
    pygame.draw.rect(screen, BLACK, (100,510, 300,50))
    #pygame.draw.rect(screen, RED, (105,515, 290,40))
    mouse_x, mouse_y=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runing=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1: #chuot trai
                if 100 <=mouse_x <=150 and 50<=mouse_y<=100:
                    total_secs+=60
                    print('press +')
                if 200 <=mouse_x <=250 and 50<=mouse_y<=100:
                    total_secs+=1
                    print('press +')
                if 100 <=mouse_x <=150 and 200<=mouse_y<=250:
                    total_secs-=60
                    print('press -')
                if 200 <=mouse_x <=250 and 200<=mouse_y<=250:
                    total_secs-=1
                if 300 <=mouse_x <=400 and 50<=mouse_y<=100:
                    start=True
                    print('Start')
                if 300 <=mouse_x <=400 and 200<=mouse_y<=250:
                    total_secs=0
                    print('Reset')

    
    if start==True:
        total_secs-=1
        if total_secs==0:
            start=False
       
        time.sleep(0.05)
    if total_secs<=0:
        total_secs=0
        start=0
                       
    mins=(total_secs//60)
    secs=total_secs-mins*60
    time1=str(mins) + ":" + str(secs)
    text_time=font.render(time1, True, BLACK)
    screen.blit(text_time, (120, 120))

    x_secs=250+90 * (math.sin(6*secs*math.pi/180))
    y_secs=400-90 * (math.cos(6*secs*math.pi/180))
    pygame.draw.line(screen, BLACK, (250,400), (int(x_secs), int(y_secs)))

    x_mins=250+40 * (math.sin(6*mins*math.pi/180))
    y_mins=400-40 * (math.cos(6*mins*math.pi/180))
    pygame.draw.line(screen, RED, (250,400), (int(x_mins), int(y_mins)))

    
        

    pygame.display.flip()
pygame.quit()
