import pygame
import random
import math
from pygame.locals import *
import pygame_gui

class TextBox:
    """
    Lớp đại diện cho một TextBox.

    Thuộc tính:
    - pos (tuple): Vị trí của hộp văn bản (x, y).
    - width (int): Chiều rộng của hộp văn bản.
    - height (int): Chiều cao của hộp văn bản.
    - font_size (int): Cỡ chữ của văn bản (mặc định: 32).
    - rect : Hình chữ nhật đại diện cho hộp văn bản.
    - font : Font được sử dụng để hiển thị văn bản.
    - text (str): Văn bản hiện tại trong hộp văn bản.
    - active (bool): Xác định liệu TextBox có được chọn hay không.
    - visible (bool): Xác định liệu TextBox có hiển thị hay không.
    - tb_color (str): Màu của TextBox.
    - color_active : Màu của TextBox khi được chọn.
    - color_inactive : Màu của TextBox khi không được chọn.
    """
    def __init__(self, pos, width, height ,font_size=32):
        self.rect = pygame.Rect(pos[0], pos[1], width, height)
        self.font = pygame.font.Font(None, font_size)
        self.text = ''
        self.active = False
        self.visible = True
        self.tb_color="WHITE"
        self.color_active = pygame.Color('lightskyblue3')
        self.color_inactive = pygame.Color('gray15')

    def handle_event(self, event):
        """
        Xử lý sự kiện được chỉ định cho TextBox .
        Đối số:
        - event : Sự kiện cần xử lý.
        """
        if self.visible:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False

            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.tb_color="BLACK"
                    #self.visible = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def update(self,surface):
        """
        Cập nhật hộp văn bản trên bề mặt đã chỉ định.
        Đối số: Bề mặt để cập nhật hộp văn bản (surface)
        """
        if self.visible:
            pygame.draw.rect(surface, self.tb_color, self.rect, 2) # vẽ HCN
            text_surface = self.font.render(self.text, True, pygame.Color("WHITE")) # phong chu mau chu 
            text_rect = text_surface.get_rect(center=self.rect.center) # đinh vị lại vic trí chính giữa
            surface.blit(text_surface, (text_rect))


class Button:
    """
    Lớp đại diện cho một Button.

    Thuộc tính:
    - x,y: Vị trí của hộp văn bản 
    - width (int): Chiều rộng của hộp văn bản.
    - height (int): Chiều cao của hộp văn bản.
    - rect : Hình chữ nhật đại diện cho hộp văn bản.
    - text (str): Văn bản hiện tại trong hộp văn bản.
    - visible (bool): Xác định liệu button có hiển thị hay không.
    - button_color (str): Màu của button
    """
    def __init__(self, x, y, width, height, text, button_color, text_color, visible=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.button_color = button_color
        self.text_color = text_color
        self.visible = visible

    def draw(self, surface):
        """
        Vẽ button lên bề mặt đã chỉ định.

        Đối số:
        - surface: Bề mặt để vẽ nút lên.
        """
        if self.visible:
            pygame.draw.rect(surface, self.button_color, self.rect)
            font = pygame.font.Font(None, 32)
            text = font.render(self.text, True, self.text_color)
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text, text_rect)

    def is_clicked(self, pos):
        """
        Kiểm tra xem nút đã được nhấp chuột hay chưa.
        Đối số:
        - pos (tuple): Tọa độ chuột (x, y).
        Trả về:
        - bool: True nếu nút đã được nhấp chuột, False nếu không.
        """
        if self.visible:
            return self.rect.collidepoint(pos)
        return False
