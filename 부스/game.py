import sys
import pygame #pygame 라이브러리 불러오기
from pygame.locals import *
import ctypes
import tensorflow
import cv2
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 모델 위치
model_filename ='C:/Users/User/Desktop/29/부스/keras_model.h5'

# 케라스 모델 가져오기
model = tensorflow.keras.models.load_model(model_filename, compile=False)

# 카메라를 제어할 수 있는 객체
capture = cv2.VideoCapture(0)

# 카메라 길이 너비 조절
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# 이미지 처리하기
def preprocessing(frame):
    #frame_fliped = cv2.flip(frame, 1)
    # 사이즈 조정 티쳐블 머신에서 사용한 이미지 사이즈로 변경해준다.
    size = (224, 224)
    frame_resized = cv2.resize(frame, size, interpolation=cv2.INTER_AREA)
    
    # 이미지 정규화
    # astype : 속성
    frame_normalized = (frame_resized.astype(np.float32) / 127.0) - 1

    # 이미지 차원 재조정 - 예측을 위해 reshape 해줍니다.
    # keras 모델에 공급할 올바른 모양의 배열 생성
    frame_reshaped = frame_normalized.reshape((1, 224, 224, 3))
    #print(frame_reshaped)
    return frame_reshaped

# 예측용 함수
def predict(frame):
    prediction = model.predict(frame)
    return prediction

#게임창의 높이
WHITE = (255, 255, 255) #흰색
width = 1920
height = 1080
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) #해상도 구하기
surface = pygame.display.set_mode((width, height))
background1_width = 1920 #배경 연결할려고 배경2 x좌표임(모르겠으면 물어봐)
background2_width = 1920 #배경 연결할려고 배경2 x좌표임(모르겠으면 물어봐)
HP = 3

#충돌0(말벌 독침1, 위에 날라오는거)
def crash0(a, b):
    global ms1_x, vel_y, HP #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 290
    y_pos_a = 0

    x_pos_b = ms1_x + 50
    y_pos_b = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y > 90:
        y_pos_a = 190
        y_pos_b = 190
    elif vel_y == 90: #점프값 고치면 고쳐야됨
        y_pos_a = 640
        y_pos_b = 0

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        print('충돌했습니다')
        if HP == 3:
            HP = 2
            return 2
        elif HP == 2:
            HP = 1
            return 2
        elif HP == 1:
            HP = 3
            return 2
    else:
        return 0

#충돌1(말벌 독침2, 밑에 부분)
def crash1(a, b):
    global ms2_x, vel_y, HP #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 290
    y_pos_a = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y > 90:
        y_pos_a = 190
    elif vel_y == 90: #점프값 고치면 고쳐야됨
        y_pos_a = 640

    x_pos_b = ms2_x + 50
    y_pos_b = 640

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        print('충돌했습니다')
        if HP == 3:
            HP = 2
            return 2
        elif HP == 2:
            HP = 1
            return 2
        elif HP == 1:
            HP = 3
            return 2
    else:
        return 0

#충돌2(곰돌이1)
def crash2(a, b):
    global bear1_x, vel_y, HP #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 290
    y_pos_a = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y > 90:
        y_pos_a = 190
    elif vel_y == 90: #점프값 고치면 고쳐야됨
        y_pos_a = 640

    x_pos_b = bear1_x + 50
    y_pos_b = 640

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        print('충돌했습니다')
        if HP == 3:
            HP = 2
            return 2
        elif HP == 2:
            HP = 1
            return 2
        elif HP == 1:
            HP = 3
            return 2
    else:
        return 0

#충돌3(파리지옥1)
def crash3(a, b):
    global dionaea1_x, vel_y, HP #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 290
    y_pos_a = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y > 90:
        y_pos_a = 190
    elif vel_y == 90: #점프값 고치면 고쳐야됨
        y_pos_a = 640

    x_pos_b = dionaea1_x + 40
    y_pos_b = 640

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        print('충돌했습니다')
        if HP == 3:
            HP = 2
            return 2
        elif HP == 2:
            HP = 1
            return 2
        elif HP == 1:
            HP = 3
            return 2
    else:
        return 0

