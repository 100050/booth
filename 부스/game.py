import sys
import pygame #pygame 라이브러리 불러오기
from pygame.locals import *
import ctypes

#게임창의 높이
WHITE = (255, 255, 255) #흰색
width = 1920
height = 1080
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) #해상도 구하기
surface = pygame.display.set_mode((width, height))
background1_width = 1920 #배경 연결할려고 배경2 x좌표임(모르겠으면 물어봐)
background2_width = 1920 #배경 연결할려고 배경2 x좌표임(모르겠으면 물어봐)


#충돌1(말벌 독침1)
def crash0(a, b):
    global ms1_x, vel_y, Hp #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 180
    y_pos_a = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y == 12:
        y_pos_a = 322
    elif vel_y == 13: #점프값 고치면 고쳐야됨
        y_pos_a = 335

    x_pos_b = ms1_x + 10
    y_pos_b = 335

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        if Hp == 3:
            Hp = 2
        elif Hp == 2:
            Hp = 1
        elif Hp == 1:
            Hp = 0

#충돌2(말벌 독침2)
def crash1(a, b):
    global ms2_x, vel_y, Hp #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 180
    y_pos_a = 0

    x_pos_b = ms2_x + 10
    y_pos_b = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y == 12:
        y_pos_a = 310
        y_pos_b = 310
    elif vel_y == 13: #점프값 고치면 고쳐야됨
        y_pos_a = 335
        y_pos_b = 0

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        if Hp == 3:
            Hp = 2
        elif Hp == 2:
            Hp = 1
        elif Hp == 1:
            Hp = 0

#충돌2(곰돌이)
def crash2(a, b):
    global bear_x, vel_y, Hp #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 180
    y_pos_a = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y == 12:
        y_pos_a = 322
    elif vel_y == 13: #점프값 고치면 고쳐야됨
        y_pos_a = 335

    x_pos_b = bear_x + 20
    y_pos_b = 350

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        if Hp == 3:
            Hp = 2
        elif Hp == 2:
            Hp = 1
        elif Hp == 1:
            Hp = 0

#충돌3(파리지옥)
def crash3(a, b):
    global dionaea_x, vel_y, Hp #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 180
    y_pos_a = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y == 12:
        y_pos_a = 310
    if vel_y == 13: #점프값 고치면 고쳐야됨
        y_pos_a = 335

    x_pos_b = dionaea_x
    y_pos_b = 335

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        if Hp == 3:
            Hp = 2
        elif Hp == 2:
            Hp = 1
        elif Hp == 1:
            Hp = 0

#배경
def back(background, x, y): #배경, 위치(x, y)
    surface.blit(background, (x, y)) #위에는 설정이고 이건 화면에서 보이게 하는거임

#땅
def earth1(earth1, x, y): #배경, 위치(x, y)
    surface.blit(earth1, (x, y)) #위에는 설정이고 이건 화면에서 보이게 하는거임

#구름
def obstacle0(cloud, x, y):
    surface.blit(cloud, (x, y))

#장애물임(말벌 독침)
def obstacle1(bt, x, y):
    surface.blit(bt, (x, y))

#장애물임(곰돌이)
def obstacle2(bear, x, y):
    surface.blit(bear, (x, y))

#장애물임(파리지옥)
def obstacle3(dionaea, x, y):
    surface.blit(dionaea, (x, y))

#플레이어 
def bee(beecraft, x, y): #위치
    surface.blit(beecraft, (x, y)) #이것도 화면상에 보이게 하는거

#사각형1
def rt1():
    global ms1_y
    pygame.draw.rect(surface, (225, 117, 125), (0, 365, 700, 50))

#사각형2
def rt2():
    global ms1_y
    pygame.draw.rect(surface, (225, 117, 125), (0, 270, 700, 50))

