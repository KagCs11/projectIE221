import pygame
import random
import math
from pygame.locals import *
import pygame_gui

class gon:
    """
    Lớp đại diện cho khung thành .

    Thuộc tính:
    - x,y: Vị trí của trên cùng bên trái của khung thành  
    - w (int): Chiều rộng của khung thàn
    - h (int): Chiều cao ccủa khung thàn
    - window : bề mặt vẽ lên 
  """
    def __init__(self,x,y,w,h,window):
        self.h=h
        self.w=w
        self.x=x
        self.y=y 
        self.window=window

    def draw_goal(self):

        """
            phương thức vẽ khung thành 
        """
        image_san = pygame.image.load("san4.jpg")
        image_san=pygame.transform.scale(image_san, (self.window.get_width(),self.window.get_height()))
        self.window.blit(image_san, (0, 0))

        WHITE = (255, 255, 255)
        pygame.draw.rect(self.window, WHITE, (self.x, self.y, self.w, self.h), 2)

        image = pygame.image.load("gon.png")
        image=pygame.transform.scale(image, (self.w,self.h))
        self.window.blit(image, (self.x, self.y))



    def cham_ball(self,ball):
        """ phương thức chạm vào quả bóng 
            đối số : quả bóng 
            mục đích : thay đổi tọa độ quả bóng 
        """
        # chạm cột bên trái 
        if(check_collision((self.x,self.y),(self.x,self.y +h),ball.x+ball.size/2,ball.y+ball.size/2)==True):
            ball.x-=5
        elif(check_collision((self.x+w,self.y),(self.x+w,self.y +h),ball.x+ball.size/2,ball.y+ball.size/2)==True):
            ball.x+=5
