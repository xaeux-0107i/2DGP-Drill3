from pico2d import *
import math

#실행 가능한 큰 뻐대를 먼저 만든다.
#실행가능하다면 커밋한다.
#무한 루프 맞는지 확인한다.
#실행 된다면 커밋한다.

open_canvas()

# fill here
grass = load_image('grass.png')
boy = load_image('character.png')

def run_top():
    print('top')
    pass
def run_right():
    print('right')
    pass
def run_bottom():
    print('bottom')
    pass
def run_left():
    print('left')
    pass

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_circle():
    print('CIRCLE')
    
    r, cx, cy = 300, 800//2, 600//2
    
    for d in range (0, 360): # 0부터 359까지
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy
        
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.1)
        
    pass

while True:
    #run_circle()
    run_rectangle()
    break

#탑다운 설계(하향식 설계)
#고수: 함수 호출 -> 함수 정의
#하수: 함수 정의 -> 함수 호출

close_canvas()
