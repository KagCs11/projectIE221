import pygame
import random
import math
from pygame.locals import *
import pygame_gui

from nut import TextBox
from nut import Button
from gon import gon
from ball import ball
from gk import gk
from cauthu import cauthu
from BLV import BLV
#
######################################################################def#########################################################################


def kq(ball,ter,messi,gon):
    """
    Kiểm tra kết quả sau khi quả bóng ball di chuyển 1 khaonrg cách hợp lý có thể kiểm tra kết quả và tính điêm 
    đối số :
        ball (object): Đối tượng ball (quả bóng).
        ter (object): Đối tượng ter (thủ môn).
        messi (object): Đối tượng messi.
        gon (object): Đối tượng gon (khung thành).

    Returns:
        int: Kết quả:
            - 99 nếu quả bóng ra khỏi khung thành. ( +1 điểm cho thủ môn)
            - 10 nếu quả bóng đến điểm trong khung thành 
            - 0 nếu chưa có kết quả.( trái banh chưa đến đích )
    """
    if(ball.size<=30 or ball.x<0 or ball.x>1400): # trái banh xa
        if(ball.x>=g.x + g.w or ball.x < g.x or ball.y < g.y):
            ter.score+=1
            return 99
        else:
            messi.score+=1
            return 10
    else:
        return 0

def draw_o(cauthu,ball,gon,ter,window,bt_is_cauthu,bt_is_gk,bt_score_gk,bt_score_ms,bt_restart,box_name_gk,box_name_messi):
    """
    Vẽ các đối tượng cauthu, ball, khùng thành (gon), thủ môn ( ter) lên cửa sổ window và cập nhật các nút và hộp văn bản.

    Args:
        cauthu (object): Đối tượng cauthu.
        ball (object): Đối tượng ball (quả bóng).
        gon (object): Đối tượng gon (khung thành).
        ter (object): Đối tượng ter (thủ môn).
        window (Surface): Cửa sổ pygame.
        bt_is_cauthu (Button): Nút chọn là cầu thủ.
        bt_is_gk (Button): Nút chọn là thủ môn.
        bt_score_gk (Button): Nút hiển thị điểm của thủ môn.
        bt_score_ms (Button): Nút hiển thị điểm của cầu thủ.
        bt_restart (Button): Nút khởi động lại trò chơi.
        textbox (Textbox): Hộp tên

    Returns:
        None
    """
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    global is_player

    window.fill(BLACK)
    gon.draw_goal()


    if(ball.size<35):
        ball.draw_ball()
        ter.draw()
    else:
        ter.draw()
        ball.draw_ball()
    cauthu.draw()
    
    bt_is_cauthu.draw(window)
    bt_is_gk.draw(window)
    bt_score_gk.text="Score Goalkeeper :"+ str(ter.score)
    bt_score_ms.text="Score player :"+ str(cauthu.score)
    bt_score_gk.draw(window)
    bt_score_ms.draw(window)
    bt_restart.draw(window)
    bt_next.draw(window)
    box_name_gk.update(window)
    box_name_gk.rect = pygame.Rect(ter.x-100, ter.y-(ter.sizedau*3), 200, 40)

    #window.blit(image, (0, WINDOW_HEIGHT /2))
    #box_name_messi.update(window)
    #box_name_messi.rect = pygame.Rect(messi.x,messi.y, 200, 40)

def re_cauthu(messi):
    """
    hàm quay lại hành động cho cầu thủ ( khởi tạo lại)
    """
    messi.i_action=0
    messi.tg_sut=1

def re_ball(ball):
    """
    hàm khởi tạo lại quả bóng về ban đầu 
    """
    global xball
    global yball
    global ball_size
    ball.x=xball
    ball.y=yball
    ball.size=ball_size
    ball.state_ball="im"

