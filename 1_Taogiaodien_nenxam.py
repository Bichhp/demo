import pygame   #dùng thư viện pygame
from random import randint
pygame.init()   #khởi tạo thư viện
screen=pygame.display.set_mode((1200,700)) #tạo màn hình
pygame.display.set_caption('KMean Visualition') #ghitiêuđề
running=True
clock =pygame.time.Clock()
BACKGROUND=(214,214,214)
BLACK=(0,0,0)
WHITE=(255,255,255)
BACKGROUND_PANEL=(249,255,250)
font=pygame.font.SysFont('sans',40)
text_plus=font.render('+',True,WHITE)
text_min=font.render('-',True,WHITE)
text_run=font.render('Run',True,WHITE)
text_random=font.render('Random',True,WHITE)
text_algorithm=font.render('Algorithm',True,WHITE)
text_reset=font.render('Reset',True,WHITE)
K=0
error=0
points=[]
clusters=[]
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(147,153,35)
SKY=(0,255,255)
ORANGCE=(255,125,25)
GRAPE=(100,155,65)
GRASS=(55,155,65)
COLOR=[RED, GREEN, BLUE, YELLOW, SKY, ORANGCE, GRAPE, GRASS]

while running:
    clock.tick(60)   
    screen.fill(BACKGROUND)  #làm đầy màn hình với màu nền

    #ve giao dien
    #ve panel
    pygame.draw.rect(screen, BLACK, (50,50,700,500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55,55,690,490))
    #ve nut K+
    pygame.draw.rect(screen, BLACK, (850,50,50,50))
    screen.blit(text_plus, (860,50))
    #ve nut K-
    pygame.draw.rect(screen, BLACK, (950,50,50,50))
    screen.blit(text_min, (960,50))
    #k value
    text_k=font.render('K=' +str(K),True,BLACK)
    screen.blit(text_k, (1050,50))
    #run button
    pygame.draw.rect(screen, BLACK, (850,150,150,50))
    screen.blit(text_run, (900,150))
    #random button
    pygame.draw.rect(screen, BLACK, (850,250,150,50))
    screen.blit(text_random, (850,250))
    #Algorithm button
    pygame.draw.rect(screen, BLACK, (850,450,150,50))
    screen.blit(text_algorithm, (850,450))
    #reset button
    pygame.draw.rect(screen, BLACK, (850,550,150,50))
    screen.blit(text_reset, (850,550))
    #text_error
    text_error=font.render('Error=' + str(int(error)),True,BLACK)
    screen.blit(text_error, (850,350))
    
    #ket thuc giao dien
    mouse_x, mouse_y=pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            #tao diem (create points in panel
            if 50<mouse_x<750 and 50<mouse_y<550:
                point=[mouse_x, mouse_y]
                points.append(point)
            
            #change K+
            if 850<mouse_x<900 and 50<mouse_y<100:
                K+=1
                print('Press K+')
            #change K-
            if 950<mouse_x<1000 and 50<mouse_y<100:
                K-=1
                print('Press K-')
            #Run button
            if 850<mouse_x<1000 and 150<mouse_y<200:
                print('Press Run')
            #Random button
            if 850<mouse_x<1000 and 250<mouse_y<300:
                clusters=[]
                for i in range(K):
                    random_point=[randint(55,740), randint(55,540)]
                    clusters.append(random_point)
                print('Press Random')
            #Algorithm button
            if 850<mouse_x<1000 and 450<mouse_y<500:
                print('Press Algorithm')
            #Reset button
            if 850<mouse_x<1000 and 550<mouse_y<600:
                print('Press Reset')
            #Reset button
            if 850<mouse_x<1000 and 550<mouse_y<600:
                print('Press Reset')
    #draw clusters_point
    for i in range(len(clusters)):
        pygame.draw.circle(screen,COLOR[i],(clusters[i][0], clusters[i][1]),10)
    #draw points
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0],points[i][1]),6)
        pygame.draw.circle(screen, WHITE, (points[i][0],points[i][1]),5)
                
    pygame.display.flip() #cập nhật thay đổi màn hình
pygame.quit()


                           
                        
                           