#충돌4(곰돌이2)
def crash4(a, b):
    global bear2_x, vel_y, HP #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 290
    y_pos_a = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y > 90:
        y_pos_a = 190
    elif vel_y == 90: #점프값 고치면 고쳐야됨
        y_pos_a = 640

    x_pos_b = bear2_x + 50
    y_pos_b = 640

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        print('충돌했습니다')
        if HP == 3:
            HP = 2
            return 2
        elif HP == 2:
            HP = 1
            return 2
        elif HP == 1:
            HP = 3
            return 2
    else:
        return 0

#충돌5(파리지옥2)
def crash5(a, b):
    global dionaea2_x, vel_y, HP #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 290
    y_pos_a = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y > 90:
        y_pos_a = 190
    elif vel_y == 90: #점프값 고치면 고쳐야됨
        y_pos_a = 640

    x_pos_b = dionaea2_x + 40
    y_pos_b = 640

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        print('충돌했습니다')
        if HP == 3:
            HP = 2
            return 2
        elif HP == 2:
            HP = 1
            return 2
        elif HP == 1:
            HP = 3
            return 2
    else:
        return 0

#충돌6(곰돌이3)
def crash6(a, b):
    global bear3_x, vel_y, HP #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 290
    y_pos_a = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y > 90:
        y_pos_a = 190
    elif vel_y == 90: #점프값 고치면 고쳐야됨
        y_pos_a = 640

    x_pos_b = bear3_x + 50
    y_pos_b = 640

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        print('충돌했습니다')
        if HP == 3:
            HP = 2
            return 2
        elif HP == 2:
            HP = 1
            return 2
        elif HP == 1:
            HP = 3
            return 2
    else:
        return 0

#충돌7(파리지옥3)
def crash7(a, b):
    global dionaea4_x, vel_y, HP #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 290
    y_pos_a = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y > 90:
        y_pos_a = 190
    elif vel_y == 90: #점프값 고치면 고쳐야됨
        y_pos_a = 640

    x_pos_b = dionaea4_x + 40
    y_pos_b = 640

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        print('충돌했습니다')
        if HP == 3:
            HP = 2
            return 2
        elif HP == 2:
            HP = 1
            return 2
        elif HP == 1:
            HP = 3
            return 2
    else:
        return 0

#충돌8(곰돌이4)
def crash8(a, b):
    global bear4_x, vel_y, HP #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 290
    y_pos_a = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y > 90:
        y_pos_a = 190
    elif vel_y == 90: #점프값 고치면 고쳐야됨
        y_pos_a = 640

    x_pos_b = bear4_x + 50
    y_pos_b = 640

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        print('충돌했습니다')
        if HP == 3:
            HP = 2
            return 2
        elif HP == 2:
            HP = 1
            return 2
        elif HP == 1:
            HP = 3
            return 2
    else:
        return 0

#충돌9(꽃 아이템)
def crash9(a, b):
    global flower_x, vel_y, HP, what #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 290
    y_pos_a = 0

    x_pos_b = flower_x + 50
    y_pos_b = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y > 90:
        y_pos_a = 190
        y_pos_b = 190
    elif vel_y == 90: #점프값 고치면 고쳐야됨
        y_pos_a = 640
        y_pos_b = 0

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        what = True

#충돌10(말벌 필살기)
def crash10(a, b):
    global ms3_x, vel_y, HP #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = 290
    y_pos_a = 190

    x_pos_b = ms3_x
    y_pos_b = 190

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        print('충돌했습니다')
        if HP == 3:
            HP = 2
            return 2
        elif HP == 2:
            HP = 1
            return 2
        elif HP == 1:
            HP = 3
            return 2
    else:
        return 0

#충돌11(끝)
def crash11(a, b):
    global honey_x, vel_y, HP #이거 원리는 이미지에 충돌상자를 만들어서 충돌상자가 부딪히며 실행되는거임
    rect_a = a.get_rect()
    rect_b = b.get_rect()
    
    #상자 좌표
    x_pos_a = honey_x
    y_pos_a = 0

    x_pos_b = 1850
    y_pos_b = 0

    #점프했을때 충돌 안 나게 할려는 조건문
    if vel_y > 90:
        y_pos_a = 190
        y_pos_b = 190
    elif vel_y == 90: #점프값 고치면 고쳐야됨
        y_pos_a = 640
        y_pos_b = 640

    rect_a.topleft = (x_pos_a, y_pos_a)
    rect_b.topleft = (x_pos_b, y_pos_b)

    if rect_b.colliderect(rect_a):
        print('클리어했습니다')
        if HP == 3:
            return 2
        elif HP == 2:
            HP = 3
            return 2
        elif HP == 1:
            HP = 3
            return 2
    else:
        return 0
        