def re_gk(gk):
    """
    hàm khởi tạo lại thủ môn về ban đầu 
    """
    global x_gk
    global y_gk
    global phanxa
    global tocdobay
    gk.x=x_gk
    gk.y=y_gk
    gk.phanxa=phanxa 
    gk.tocdobay=tocdobay
    gk.state_bay="len"
    gk.state_cham="chua"
    gk.i_icon=0

def again(cauthu,gk,ball):
    """
    hàm bấm phím chơi lại cho nút again
    """
    re_gk(gk)
    re_ball(ball)
    re_cauthu(cauthu)
    gk.score=0
    cauthu.score=0
    bt_is_cauthu.visible=True
    bt_is_gk.visible = True


############################################################################ khởi tạo biến ########################################################
pygame.init()

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 600
window_size=(WINDOW_WIDTH, WINDOW_HEIGHT)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Penalty Kick Game")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

bt_is_cauthu = Button(500, 325, 400, 50, "Soccer player", (0,191,255), (0, 0, 0))
bt_is_gk = Button(500,275, 400, 50, "Goalkeeper ", (255,0,0), (0, 0, 0))
bt_score_gk=Button(0,0, 250, 100, "Score Goalkeeper :" + str(0), (255, 255,0), (0, 0, 0))
bt_score_ms=Button(1150,0, 250, 100, "Score player  :" +str(0), (255, 255,0), (0, 0, 0))
bt_restart = Button(0, 550, 400, 50, "Play again", (255,165, 0), (0, 0, 0))
bt_next = Button(WINDOW_WIDTH-400, 550, 400, 50, "NEXT", (255,165, 0), (0, 0, 0))

#BLV
blv=BLV()

# BALLLL
ball_size=130
xball=WINDOW_WIDTH//2-(ball_size/2)
yball=WINDOW_HEIGHT//2+150
ball=ball(xball,yball,ball_size,WHITE,window)

#GONNNNNN
gon_h = 300 # chiều cao gôn
gon_w =WINDOW_WIDTH*0.6 # chiều rộng gôn 
x_gon=(WINDOW_WIDTH-gon_w)/2
y_gon=25
g=gon(x_gon,y_gon,gon_w,gon_h,window)

