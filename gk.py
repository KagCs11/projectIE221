import pygame
import random
import math
from pygame.locals import *
import pygame_gui
from player import player


donhay=5
class gk(player):
    """
    Lớp đại diện cho thủ môn.

    Thuộc tính:
    - x (int): Vị trí x của thủ môn.
    - y (int): Vị trí y của thủ môn.
    - color (tuple): Màu sắc của cầu thủ.
    - window: Bề mặt để vẽ lên.
    - sizedau (int): Kích thước đầu thủ môn.
    - sizebody (int): Kích thước cơ thể thủ môn.
    - sp (int): Tốc độ di chuyển của thủ môn.
    - phanxa (int): Phạm vi phản xạ của thủ môn.
    - tocdobay (int): Tốc độ bay của thủ môn.
    - speed (int): Giá trị thời gian chờ nhún chính của thủ môn.( tốc độ lắc người )
    - slow (int): Giá trị thời gian chờ nhún chính của thủ môn.( tốc độ lắc người )
    - speed_bay (int): Tốc độ bay hiện tại của thủ môn.
    - x2body (int): Tọa độ x của đường thẳng kết nối đầu và cơ thể thủ môn.
    - y2body (int): Tọa độ y của đường thẳng kết nối đầu và cơ thể thủ môn.
    - x1chan (int): Tọa độ x của chân trái của thủ môn.
    - x2chan (int): Tọa độ x của chân phải của thủ môn.
    - y1chan (int): Tọa độ y của chân trái của thủ môn.
    - y2chan (int): Tọa độ y của chân phải của thủ môn.
    - sizechan (int): Kích thước chân của thủ môn.
    - x1chanp (int): Tọa độ x của chân trái phản xạ của thủ môn.
    - x2chanp (int): Tọa độ x của chân phải phản xạ của thủ môn.
    - y1chanp (int): Tọa độ y của chân trái phản xạ của thủ môn.
    - y2chanp (int): Tọa độ y của chân phải phản xạ của thủ môn.
    - x1tayt (int): Tọa độ x của tay trái trên của thủ môn.
    - y1tayt (int): Tọa độ y của tay trái trên của thủ môn.
    - x2tayt (int): Tọa độ x của tay trái dưới của thủ môn.
    - y2tayt (int): Tọa độ y của tay trái dưới của thủ môn.
    - sizetay (int): Kích thước tay của thủ môn
    - x1tayp (int): Tọa độ x của tay phải phản xạ của thủ môn.
    - y1tayp (int): Tọa độ y của tay phải phản xạ của thủ môn.
    - x2tayp (int): Tọa độ x của tay phải trên của thủ môn.
    - y2tayp (int): Tọa độ y của tay phải trên của thủ môn.
    - px (int): phản xạ ( thời gian mà thut môn sẽ bay khi kể từ khi cầu thủ bắt đầu sút)
    - tocdobay (int): Tốc độ bay của thủ môn.
    - state_bay (str): Trạng thái hiện tại của thủ môn (đang bay lên hoặc đang bay xuống).
    - state_cham (str): Trạng thái hiện tại của thủ môn khi va chạm với bóng (đã va chạm hoặc chưa va chạm).
    - state_vui (str): Trạng thái hiện tại của thủ môn khi ăn mưng (đang nhảy lên hoặc nhảy xuôngs).
    """
    def __init__(self,x,y,color,window,sizedau,sizebody,sp,phanxa,tocdobay):
        super().__init__(x,y,color,window)
        self.speed=sp
        self.slow=sp
        self.speed_bay=2

        self.sizedau=sizedau+10

        self.sizebody=sizebody
        self.wbody=15
        self.x2body=0
        self.y2body=0

        self.x1chan=0
        self.x2chan=0
        self.y1chan=0
        self.y2chan=0
        self.sizechan=sizebody
        self.x1chanp=0
        self.x2chanp=0
        self.y1chanp=0
        self.y2chanp=0

        self.x1tayt=0
        self.y1tayt=0
        self.x2tayt=0
        self.y2tayt=0
        self.sizetay=sizebody
        self.x1tayp=0
        self.y1tayp=0
        self.x2tayp=0
        self.y2tayp=0

        self.px=phanxa
        self.tocdobay=tocdobay
        self.state_bay="len"
        self.state_cham="chua"
        self.state_vui="len"

        self.dx=0
        self.dy=0

        self.image_icon=[]
        self.image_icon.append(pygame.image.load("gk_gian2.png"))
        self.image_icon.append(pygame.image.load("gk_vui.png"))
        self.image_icon.append(pygame.image.load("gk_vui2.png"))
        self.image_icon.append(pygame.image.load("gk_vui3.png"))
        self.image_icon.append(pygame.image.load("gk_sad1.png"))
        self.image_icon.append(pygame.image.load("gk_sad2.png"))
        self.image_icon.append(pygame.image.load("gk_sad3.png"))
        self.i_icon=0


    def draw(self):
        """
        Vẽ thủ môn lên bề mặt window.
        """
        pygame.draw.circle(self.window, self.color, (self.x,self.y),self.sizedau)

        to=20

        pygame.draw.line(self.window, self.color, (self.x,self.y+5), (self.x2body,self.y2body), self.wbody)

        pygame.draw.line(self.window, self.color, (self.x1chan, self.y1chan), (self.x2chan, self.y2chan), to+5)
        pygame.draw.line(self.window, self.color, (self.x1chanp, self.y1chanp), (self.x2chanp, self.y2chanp),to+5)
        pygame.draw.line(self.window, self.color, (self.x1tayp, self.y1tayp), (self.x2tayp, self.y2tayp), to)
        pygame.draw.line(self.window, self.color, (self.x1tayt, self.y1tayt), (self.x2tayt, self.y2tayt), to)

        image_gk=self.image_icon[self.i_icon]
        image_gk=pygame.transform.scale(image_gk, (self.sizedau*2,self.sizedau*2))
        self.window.blit(image_gk, (self.x-self.sizedau,self.y-self.sizedau))

    def canh(self,ball,g):
        """
        Cập nhật tọa độ các phần của thủ môn dựa trên vị trí hiện tại , khung thành và quả bóng . khi thủ môn đang đứng canh 
        Tham số:
        - ball (Ball): Đối tượng bóng.
        - g (int): đối tượng khung thành 
        """
        if(check(self,ball,g)==1 ):
            ball.vang(self)
        self.x2body=self.x
        self.y2body=self.y+self.sizedau+self.sizebody
        self.x1chan=self.x2body
        self.y1chan=self.y2body-5
        self.x1chanp=self.x2body
        self.y1chanp=self.y2body-5
        self.x1tayt=self.x
        self.y1tayt=self.y+self.sizedau+2
        self.x1tayp=self.x
        self.y1tayp=self.y+self.sizedau+2

        if(self.slow==self.speed ): # tốc độ nhúc nhích 
            self.x2chan=random.randint(self.x1chan-(self.sizechan),self.x1chan-(self.sizechan/2))
            self.y2chan=random.randint(self.y1chan+self.sizechan-5,self.y1chan+self.sizechan-1)
            self.x2chanp=random.randint(self.x1chanp+(self.sizechan/2),self.x1chanp+(self.sizechan))
            self.y2chanp=random.randint(self.y1chanp+self.sizechan-5,self.y1chanp+self.sizechan-1)


            self.x2tayt=random.randint(self.x1tayt-self.sizetay,self.x1tayt-(self.sizetay/2)) 
            self.y2tayt=random.randint(self.y,self.y2body)

            self.x2tayp=random.randint(self.x1tayp+(self.sizetay/2),self.x1tayp+self.sizetay)
            self.y2tayp=random.randint(self.y,self.y2body)

            self.speed=0
        else:
            self.speed+=1

        self.wbody=15
    def di(self,huong,buoc):
        """
        phương thức di chuyển của thủ môn khi đi 

        Tham số:
        - huong (string): trái hoặc phải 
        - bước : số bước bỏ di chuyển 

        """
        for i in range(buoc):            
            if(huong=="trai"):
                self.x-=1
                self.x2chan-=1
                self.x2chanp-=1
                self.x2tayt-=1
                self.x2tayp-=1
            else:
                self.x+=1
                self.x2chan+=1
                self.x2chanp+=1
                self.x2tayt+=1
                self.x2tayp+=1

    def bay(self,huong,xa,gon,ball):
        dx=random.randint(self.tocdobay-2,self.tocdobay+2)
        dy=random.randint(self.tocdobay-2,self.tocdobay)
        """
        Cập nhật tọa độ của thủ môn khi đang bay để bắt quả bóng 

        Tham số:
        - huong (str): Hướng bay của thủ môn ("trai" hoặc "phai").
        - xa (int): Giá trị phạm vi bay của thủ môn.
        - gon (Gon): Đối tượng khung thành 
        - ball (Ball): Đối tượng bóng.

        """
        if(check(self,ball,gon)==1 ):
            ball.vang(self)
        self.px-=1
        if(self.px<=0 and self.y2body<=gon.y+gon.h):
            if(huong=="trai"):
                if(self.state_bay=="len" ):
                    #self.x-=self.tocdobay
                    self.x-=dx
                    self.y-=dy
                    #if(self.x%2==0):
                        #self.y-=self.tocdobay
                    if(self.y<=gon.y+10):
                        self.state_bay="xuong"
                elif(self.state_bay=="xuong" and self.y2chan<=gon.y+gon.h):
                    #self.y+=self.tocdobay
                    #self.x-=self.tocdobay/2
                    self.y+=dy*2
                    self.x-=dx/2

                self.x2body=self.x+self.sizebody
                self.y2body=self.y+self.sizebody
                self.wbody=25

                self.x1chan=self.x2body
                self.y1chan=self.y2body-1
                self.y2chan=self.y2body+self.sizechan-self.sizechan/2+10
                self.x2chan=self.x2body+self.sizechan
                self.x1chanp=self.x2body
                self.y1chanp=self.y2body-1
                self.x2chanp=self.x2body+self.sizechan+20
                self.y2chanp=self.y1chanp+5
                self.x1tayt=self.x+10
                self.y1tayt=self.y+self.sizedau+2
                self.x2tayt=self.x1tayt-self.sizetay-3
                self.y2tayt=self.y-2
                self.x1tayp=self.x+30
                self.y1tayp=self.y+self.sizedau+2
                self.x2tayp=self.x1tayp+self.sizetay+10
                self.y2tayp=self.y+5

            else:
                if(self.state_bay=="len" ):
                    self.x+=dx
                    self.y-=dy
                    if(self.y<=gon.y+10):
                        self.state_bay="xuong"
                elif(self.state_bay=="xuong" and self.y2chan<=gon.y+gon.h):
                    self.y+=dy*2
                    self.x+=dx/2
                self.x2body=self.x-self.sizebody
                self.y2body=self.y+self.sizebody
                self.wbody=25

                self.x1chanp=self.x2body
                self.y1chanp=self.y2body-1
                self.y2chanp=self.y2body+self.sizechan-self.sizechan/2+10
                self.x2chanp=self.x2body-self.sizechan


                self.x1chan=self.x2body+5
                self.y1chan=self.y2body-1
                self.x2chan=self.x2body-self.sizechan-20
                self.y2chan=self.y2body

                self.x1tayp=self.x-15
                self.y1tayp=self.y+self.sizedau+5
                self.x2tayp=self.x1tayp+self.sizetay+5
                self.y2tayp=self.y

                self.x1tayt=self.x-30
                self.y1tayt=self.y+self.sizedau+2
                self.x2tayt=self.x1tayt-self.sizetay-10
                self.y2tayt=self.y1tayt-5

    def canh_nhay(self,ball,g):
        if(check(self,ball,g)==1 ):
            ball.vang(self)
        """
        Phương thức thể hiện cầu thủ vui mừng.( cập nhật các tọa độ của thủ môn)
        """
        from P import y_gon
        from P import gon_h
        global y_gon
        global gon_h
        ##
        self.x2body=self.x
        self.y2body=self.y+self.sizedau+self.sizebody
        self.x1chan=self.x2body
        self.y1chan=self.y2body-5
        self.x1chanp=self.x2body
        self.y1chanp=self.y2body-5
        self.x1tayt=self.x
        self.y1tayt=self.y+self.sizedau+2
        self.x1tayp=self.x
        self.y1tayp=self.y+self.sizedau+2

        if(self.state_vui=="len"):
            self.y-=2
            self.x2chan-=2
            self.x2chanp-=2
            if(self.y<=y_gon+100):
                self.state_vui="xuong"
        if(self.state_vui=="xuong"):
            self.x2chan+=2
            self.x2chanp+=2
            self.y+=2
            if(self.y2chan>=y_gon+gon_h):
                self.state_vui="len"
        
        self.y2chan=random.randint(self.y1chan+self.sizechan-5,self.y1chan+self.sizechan-1)
        self.y2chanp=random.randint(self.y1chanp+self.sizechan-5,self.y1chanp+self.sizechan-1)
        self.x2chanp=self.x1chanp+self.sizechan
        self.x2chan=self.x1chan-self.sizechan
        self.y2tayt=self.y
        self.y2tayp=self.y
        self.x2tayt=self.x1tayt-self.sizetay
        self.x2tayp=self.x1tayp+self.sizetay

    def vui(self):
        global donhay
        if(donhay==0):
            self.i_icon=random.choice([1,2,3])
            donhay=7
        else:
            donhay-=1

    def sad(self):
        global donhay
        if(donhay==0):
            self.i_icon=random.choice([4,5,6])
            donhay=7
        else:
            donhay-=1