#장애물
def obstacle(cloud, x, y):
    surface.blit(cloud, (x, y))

#사각형1
def rt1():
    pygame.draw.rect(surface, (225, 117, 125), (0, 440, 1230, 90))

#사각형2
def rt2():
    pygame.draw.rect(surface, (225, 117, 125), (0, 710, 1230, 90))

def rt3():
    pygame.draw.rect(surface, (225, 117, 125), (0, 0, 1920, 1080))

    #생명
def health():
    global hp3, hp2, hp1, diebigbee, Hp
    Hp = hp3  #HP

    if HP == 3:
        Hp = hp3
        obstacle(Hp, 1000, -10)  # HP 그리기
    elif HP == 2:
        Hp = hp2
        obstacle(Hp, 1000, -10)  # HP 그리기
    elif HP == 1:
        Hp = hp1
        obstacle(Hp, 1000, -10)  # HP 그리기

def Startscreen():
    global startscreen
    if HP == 3:
        obstacle(startscreen, 0, 0)

#게임 실행
def runGame():
    global clock, background1, bigbee_x, bigbee_y, vel_y, ms1, ms1_x, ms1_y, ms2_x, ms2_y, oj, bear5, bear6, bear7, bear8, bear9, ms3, ms3_x
    global floor1, floor2, cloud1, cloud2, cloud3, watermark, beecraft1, beecraft2, ms2, bear1, bear2, bear3, diebear, diedionaea, diebigbee
    global bigbee1, bigbee2, bigbee3, bigbee4, bigbee5, bigbee6, bigbee7, bigbee8, bigbee9, dionaea1, dionaea2, dionaea3, dionaea4, dionaea5, startscreen
    global bigbee10, bigbee11, bigbee12, bigbee13, dionaea6, dionaea7, dionaea8, dionaea9, dionaea10, bear4, bear5, bear6, Hp, Honeycomb, what, start
    global dionaea11, dionaea12, dionaea13, dionaea14, dionaea15, dionaea16, dionaea17, dionaea18, dionaea19, dionaea20, bear10, bear11, bear12, TEXTitem, honey_x
    global flower, bear1_x, bear2_x, bear3_x, bear4_x, dionaea1_x, dionaea2_x, dionaea3_x, dionaea4_x, flower_x
    #왼쪽부터 화면상에 그리기, 플레이어, 시간(프레임), 장애물

    honey_x = 290 #플레이어 x축 위치
    y = 640 #플레이어 y축 위치
    vel_y = 90 #점프값
    vel2_y = 90 #곰돌이 점프
    jump1 = False
    jump = False #점프 트루되면 점프됨

    what = False #필살기 실행 변수
    start = 0 #창 넘기는 변수
    
    oj = 0 #장애물 위치 설정할려고 만든 변수
    bigbee_x = 870
    bigbee_y = height

    flower_x = 1000

    ms1_x = 1230 #독침
    ms1_y = 450
    ms2_x = 1230
    ms2_y = 720
    ms3_x = width
    ms3_y = 100

    bear1_x = width #곰탱이1 x
    bear2_x = width
    bear3_x = width
    bear4_x = width
    bear_y = 600

    dionaea1_x = width - 300 #파리지옥 x, y 좌표
    dionaea2_x = width - 500
    dionaea3_x = -300  # 파리지옥 x, y 좌표
    dionaea4_x = width - 1000

    dionaea_y = 590
    flower1 = False
    flower2 = False
    flower3 = False
    flower4 = False

    Honeycomb_x = width - 610 #도착점
    Honeycomb_y = 200

    background1_x = 0 #배경1

    floor1_x = 0 #배경1
    floor2_x = background2_width #배경 오래가게 하는거

    cloud1_x = 200 #구름1
    cloud_y = -30   
    cloud2_x = background1_width #구름2
    cloud3_x = 800 #구름3

    #게임 종료 코드 True되면 꺼짐
    keyC = 0
    key1C = 0
    key2C = 0
    key3C = 0
    key4C = 0
    key5C = 0
    key6C = 0
    key7C = 0
    key8C = 0
    key10C = 0
    key11C = 0
    while keyC == 0 and key1C == 0 and key2C == 0 and key3C == 0 and key4C == 0 and key5C == 0 and key6C == 0 and key7C == 0 and key8C == 0 and key10C == 0 and key11C == 0:
        for event in pygame.event.get():...

        # if event.type == pygame.QUIT:
        #    keyC = 1

        ret, frame = capture.read()

        # 사진 조정 후 예측
        preprocessed = preprocessing(frame) 
        prediction = predict(preprocessed)

        userInput = pygame.key.get_pressed() #이게 키넣는 이벤트 넣게 해주는 그런 코드임

        if jump is False and (prediction[0,0] > 0.7): # 주먹으로 99프로 예측될 때 // 스페이스바 누르면 작동되는거 userInput[pygame.K_SPACE]
            jump = True #트루로 만들어서 아래 코드 작동

        if jump is True:
            y -= vel_y #y값에서 뺴야 올라감 젤 위는 0임
            vel_y -= 18 #다음 코드 작동할려고 뺴는거 13에서 12로 만듬
            if vel_y < -90:
                jump = False #점프가 거짓이 되어 멈춤
                vel_y = 90 #다시 원래 자리로 가버림

        pygame.time.delay(10)
        pygame.display.update() #실행될떄마다 계속 업데이트

        if userInput[pygame.K_1]: # 따봉으로 99프로 예측될 때 // 키보드 1을 누르면 이벤트 실행
            if start == 0:
                start = 1

        if userInput[pygame.K_5]:
            quit()
            

        floor1_x -= 64 #땅 속도
        floor2_x -= 64 

        cloud1_x -= 4 #구름 속도
        cloud2_x -= 4
        cloud3_x -= 4
        
        obstacle(background1, background1_x, 0) #위에 back에 넣는거

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

        #구름
        obstacle(cloud1, cloud1_x, cloud_y)
        obstacle(cloud2, cloud2_x, cloud_y + 40)
        obstacle(cloud3, cloud3_x, cloud_y)

        #워터마크
        obstacle(watermark, -55, -60)
        
        #땅
        obstacle(floor1, floor1_x, 80)
        obstacle(floor2, floor2_x, 80)

        #장애물 위치 지정 변수
        if keyC == 0 and start == 1:
            oj += 1
            
            #말벌 독침1 실행코드
            if oj >= 249 and oj < 258:
                rt1()
            elif oj >= 260:
                obstacle(ms1, ms1_x, ms1_y)
                ms1_x -= 120

            #말벌 독침2 실행코드
            if oj >= 238 and oj < 247:
                rt2()
            elif oj >= 249:
                obstacle(ms2, ms2_x, ms2_y)
                ms2_x -= 120

            #말벌 독침3 실행코드
            if oj >= 273 and oj < 287 and what == False:
                rt3()
                obstacle(flower, flower_x, 200)
                obstacle(TEXTitem, 100, 100)
                flower_x -= 80
            elif oj >= 290 and what == False:
                obstacle(ms3, ms3_x, ms3_y)
                ms3_x -= 120

            #곰돌이 실행코드
            if oj >= 1:
                if oj % 15 <= 4:
                    obstacle(bear1, bear1_x, bear_y) #곰도리1
                elif oj % 15 <= 9:
                    obstacle(bear2, bear1_x, bear_y)
                elif oj % 15 <= 14:
                    obstacle(bear3, bear1_x, bear_y)
                bear1_x -= 64

            if oj >= 55:
                if oj % 15 <= 4:
                    obstacle(bear4, bear2_x, bear_y) #곰도리2
                elif oj % 15 <= 9:
                    obstacle(bear5, bear2_x, bear_y)
                elif oj % 15 <= 14:
                    obstacle(bear6, bear2_x, bear_y)
                bear2_x -= 70

            if oj >= 112:
                if oj % 15 <= 4:
                    obstacle(bear7, bear3_x, bear_y) #곰도리3
                elif oj % 15 <= 9:
                    obstacle(bear8, bear3_x, bear_y)
                elif oj % 15 <= 14:
                    obstacle(bear9, bear3_x, bear_y)
                bear3_x -= 64

            if oj >= 185:
                if oj % 15 <= 4:
                    obstacle(bear10, bear4_x, bear_y) #곰도리4
                elif oj % 15 <= 9:
                    obstacle(bear11, bear4_x, bear_y)
                elif oj % 15 <= 14:
                    obstacle(bear12, bear4_x, bear_y)
                bear4_x -= 90
                if oj >= 185 and jump1 == False:
                    bear_y -= vel2_y #y값에서 뺴야 올라감 젤 위는 0임
                    vel2_y -= 18 #다음 코드 작동할려고 뺴는거 13에서 12로 만듬
                    if vel2_y < -90:
                        jump1 = True
                        vel2_y = 90

            
            #파리지옥 실행코드1
            if oj >= 30:
                if oj % 20 <= 6 and flower1 == False:
                    obstacle(dionaea1, dionaea1_x, dionaea_y) #파리지옥1
                elif oj % 20 <= 7 and flower1 == False:
                    obstacle(dionaea2, dionaea1_x, dionaea_y)
                elif oj % 20 <= 11 and flower1 == False:
                    obstacle(dionaea3, dionaea1_x, dionaea_y) 
                elif oj % 20 <= 15 and flower1 == False:
                    obstacle(dionaea4, dionaea1_x, dionaea_y)
                    flower1 = True
                elif oj % 20 <= 19 and flower1 == True:
                    obstacle(dionaea5, dionaea1_x, dionaea_y)
                dionaea1_x -= 64

            if oj >= 80:
                if oj % 20 <= 3 and flower2 == False:
                    obstacle(dionaea6, dionaea2_x, dionaea_y) #파리지옥2
                elif oj % 20 <= 7 and flower2 == False:
                    obstacle(dionaea7, dionaea2_x, dionaea_y)
                elif oj % 20 <= 11 and flower2 == False:
                    obstacle(dionaea8, dionaea2_x, dionaea_y) 
                elif oj % 20 <= 15 and flower2 == False:
                    obstacle(dionaea9, dionaea2_x, dionaea_y)
                    flower2 = True
                elif oj % 20 <= 19 and flower2 == True:
                    obstacle(dionaea10, dionaea2_x, dionaea_y)
                if oj >= 95:
                    dionaea2_x -= 80

            if oj >= 142 and oj < 178:
                if oj % 20 <= 3 and flower3 == False:
                    obstacle(dionaea11, dionaea3_x, dionaea_y) #파리지옥3
                elif oj % 20 <= 7 and flower3 == False:
                    obstacle(dionaea12, dionaea3_x, dionaea_y)
                elif oj % 20 <= 11 and flower3 == False:
                    obstacle(dionaea13, dionaea3_x, dionaea_y)
                elif oj % 20 <= 15 and flower3 == False:
                    obstacle(dionaea14, dionaea3_x, dionaea_y)
                    flower3 = True
                elif oj % 20 <= 19 and flower3 == True:
                    obstacle(dionaea15, dionaea3_x, dionaea_y)
                if oj >= 160:
                    dionaea3_x += 64

            if oj >= 142:
                if oj % 20 <= 3 and flower4 == False:
                    obstacle(dionaea16, dionaea4_x, dionaea_y) #파리지옥4
                elif oj % 20 <= 7 and flower4 == False:
                    obstacle(dionaea17, dionaea4_x, dionaea_y)
                elif oj % 20 <= 11 and flower4 == False:
                    obstacle(dionaea18, dionaea4_x, dionaea_y)
                elif oj % 20 <= 15 and flower4 == False:
                    obstacle(dionaea19, dionaea4_x, dionaea_y)
                    flower4 = True
                elif oj % 20 <= 19 and flower4 == True:
                    obstacle(dionaea20, dionaea4_x, dionaea_y)
                if oj >= 160:
                    dionaea4_x -= 64

            #말벌 장애물 실행 코드
            if oj >= 200:
                if oj % 13 == 0:
                    obstacle(bigbee1, bigbee_x, bigbee_y) #말벌 애니메이션
                elif oj % 13 == 1:
                    obstacle(bigbee2, bigbee_x, bigbee_y)
                elif oj % 13 == 2:
                    obstacle(bigbee3, bigbee_x, bigbee_y)
                elif oj % 13 == 3:
                    obstacle(bigbee4, bigbee_x, bigbee_y)
                elif oj % 13 == 4:
                    obstacle(bigbee5, bigbee_x, bigbee_y)
                elif oj % 13 == 5:
                    obstacle(bigbee6, bigbee_x, bigbee_y)
                elif oj % 13 == 6:
                    obstacle(bigbee7, bigbee_x, bigbee_y)
                elif oj % 13 == 7:
                    obstacle(bigbee8, bigbee_x, bigbee_y)
                elif oj % 13 == 8:
                    obstacle(bigbee9, bigbee_x, bigbee_y)
                elif oj % 13 == 9:
                    obstacle(bigbee10, bigbee_x, bigbee_y)
                elif oj % 13 == 10:
                    obstacle(bigbee11, bigbee_x, bigbee_y)
                elif oj % 13 == 11:
                    obstacle(bigbee12, bigbee_x, bigbee_y)
                elif oj % 13 == 12:
                    obstacle(bigbee13, bigbee_x, bigbee_y)
                bigbee_y -= 40
                if bigbee_y <= -150:
                    bigbee_y = -150
                if oj >= 300:
                    bigbee_x -= 50

            if bigbee_x < 0:
                obstacle(Honeycomb, Honeycomb_x, Honeycomb_y)
                honey_x += 40

            if oj % 2 == 0:
                obstacle(beecraft1, honey_x, y) #플레이어 애니메이션
            elif oj % 2 == 1:
                obstacle(beecraft2, honey_x, y)

        if start == 0:
            Startscreen()

        #죽는 화면
        health()

        #충돌
        keyC = crash0(beecraft1 or beecraft2, ms1)
        key1C = crash1(beecraft1 or beecraft2, ms2)
        key2C = crash2(beecraft1 or beecraft2, bear1 or bear2 or bear3)
        key3C = crash3(beecraft1 or beecraft2, dionaea1 or dionaea2 or dionaea3 or dionaea4 or dionaea5)
        key4C = crash4(beecraft1 or beecraft2, bear4 or bear5 or bear6)
        key5C = crash5(beecraft1 or beecraft2, dionaea6 or dionaea7 or dionaea8 or dionaea9 or dionaea10)
        key6C = crash6(beecraft1 or beecraft2, bear7 or bear8 or bear9)
        key7C = crash7(beecraft1 or beecraft2, dionaea11 or dionaea12 or dionaea13 or dionaea14 or dionaea15)
        key8C = crash8(beecraft1 or beecraft2, bear10 or bear11 or bear12)
        crash9(beecraft1 or beecraft2, flower)
        key10C = crash10(beecraft1 or beecraft2, ms3)
        key11C = crash11(beecraft1 or beecraft2, Honeycomb)
        
        if keyC == 2:
            runGame()
        elif key1C == 2:
            runGame()
        elif key2C == 2:
            runGame()
        elif key3C == 2:
            runGame()
        elif key4C == 2:
            runGame()
        elif key5C == 2:
            runGame()
        elif key6C == 2:
            runGame()
        elif key7C == 2:
            runGame()
        elif key8C == 2:
            runGame()
        elif key10C == 2:
            runGame()
        elif key11C == 2:
            runGame()
        
        pygame.display.update() #화면 업데이트
        clock.tick(60) #프레임

    pygame.quit()
    quit() #화면 닫으면 나가지는 코드

