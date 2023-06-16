import pygame
import random
import math
from pygame.locals import *
import pygame_gui
from player import player

donhay=5
class cauthu(player):
    """
    Lớp đại diện cho cầu thủ.

    Thuộc tính:
    - x (int): Vị trí x của cầu thủ.
    - y (int): Vị trí y của cầu thủ.
    - color (tuple): Màu sắc của cầu thủ.
    - window : Bề mặt để vẽ lên.
    - luc (int): Lực sút của cầu thủ.
    - image_action (list): Danh sách các hình ảnh thể hiện hành động của cầu thủ.
    - i_action (int): Chỉ số hình ảnh hiện tại trong danh sách hành động.
    - tg_sut (int): Thời gian chờ giữa các lần sút của cầu thủ.
    """
    def __init__(self,x,y,color,window,luc):
        super().__init__(x,y,color,window)
        self.luc=luc
        self.image_action=[]
        self.image_action.append(pygame.image.load("messi.png"))
        self.image_action.append(pygame.image.load("m10_sut.png"))
        self.image_action.append(pygame.image.load("ms_vui.png"))
        self.image_action.append(pygame.image.load("ms_vui2.png"))
        self.image_action.append(pygame.image.load("ms_sad.png"))

        self.i_action=0
        self.tg_sut=1
        self.x_target=500
        self.y_target=100


    def draw(self):
        """
        Vẽ cầu thủ lên bề mặt window.
        """
        ms_size = (100,200)
        ms_image=self.image_action[self.i_action]
        ms_image=pygame.transform.scale(ms_image, (200,200))
        self.window.blit(ms_image, (700,400))
        #pygame.draw.circle(self.window, self.color, (self.x,self.y),self.size)

    def sut(self,ball,x_target,y_target,gon,gk):
        """
        Phương thức thực hiện hành động sút của cầu thủ.

        Đối số:
        - ball (Ball): Đối tượng quả bóng.
        - x_target (int): Vị trí x mục tiêu của quả bóng.
        - y_target (int): Vị trí y mục tiêu của quả bóng.
        - gon (Gon): Đối tượng cổ động viên.
        - gk (ThủMon): Đối tượng thủ môn.
        """
        if(self.tg_sut==1):
            self.i_action=1
        self.tg_sut-=1
        if(self.tg_sut<=0):
            d=math.sqrt((ball.x -x_target )**2 + (ball.y - y_target)**2)
            if(x_target<=(self.window.get_width())/2 and ball.x<=x_target and ball.y<=y_target):
                dx=0 
                dy=0
            elif(x_target>=(self.window.get_width())/2 and ball.x>=x_target and ball.y<=y_target):
                dx=0
                dy=0
            else:
                dx=(x_target-ball.x)/(d)
                dy=(y_target-ball.y)/(d)
            ball.bay((dx*self.luc),(dy*self.luc),self.luc,gk)
    def vui(self):
        """
        Phương thức thể hiện cầu thủ vui mừng.
        """
        global donhay
        if(donhay==0):
            self.i_action=random.choice([2,3])
            donhay=5
        else:
            donhay-=1

    def sad(self):
        global donhay
        if(donhay==0):
            self.i_action=random.choice([4])
            donhay=5
        else:
            donhay-=1

    def nham(self):
        center = (self.x_target,self.y_target)
        radius = 50
        pygame.draw.circle(self.window,(255,0,0), center, radius)