#게임 실행
def runGame():
    global gamepad, clock, background1, background2, bigbee, bigbee_x, bigbee_y, vel_y, ms1, ms1_x, ms1_y, ms2_x, ms2_y, hp3, hp2, hp1, Hp, oj
    global floor1, floor2, cloud1, cloud2, cloud3, watermark, beecraft1, beecraft2, ms2, bear1, bear2, bear3, bear_x, dionaea_x, diebear, diedionaea, diebigbee
    global bigbee1, bigbee2, bigbee3, bigbee4, bigbee5, bigbee6, bigbee7, bigbee8, bigbee9, dionaea1, dionaea2, dionaea3, dionaea4, dionaea5, startscreen
    #왼쪽부터 화면상에 그리기, 플레이어, 시간(프레임), 장애물

    x = 180 #플레이어 x축 위치
    y = 335 #플레이어 y축 위치
    vel_y = 13 #점프값
    jump = False #점프 트루되면 점프됨

    Hp = 3 #HP
    HP = hp3

    start = False
 
    oj = 0 #장애물 위치 설정할려고 만든 변수
    bigbee_x = 1024 - 580
    bigbee_y = 512 #512

    ms1_x = 700 #독침
    ms1_y = 370
    ms2_x = 700
    ms2_y = 280

    bear_x = 1024 #곰탱이 x, y 좌표
    bear_y = 340

    dionaea_x = 1024 #파리지옥 x, y 좌표
    dionaea_y = 335
    flower = False

    background1_x = 0 #배경1

    floor1_x = 0 #배경1
    floor2_x = background2_width #배경 오래가게 하는거

    cloud1_x = 60 #구름1
    cloud_y = 20
    cloud2_x = background1_width #구름2
    cloud3_x = 300 #구름3

    #게임 종료 코드 True되면 꺼짐
    keyC = 0
    while keyC == 0:

        for event in pygame.event.get():...

        if event.type == pygame.QUIT:
            keyC = 1

        userInput = pygame.key.get_pressed() #이게 키넣는 이벤트 넣게 해주는 그런 코드임

        if jump is False and userInput[pygame.K_SPACE]: # 주먹일 때 점프 // 스페이스바 누르면 작동되는거 userInput[pygame.K_SPACE]
            jump = True #트루로 만들어서 아래 코드 작동

        if jump is True:
            y -= vel_y #y값에서 뺴야 올라감 젤 위는 0임
            vel_y -= 1 #다음 코드 작동할려고 뺴는거 13에서 12로 만듬
            if vel_y < -13:
                jump = False #점프가 거짓이 되어 멈춤
                vel_y = 13 #다시 원래 자리로 가버림

        pygame.time.delay(1)
        pygame.display.update() #실행될떄마다 계속 업데이트

        if userInput[pygame.K_1]: # 따봉일 때 시작// 키보드 1을 누르면 게임 시작 userInput[pygame.K_1]
            start = True

        floor1_x -= 32 #땅 속도
        floor2_x -= 32

        cloud1_x -= 4 #구름 속도
        cloud2_x -= 4
        cloud3_x -= 4
        
        back(background1, background1_x, 0) #위에 back에 넣는거

        if cloud1_x == -400: #배경1은 원본 배경2는 복사본임, 1024 맞아떨어져야 if문 실행
            cloud1_x = background1_width #배경1이 화면에서 사라지면 배경2가 나타나는 구조임

        if cloud2_x == -400:
            cloud2_x = background1_width
            
        if cloud3_x == -400:
            cloud3_x = background1_width

        if floor1_x == -background2_width: #배경1은 원본 배경2는 복사본임, 1024 맞아떨어져야 if문 실행
            floor1_x = background2_width #배경1이 화면에서 사라지면 배경2가 나타나는 구조임

        if floor2_x == -background2_width:
            floor2_x = background2_width   

        if Hp == 3:
            HP = hp3
        elif Hp == 2:
            HP = hp2
        elif Hp == 1:
            HP = hp1

        #구름
        obstacle0(cloud1, cloud1_x, cloud_y)
        obstacle0(cloud2, cloud2_x, cloud_y)
        obstacle0(cloud3, cloud3_x, cloud_y)

        #워터마크
        obstacle0(watermark, -20, -10)
        obstacle0(HP, 100, 100) #HP
        
        earth1(floor1, floor1_x, 185) #위에 back에 넣는거
        earth1(floor2, floor2_x, 185) #배경 위에 그릴 이미지들은 이 뒤에 그려야 됨

        #말벌 장애물 실행 코드
        if keyC == 0 and start == True:
            oj += 1
            if oj >= 100:
                if oj % 9 == 0:
                    obstacle0(bigbee1, bigbee_x, bigbee_y) #말벌 애니메이션
                elif oj % 9 == 1:
                    obstacle0(bigbee2, bigbee_x, bigbee_y)
                elif oj % 9 == 2:
                    obstacle0(bigbee3, bigbee_x, bigbee_y)
                elif oj % 9 == 3:
                    obstacle0(bigbee4, bigbee_x, bigbee_y)
                elif oj % 9 == 4:
                    obstacle0(bigbee5, bigbee_x, bigbee_y)
                elif oj % 9 == 5:
                    obstacle0(bigbee6, bigbee_x, bigbee_y)
                elif oj % 9 == 6:
                    obstacle0(bigbee7, bigbee_x, bigbee_y)
                elif oj % 9 == 7:
                    obstacle0(bigbee8, bigbee_x, bigbee_y)
                elif oj % 9 == 8:
                    obstacle0(bigbee9, bigbee_x, bigbee_y)
                bigbee_y -= 10
                if bigbee_y <= -110:
                    bigbee_y = -110
                if oj >= 300:
                    bigbee_x -= 10   

            #말벌 독침1 실행코드
            if oj >= 100 and oj < 109:
                rt1()
            elif oj >= 110:
                obstacle1(ms1, ms1_x, ms1_y)
                ms1_x -= 20

            #말벌 독침2 실행코드
            if oj >= 30 and oj < 39:
                rt2()
            elif oj >= 40:
                obstacle1(ms2, ms2_x, ms2_y)
                ms2_x -= 20

            if oj >= 50:
                if oj % 27 <= 8:
                    obstacle2(bear1, bear_x, bear_y) #곰도리 애니메이션
                elif oj % 27 <= 17:
                    obstacle2(bear2, bear_x, bear_y)
                elif oj % 27 <= 26:
                    obstacle2(bear3, bear_x, bear_y)
                bear_x -= 10
            
            if oj >= 120:
                if oj % 100 <= 19 and flower == False:
                    obstacle3(dionaea1, dionaea_x, dionaea_y) #파리지옥 애니메이션
                elif oj % 100 <= 39 and flower == False:
                    obstacle3(dionaea2, dionaea_x, dionaea_y)
                elif oj % 100 <= 59 and flower == False:
                    obstacle3(dionaea3, dionaea_x, dionaea_y) 
                elif oj % 100 <= 79 and flower == False:
                    obstacle3(dionaea4, dionaea_x, dionaea_y)
                    flower = True
                elif oj % 100 <= 99 and flower == True:
                    obstacle3(dionaea5, dionaea_x, dionaea_y)
                dionaea_x -= 10

            if oj % 2 == 0:
                bee(beecraft[0], x, y) #플레이어 애니메이션
            elif oj % 2 == 1:
                bee(beecraft[1], x, y)

        if start == False:
            obstacle0(startscreen, 0, 0)
            oj = 0

        #죽는 화면

        #충돌
        crash0(beecraft[0] or beecraft[1], ms1)
        crash1(beecraft[0] or beecraft[1], ms2)
        crash2(beecraft[0] or beecraft[1], bear1 or bear2 or bear3)
        crash3(beecraft[0] or beecraft[1], dionaea1 or dionaea2 or dionaea3 or dionaea4 or dionaea5)

        pygame.display.update() #화면 업데이트
        clock.tick(60) #프레임

    pygame.quit()
    quit() #화면 닫으면 나가지는 코드

