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

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.1)
    
def run_top():
    print('top')
    for x in range (20, 780, 10):
        draw_boy(x, 550)
    pass

def run_right():
    print('right')
    for y in range (550, 50, -10):
        draw_boy(780, y)
    pass

def run_bottom():
    print('bottom')
    for x in range (780, 20, -10):
        draw_boy(x, 50)
    pass

def run_left():
    print('left')
    for y in range (50, 550, 10):
        draw_boy(20, y)
    pass

def run_down():
    print('down')
    pass

def run_up():
    print('up')
    pass

def run_bottomT():
    print('bottomT')
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
        draw_boy(x, y)
    pass

def run_triangle():
    print('TRIANGLE')
    run_down()
    run_bottomT()
    run_up()
    pass

while True:
    #run_circle()
    #run_rectangle()
    run_triangle()
    break

#탑다운 설계(하향식 설계)
#고수: 함수 호출 -> 함수 정의
#하수: 함수 정의 -> 함수 호출

close_canvas()