#
######################################################################def#########################################################################


def check_collision(line_start, line_end, circle_center, circle_radius):
    """
    Kiểm tra va chạm giữa một đường thẳng và một hình tròn.

    Args:
        line_start (tuple): Tọa độ điểm đầu của đường thẳng (x, y).
        line_end (tuple): Tọa độ điểm cuối của đường thẳng (x, y).
        circle_center (tuple): Tọa độ tâm của hình tròn (x, y).
        circle_radius (float): Bán kính của hình tròn.

    Returns:
        bool: True nếu có va chạm, False nếu không.

    """
    # Tính toán vector từ đầu đường thẳng tới đầu đường tròn
    line_vector = pygame.math.Vector2(line_end[0] - line_start[0], line_end[1] - line_start[1])
    
    # Tính toán vector từ đầu đường thẳng tới tâm đường tròn
    circle_vector = pygame.math.Vector2(circle_center[0] - line_start[0], circle_center[1] - line_start[1])
    
    # Tính toán độ dài của đường thẳng
    line_length = line_vector.length()
    
    # Đảm bảo vector đường thẳng không có độ dài bằng 0 để tránh lỗi chia cho 0
    if line_length == 0:
        return False
    
    # Chuẩn hóa vector đường thẳng _Chuẩn hóa line_vector để có line_unit_vector, đại diện cho hướng của đường thẳng.
    line_direction = line_vector.normalize()
    
    # Tính toán điểm trên đường thẳng gần nhất với tâm đường tròn
    closest_point = line_direction.dot(circle_vector)#độ dài chiếu của vector từ tâm hình tròn đến đường thẳng lên đơn vị vector hướng của đường thẳng.
    
    # Giới hạn giá trị của closest_point trong khoảng (0, line_length) để nằm trên đoạn đường thẳng
    closest_point = max(0, min(closest_point, line_length))
    
    # Tính toán tọa độ của điểm gần nhất trên đường thẳng
    closest_point_coords = (line_start[0] + closest_point * line_direction.x,
                            line_start[1] + closest_point * line_direction.y)
    
    # Tính toán khoảng cách giữa điểm gần nhất và tâm đường tròn
    distance = math.sqrt((closest_point_coords[0] - circle_center[0]) ** 2 +
                         (closest_point_coords[1] - circle_center[1]) ** 2)
    
    # Kiểm tra nếu khoảng cách nhỏ hơn bán kính đường tròn, tức là có va chạm
    if distance < circle_radius:
        return True
    else:
        return False