#MESSIIIIIIIIIII
messi=cauthu(WINDOW_WIDTH//2,WINDOW_HEIGHT//2,WHITE,window,luc=8)

#GKKKKKKKKKKKKKKKK
x_gk=x_gon+(gon_w/2)
y_gk=gon_h/2
phanxa=10
tocdobay=5
ter=gk(x_gk,y_gk,WHITE,window,20,70,25,phanxa=phanxa,tocdobay=tocdobay) 

box_name_gk = TextBox((ter.x-100,ter.y-(ter.sizedau*3)),200,40)
box_name_messi = TextBox((messi.x,messi.y),200,40)

is_player="NO"
action="NO"
action_ms="NO"

x_t=0
y_t=0
################################################################## running #################################################################
running=True
while running:
    draw_o(messi,ball,g,ter,window,bt_is_cauthu,bt_is_gk,bt_score_gk,bt_score_ms,bt_restart,box_name_gk,box_name_messi)
    pygame.mixer.Sound('san.wav').play()
    for event in pygame.event.get():
        # xử lý nhập tên player 
        box_name_gk.handle_event(event)
        ter.name=box_name_gk.text
        box_name_messi.handle_event(event)
        messi.name=box_name_messi.text

        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # xử lý nhấn phím "next" để chơi tiếp 
            if bt_next.visible and bt_next.is_clicked(pygame.mouse.get_pos()): 
                action="NO"
                action_ms="NO"
                re_ball(ball)
                re_gk(ter)
                re_cauthu(messi)
                messi.tg_sut=1
                blv.stop()

            #xử lý chọn 1 trong 2 player (messi / GK)
            if bt_is_cauthu.visible and bt_is_cauthu.is_clicked(pygame.mouse.get_pos()):
                print("chon messi")
                is_player="messi"
                bt_is_cauthu.visible=False
                bt_is_gk.visible = False 
            elif bt_is_gk.visible and bt_is_gk.is_clicked(pygame.mouse.get_pos()):
                print("chon thu mon")
                is_player="GK"
                bt_is_gk.visible = False 
                bt_is_cauthu.visible = False
            elif bt_restart.visible and bt_restart.is_clicked(pygame.mouse.get_pos()):
                again(messi,ter,ball)
                action="NO"
                action_ms="NO"
                messi.tg_sut=1
                blv.stop()

        # xử lý nhấn phím khi chọn đối tượng " messi "
        elif event.type== KEYDOWN and is_player=="messi":
            if(event.key == K_LEFT): # khi muốn sút bên trái 
                messi.x_target-=25
            elif(event.key == K_RIGHT): # khi muốn sút bên phải 
                messi.x_target+=25
            if(event.key == K_UP): # khi muốn sút bên trái 
                messi.y_target-=25
            elif(event.key == K_DOWN): # khi muốn sút bên phải 
                messi.y_target+=25
            elif(event.key==K_SPACE and action=="NO"):
                x_t=random.randint(messi.x_target-25,messi.x_target+25)
                y_t=random.randint(messi.y_target-25,messi.y_target+25)
                huong_bay= random.choice(["trai","phai"])
                xa=ter.x+gon_w/2
                action="sut"


        # xử lý nhấn phím khi chọn đối tượng " GK "
        elif event.type== KEYDOWN and is_player=="GK":
            if(event.key == K_LEFT and action=="NO"):
                ter.di("trai",10)
            elif(event.key == K_RIGHT and action =="NO"):
                ter.di("phai",10)
            elif(event.key==K_a and action=="NO"):
                xa=ter.x+gon_w/2
                huong_bay="trai"
                action="bay"
            elif(event.key==K_d and action =="NO"):
                xa=ter.x+gon_w/2
                huong_bay="phai"
                action="bay"


    if(action=="gk_vui"):# khi GK win 
        ter.canh_nhay(ball,g)
        ter.vui()
        messi.sad()
        blv.kovao()
    elif(action=="messi_vui"): #khi messi win
        #ter.canh(ball,g)
        ter.canh(ball,g)
        messi.vui()
        ter.sad()
        blv.vao()
    elif(is_player=="NO" or action=="NO"): #khi bắt đầu chưa có hành động nào 
        #ter.canh(ball,g)
        ter.canh_nhay(ball,g)

    if(is_player=="messi" and action=="sut"):  #khi đối tượng được chọn là messi và bắt đầu nhấn phím sút 
        if(ball.x==xball):
            blv.coi()
        messi.sut(ball,x_t,y_t,g,ter)
        ter.bay(huong_bay,xa,g,ball)

    elif(is_player=="messi"):
        messi.nham()
    elif(is_player=="GK" and action=="bay"): #khi đối tượng được chọn là GK và bắt đầu nhấn phím "A" để bay sang trái hoặc "D" để bay sang phải 
        ter.bay(huong_bay,xa,g,ball)

    if(is_player=="GK"): # khi chọn đối tượng muốn chơi là GK
        if(action_ms=="sut" and action!="gk_vui" and action!="messi_vui"):
            messi.sut(ball,x_t,y_t,g,ter)
        elif(messi.tg_sut==1): # bắt đầu chọn hướng sút và sút ( action_ms="sut")
            x_t=random.randint(x_gon,WINDOW_WIDTH)
            y_t=random.randint(1,gon_h/2)
            messi.tg_sut=random.randint(2,100) # thơi gian chuẩn bị sút 
            action_ms="sut"

    KQ=kq(ball,ter,messi,g) # kiểm tra kết quả 
    if(KQ!=0): 
        re_ball(ball)
        re_gk(ter)
        re_cauthu(messi)
        action="NO"
        action_ms="NO"
        if(KQ==10):
            action="messi_vui"
        elif(KQ==99):
            ter.canh(ball,g)
            action="gk_vui"

    pygame.display.update()
    clock.tick(9999999999999999999999999999999999999999999999)

pygame.quit()

