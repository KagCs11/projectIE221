import pygame
import random
import math
from pygame.locals import *
import pygame_gui

class ball:
    """
    Lớp đại diện cho quả bóng .

    Thuộc tính:
    - x,y: Vị trí của quả bóng 
    - size : size quả bóng 
    - color : màu quả bóng 
    - window : bề mặt vẽ lên 
    - state_ball : trạng thái hiện tại của quả bóng 
    """
    def __init__(self,x,y,size,color,window):
        self.x=x
        self.y=y
        self.size=size
        self.window=window
        self.color=color
        self.state_ball="im"

    def draw_ball(self):
        """
        phương thức vẽ quả bóng 
        """
        ball_size = (self.size,self.size)
        ball_image = pygame.image.load("ball.PNG")
        ball_image=pygame.transform.scale(ball_image, (self.size,self.size))
        self.window.blit(ball_image, (self.x,self.y))

    def bay(self,dx,dy,luc,gk):
        """
        phương thức quả bóng bay 
        đối số : dx,dy : khoảng di chuyển của quả bóng theo tậm x,y
        luc : lực làm cho quả bóng bay 
        mục đích : Thay đổi tọa độ của quả bóng khi nó bay.
        """
        if(self.state_ball=="vang"):
            self.vang(gk)
        else:
            self.size-=luc/10
            self.x+=dx
            self.y+=dy
    def vang(self,gk):
        """
        phương thức quả bóng bị văng bởi thủ môn 
        đối số : thủ môn 
        --> mục đích : thay đổi tọa độ quả bóng khi nó bị văng bởi thủ môn 
        """
        self.state_ball="vang"
        self.size-=0.1
        if(self.x<gk.x2body):
            self.x-=10
        else:
            self.x+=10