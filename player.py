import pygame
import random
import math
from pygame.locals import *
import pygame_gui

class player:
    """
    Lớp đại diện cho player (cầu thủ / thủ môn  ) .

    Thuộc tính:
    - x,y: Vị trí của người chơi 
    - color : màu quả người chơi 
    - window : bề mặt vẽ lên 
    """
    def __init__(self,x,y,color,window):
        """
        Khởi tạo một đối tượng Player mới.

        Đối số:
        - x (int): Vị trí x của người chơi.
        - y (int): Vị trí y của người chơi.
        - color (tuple): Màu sắc của người chơi.
        - name (string) : tên người 
        - window (pygame.Surface): Bề mặt để vẽ lên.
        """
        self.x=x
        self.y=y
        self.color=color
        self.score=0
        self.name=""
        self.window=window

    def draw(self):
        """
            phương thức vẽ player 
        """
        pass
    def sad(self):

        pass
    def vui(self):
        """
            phương thức ăn mừng khi chiến thắng     
        """
        pass