#게임 초기화 코드
def initGame():
    global clock, background1, ms1, floor1, floor2, cloud1, cloud2, cloud3, watermark, beecraft1, beecraft2, hp1, hp2, hp3, flower
    global bigbee1, bigbee2, bigbee3, bigbee4, bigbee5, bigbee6, bigbee7, bigbee8, bigbee9, ms2, bear1, bear2, bear3, dionaea1, dionaea2, dionaea3, dionaea4, dionaea5, TEXTitem
    global diebear, diedionaea, diebigbee, startscreen, bigbee10, bigbee11, bigbee12, bigbee13, bear4, bear5, bear6, bear7, bear8, bear9, bear10, bear11, bear12, ms3, Honeycomb
    global dionaea6, dionaea7, dionaea8, dionaea9, dionaea10, dionaea11, dionaea12, dionaea13, dionaea14, dionaea15, dionaea16, dionaea17, dionaea18, dionaea19, dionaea20, clear

    pygame.init()
    pygame.display.set_caption('야꿀벌') #타이틀 제목
    r = 'C:/Users/User/Desktop/29/부스/' #주소
    b = 200 #꿀벌
    beecraft1 = pygame.image.load(r+'honeybee1.png').convert_alpha() #캐릭터 이미지
    beecraft1 = pygame.transform.scale(beecraft1, (b, b)) #이미지 크기 바꿈
    beecraft2 = pygame.image.load(r+'honeybee2.png').convert_alpha() #캐릭터 이미지
    beecraft2 = pygame.transform.scale(beecraft2, (b, b)) #이미지 크기 바꿈
    bigbee1 = pygame.image.load(r+'말벌1.png').convert_alpha() #말벌 이미지
    bigbee1 = pygame.transform.scale(bigbee1, (1400, 1400))
    bigbee2 = pygame.image.load(r+'말벌2.png').convert_alpha()
    bigbee2 = pygame.transform.scale(bigbee2, (1400, 1400))
    bigbee3 = pygame.image.load(r+'말벌3.png').convert_alpha()
    bigbee3 = pygame.transform.scale(bigbee3, (1400, 1400))
    bigbee4 = pygame.image.load(r+'말벌4.png').convert_alpha()
    bigbee4 = pygame.transform.scale(bigbee4, (1400, 1400))
    bigbee5 = pygame.image.load(r+'말벌5.png').convert_alpha()
    bigbee5 = pygame.transform.scale(bigbee5, (1400, 1400))
    bigbee6 = pygame.image.load(r+'말벌6.png').convert_alpha()
    bigbee6 = pygame.transform.scale(bigbee6, (1400, 1400))
    bigbee7 = pygame.image.load(r+'말벌7.png').convert_alpha()
    bigbee7 = pygame.transform.scale(bigbee7, (1400, 1400))
    bigbee8 = pygame.image.load(r+'말벌8.png').convert_alpha()
    bigbee8 = pygame.transform.scale(bigbee8, (1400, 1400))
    bigbee9 = pygame.image.load(r+'말벌9.png').convert_alpha()
    bigbee9 = pygame.transform.scale(bigbee9, (1400, 1400))
    bigbee10 = pygame.image.load(r+'말벌20.png').convert_alpha()
    bigbee10 = pygame.transform.scale(bigbee10, (1400, 1400))
    bigbee11 = pygame.image.load(r+'말벌21.png').convert_alpha()
    bigbee11 = pygame.transform.scale(bigbee11, (1400, 1400))
    bigbee12 = pygame.image.load(r+'말벌22.png').convert_alpha()
    bigbee12 = pygame.transform.scale(bigbee12, (1400, 1400))
    bigbee13 = pygame.image.load(r+'말벌23.png').convert_alpha()
    bigbee13 = pygame.transform.scale(bigbee13, (1400, 1400))
    floor1 = pygame.image.load(r+'floor.png') #땅 이미지
    floor1 = pygame.transform.scale(floor1, (1920, 1000))
    floor2 = floor1.copy()
    background1 = pygame.image.load(r+'background.png') #게임배경 이미지
    background1 = pygame.transform.scale(background1, (1920, 1080))
    c = 100 #독침
    ms1 = pygame.image.load(r+'ms.png') #말벌 독침 이미지
    ms1 = pygame.transform.scale(ms1, (c, c))
    ms2 = ms1.copy() 
    ms3 = pygame.image.load(r+'ms1.png') #말벌 독침 이미지
    ms3 = pygame.transform.scale(ms3, (1000, 1000))
    cloud1 = pygame.image.load(r+'cloud1.png') #구름 이미지
    cloud1 = pygame.transform.scale(cloud1, (1400, 800))
    cloud2 = pygame.image.load(r+'cloud2.png') #구름 이미지
    cloud2 = pygame.transform.scale(cloud2, (1400, 700))
    cloud3 = pygame.image.load(r+'cloud3.png') #구름 이미지
    cloud3 = pygame.transform.scale(cloud3, (1400, 800))
    watermark = pygame.image.load(r+'watermark.png') #워터마크 이미지
    watermark = pygame.transform.scale(watermark, (2200, 1500))
    a = 250 #곰돌이 크기
    bear1 = pygame.image.load(r+'bear1.png') #곰 이미지
    bear1 = pygame.transform.scale(bear1, (a, a))
    bear2 = pygame.image.load(r+'bear2.png')
    bear2 = pygame.transform.scale(bear2, (a, a))
    bear3 = pygame.image.load(r+'bear3.png')
    bear3 = pygame.transform.scale(bear3, (a, a))
    bear4 = bear1.copy()
    bear5 = bear2.copy()
    bear6 = bear3.copy()
    bear7 = bear1.copy()
    bear8 = bear2.copy()
    bear9 = bear3.copy()
    bear10 = bear1.copy()
    bear11 = bear2.copy()
    bear12 = bear3.copy()
    d = 280 #파리지옥 y좌표
    e = 180 #파리지옥 x좌표
    dionaea1 = pygame.image.load(r+'Dionaea1.png') #파리지옥 이미지
    dionaea1 = pygame.transform.scale(dionaea1, (e, d))
    dionaea2 = pygame.image.load(r+'Dionaea2.png')
    dionaea2 = pygame.transform.scale(dionaea2, (e, d))
    dionaea3 = pygame.image.load(r+'Dionaea3.png')
    dionaea3 = pygame.transform.scale(dionaea3, (e, d))
    dionaea4 = pygame.image.load(r+'Dionaea4.png')
    dionaea4 = pygame.transform.scale(dionaea4, (e, d))
    dionaea5 = pygame.image.load(r+'Dionaea5.png')
    dionaea5 = pygame.transform.scale(dionaea5, (e, d))
    dionaea6 = dionaea1.copy()
    dionaea7 = dionaea2.copy()
    dionaea8 = dionaea3.copy()
    dionaea9 = dionaea4.copy()
    dionaea10 = dionaea5.copy()
    dionaea11 = dionaea1.copy()
    dionaea12 = dionaea2.copy()
    dionaea13 = dionaea3.copy()
    dionaea14 = dionaea4.copy()
    dionaea15 = dionaea5.copy()
    dionaea16 = dionaea1.copy()
    dionaea17 = dionaea2.copy()
    dionaea18 = dionaea3.copy()
    dionaea19 = dionaea4.copy()
    dionaea20 = dionaea5.copy()
    f = 900 #HP
    hp1 = pygame.image.load(r+'hp1.png') #HP 이미지(1이 목숨 한개뿐인거)
    hp1 = pygame.transform.scale(hp1, (f, f))
    hp2 = pygame.image.load(r+'hp2.png')
    hp2 = pygame.transform.scale(hp2, (f, f))
    hp3 = pygame.image.load(r+'hp3.png')
    hp3 = pygame.transform.scale(hp3, (f, f))
    diebear = pygame.image.load(r+'death message bear1.png')
    diedear = pygame.transform.scale(diebear, (1920, 1080))
    diedionaea = pygame.image.load(r+'death message Dionaea1.png')
    diedionaea = pygame.transform.scale(diedionaea, (1920, 1080))
    diebigbee = pygame.image.load(r+'death message wasp1.png')
    diebigbee = pygame.transform.scale(diebigbee, (1920, 1080))
    startscreen = pygame.image.load(r+'start screen.png')
    startscreen = pygame.transform.scale(startscreen, (1920, 1080)) #시작화면
    hc = 800
    Honeycomb = pygame.image.load(r+'Honeycomb.png')
    Honeycomb = pygame.transform.scale(Honeycomb, (hc, hc))
    flower = pygame.image.load(r+'flower.png')
    flower = pygame.transform.scale(flower, (200, 400))
    TEXTitem = pygame.image.load(r+'TEXTitem.png')
    TEXTitem = pygame.transform.scale(TEXTitem, (1200, 400))
    clear = pygame.image.load(r+'clear.png')
    clear = pygame.transform.scale(clear, (1920, 1080))

    clock = pygame.time.Clock() #다시 키면 다시 재생되게 할려고 초기화 코드넣는거

    runGame()

if __name__ == '__main__':
    initGame() #초기화 시킴  