#게임 초기화 코드
def initGame():
    global gamepad, beecraft, clock, background1, background2, bigbee, ms1, floor1, floor2, cloud1, cloud2, cloud3, watermark, beecraft1, beecraft2, hp1, hp2, hp3
    global bigbee1, bigbee2, bigbee3, bigbee4, bigbee5, bigbee6, bigbee7, bigbee8, bigbee9, ms2, bear1, bear2, bear3, dionaea1, dionaea2, dionaea3, dionaea4, dionaea5
    global diebear, diedionaea, diebigbee, startscreen
    global beecraft
    route = 'D:/코딩 김인환/Python/부스/object/'
    pygame.init()
    pygame.display.set_caption('야꿀벌') #타이틀 제목
    # beecraft1 = pygame.image.load(route+'honeybee/honeybee1.png').convert_alpha() #캐릭터 이미지
    # beecraft1 = pygame.transform.scale(beecraft1, (100, 100)) #이미지 크기 바꿈
    # beecraft2 = pygame.image.load(route+'honeybee/honeybee2.png').convert_alpha() #캐릭터 이미지
    # beecraft2 = pygame.transform.scale(beecraft2, (100, 100)) #이미지 크기 바꿈
    beecraft = [pygame.image.load('object/honeybee/honeybee1.png').convert_alpha(), pygame.image.load(route+'honeybee/honeybee2.png').convert_alpha()]
    beecraft[0] = pygame.transform.scale(beecraft[0], (100, 100))
    beecraft[1] = pygame.transform.scale(beecraft[1], (100, 100))
    bigbee1 = pygame.image.load(route+'wasp/말벌1.png').convert_alpha() #말벌 이미지
    bigbee1 = pygame.transform.scale(bigbee1, (800, 800))
    bigbee2 = pygame.image.load(route+'wasp/말벌2.png').convert_alpha()
    bigbee2 = pygame.transform.scale(bigbee2, (800, 800))
    bigbee3 = pygame.image.load(route+'wasp/말벌3.png').convert_alpha()
    bigbee3 = pygame.transform.scale(bigbee3, (800, 800))
    bigbee4 = pygame.image.load(route+'wasp/말벌4.png').convert_alpha()
    bigbee4 = pygame.transform.scale(bigbee4, (800, 800))
    bigbee5 = pygame.image.load(route+'wasp/말벌5.png').convert_alpha()
    bigbee5 = pygame.transform.scale(bigbee5, (800, 800))
    bigbee6 = pygame.image.load(route+'wasp/말벌6.png').convert_alpha()
    bigbee6 = pygame.transform.scale(bigbee6, (800, 800))
    bigbee7 = pygame.image.load(route+'wasp/말벌7.png').convert_alpha()
    bigbee7 = pygame.transform.scale(bigbee7, (800, 800))
    bigbee8 = pygame.image.load(route+'wasp/말벌8.png').convert_alpha()
    bigbee8 = pygame.transform.scale(bigbee8, (800, 800))
    bigbee9 = pygame.image.load(route+'wasp/말벌9.png').convert_alpha()
    bigbee9 = pygame.transform.scale(bigbee9, (800, 800))
    floor1 = pygame.image.load(route+'floor.png') #땅 이미지
    floor1 = pygame.transform.scale(floor1, (1920, 600))
    floor2 = floor1.copy()
    background1 = pygame.image.load(route+'background.png') #게임배경 이미지
    background1 = pygame.transform.scale(background1, (1920, 1080))
    ms1 = pygame.image.load(route+'wasp/poisoned needle.png') #말벌 독침 이미지
    ms1 = pygame.transform.scale(ms1, (50, 50))
    ms2 = ms1.copy() 
    cloud1 = pygame.image.load(route+'cloud/cloud1.png') #구름 이미지
    cloud1 = pygame.transform.scale(cloud1, (600, 300))
    cloud2 = pygame.image.load(route+'cloud/cloud2.png') #구름 이미지
    cloud2 = pygame.transform.scale(cloud2, (700, 300))
    cloud3 = pygame.image.load(route+'cloud/cloud3.png') #구름 이미지
    cloud3 = pygame.transform.scale(cloud3, (600, 300))
    watermark = pygame.image.load(route+'watermark.png') #워터마크 이미지
    watermark = pygame.transform.scale(watermark, (900, 500))
    bear1 = pygame.image.load(route+'Bear/bear1.png') #곰 이미지
    bear1 = pygame.transform.scale(bear1, (100, 100))
    bear2 = pygame.image.load(route+'Bear/bear2.png')
    bear2 = pygame.transform.scale(bear2, (100, 100))
    bear3 = pygame.image.load(route+'Bear/bear3.png')
    bear3 = pygame.transform.scale(bear3, (100, 100))
    dionaea1 = pygame.image.load(route+'Dionaea/Dionaea1.png') #파리지옥 이미지
    dionaea1 = pygame.transform.scale(dionaea1, (80, 100))
    dionaea2 = pygame.image.load(route+'Dionaea/Dionaea2.png')
    dionaea2 = pygame.transform.scale(dionaea2, (80, 100))
    dionaea3 = pygame.image.load(route+'Dionaea/Dionaea3.png')
    dionaea3 = pygame.transform.scale(dionaea3, (80, 100))
    dionaea4 = pygame.image.load(route+'Dionaea/Dionaea4.png') 
    dionaea4 = pygame.transform.scale(dionaea4, (80, 100))
    dionaea5 = pygame.image.load(route+'Dionaea/Dionaea5.png')
    dionaea5 = pygame.transform.scale(dionaea5, (80, 100))
    hp1 = pygame.image.load(route+'hp1.png') #HP 이미지(1이 목숨 한개뿐인거)
    hp1 = pygame.transform.scale(hp1, (500, 500))
    hp2 = pygame.image.load(route+'hp2.png')
    hp2 = pygame.transform.scale(hp2, (500, 500))
    hp3 = pygame.image.load(route+'hp3.png')
    hp3 = pygame.transform.scale(hp3, (500, 500))
    diebear = pygame.image.load(route+'death message/death message bear.png')
    diedear = pygame.transform.scale(diebear, (1920, 1080))
    diedionaea = pygame.image.load(route+'death message/death message Dionaea.png')
    diedionaea = pygame.transform.scale(diedionaea, (1920, 1080))
    diebigbee = pygame.image.load(route+'death message/death message wasp.png')
    diebigbee = pygame.transform.scale(diebigbee, (1920, 1080))
    startscreen = pygame.image.load(route+'start screen.png')
    startscreen = pygame.transform.scale(startscreen, (1920, 1080)) #시작화면

    clock = pygame.time.Clock() #다시 키면 다시 재생되게 할려고 초기화 코드넣는거

    runGame()

if __name__ == '__main__':
    initGame() #초기화 시킴  