def check(ter,ball,g):
    """
    Kiểm tra va chạm giữa thủ môn(ter) và quả bóng(ball)
    đối số:
        ter (object): Đối tượng ter (thủ môn).
        ball (object): Đối tượng ball (quả bóng).
        g (object): Đối tượng g (khung thành).

    Returns:
        int: Kết quả kiểm tra va chạm:
            - 1 nếu có va chạm giữa thủ môn và quả bóng 
            - 2 nếu ball ra khỏi khung thành 
            - 0 nếu không có va chạm.

    """
    if(ball.size<=100 and ball.size>=30):
        if(check_collision((ter.x, ter.y+1),(ter.x2body, ter.y2body),(ball.x+(ball.size)/2,ball.y+(ball.size)/2),(ball.size/2))==True):
            ball.vang(ter)
            pygame.mixer.Sound('cham.wav').play()
            return 1
        elif(check_collision((ter.x1chan,ter.y1chan),(ter.x2chan, ter.y2chan),(ball.x+(ball.size)/2,ball.y+(ball.size)/2),(ball.size/2))==True):
            ball.vang(ter)
            pygame.mixer.Sound('cham.wav').play()
            return 1
        elif(check_collision((ter.x1chanp,ter.y1chanp),(ter.x2chanp, ter.y2chanp),(ball.x+(ball.size)/2,ball.y+(ball.size)/2),(ball.size/2))==True):
            ball.vang(ter)
            pygame.mixer.Sound('cham.wav').play()
            return 1 
        elif(check_collision((ter.x1tayt,ter.y1tayt), (ter.x2tayt,ter.y2tayt),(ball.x+(ball.size)/2,ball.y+(ball.size)/2),(ball.size/2))==True):
            ball.vang(ter)
            pygame.mixer.Sound('cham.wav').play()
            return 1 # thu mon bat duoc bong
        elif(ball.x>=g.x + g.w or ball.x < g.x or ball.y < g.y):
            return 2 # bong ra ngoai 
        else:
            return 0
    else:
        return 0