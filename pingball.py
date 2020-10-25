import pygame as pg
import sys

Size = [640, 480]
Width = Size[0]
Height = Size[1]

black = (0, 0, 0)
white = (255, 255, 255)
brown = (153, 102, 51)
orange = (255, 102, 0)

State_Wait = 0
State_play = 1
State_Won = 2
State_Over = 3

Brick_Width = 60
Brick_Height = 15

Paddle_Width = 60
Paddle_Height = 15

Ball_Size = 16
Ball_Radius = int(Ball_Size/2)

Max_Paddle_X = Width - Paddle_Width
Max_Ball_X = Width - Ball_Size
Max_Ball_Y = Height - Ball_Size

Paddle_Y = Height - Paddle_Height - 10

class pingball:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode(Size)
        pg.display.set_caption("PingBall_Game")
        self.fps = pg.time.Clock()
        self.font = pg.font.Font(None, 30)

        self.init_game()
    def init_game(self):
        self.hp = 3
        self.score = 0
        self.state = State_Wait

    def create_bricks(self):
        pass

    def draw_bricks(slef):
        pass

    def check_input(self):
        pass

    def move_ball(self):
        pass
    
    def handle_collisions(self):
        pass

    def show_stats(self):
        pass

    def show_message(self, message):
        pass

    def run(self):
        While True:
        for event in pg.event.get():
            if event type == pg.QUIT:
                pg.quit()
                sys.exit()

if __name__ == "__main__":
    pingball().run()
