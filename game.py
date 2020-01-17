from collections import deque, namedtuple
from random import randint
import pyxel

Point = namedtuple("Point", ["w", "h"])  # キャラの向き

UP = Point(-16, 16)
DOWN = Point(-16, 16)
RIGHT = Point(-16, 16)
LEFT = Point(16, 16)

class App:
    def __init__(self):
        pyxel.init(255, 160)        #window sizeの指定　最大(255,255)
        pyxel.load("picture.pyxres")     #画像読み込み
        pyxel.run(self.update_menu, self.draw_menu)
        

    def draw_menu(self):        #menu画面の描写
        pyxel.cls(0)        #背景色　黒
        s = "--- PUSH SPACE KEY ---"
        pyxel.text(80, 90, s, 7)

    def update_menu(self):      #menu画面の操作
        #　スペースキーを押したらゲーム開始
        if pyxel.btn(pyxel.KEY_SPACE):
            self.game_start()
        
    def game_start(self):           #ゲーム開始
        self.direction = RIGHT
        # スコア
        self.score = 0
        #ハート
        self.countheart=5
        # 始めの位置
        self.player_x = 20
        self.player_y = 60
        self.player_vy = 0
        self.monster = [(200,randint(30,100), True)for i in range(1)]
        self.fire=[]
        self.flag=0
        for i in range(len(self.monster)):
            self.fire.append((self.monster[i][0]-16,self.monster[i][1],self.monster[i][2],self.flag))

        self.star=[(randint(0,255),randint(0,150), True)for i in range(25)]

        pyxel.playm(0, loop=True)
        pyxel.run(self.update_game, self.draw_game)

    def update_game(self):
        if pyxel.btnp(pyxel.KEY_Q):     #Qを押したら終了
            pyxel.quit()
        if self.countheart ==0:         #ハートがなくなったら終了
            pyxel.quit()

        self.update_player()            #キャラ操作

        for i, v in enumerate(self.fire):    #炎
            self.fire[i] = self.update_fire(*v)

        for i, v in enumerate(self.monster):    #魔物
            self.monster[i] = self.update_monster(*v)

        for i, v in enumerate(self.star):      #星
            self.star[i] = self.update_star(*v)


    def update_player(self):        #キャラ操作詳細
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(self.player_x - 2, 0)
            self.direction = LEFT
 
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)
            self.direction = RIGHT

        if pyxel.btn(pyxel.KEY_UP):
            self.player_y = max(self.player_y - 2, 0)
            self.direction = UP

        if pyxel.btn(pyxel.KEY_DOWN):
            self.player_y = min(self.player_y + 2, pyxel.height - 16)
            self.direction = DOWN

    def draw_game(self):
        # 背景色
        pyxel.cls(0)
        #星を描写
        for x, y, is_active in self.star:
            if is_active:
                pyxel.blt(x, y, 0, 16, 104, 6, 6, 0)
 
        # 火
        for x, y, is_active,flag in self.fire:
            if is_active:
                if flag==0:
                    pyxel.blt(x,y,0,16,88,16,16,0)
                else:
                    pyxel.blt(x,y,0,16,88,-16,16,0)

        # 魔物
        for x, y, is_active in self.monster:
            if is_active:
                pyxel.blt(x, y, 0, 24, 72, 31, 15, 0)

        # 勇者ミニ
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            0,
            72,
            self.direction[0],
            self.direction[1],
            0,
        )

        # ハート表示
        hx=0
        for i in range(self.countheart):
            pyxel.blt(hx,10,0,0,104,16,16,0)
            hx+=16

        # スコアを表示
        s = "Score {:>4}".format(self.score)
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)

    def update_star(self,x,y,is_active):
        if is_active and abs(x - self.player_x) < 5 and abs(y-self.player_y)< 5:
            self.countheart-=1

        n=2
        x-=n
        
        if x < -40:
            x += 290
            y = randint(30, 150)
            is_active = True
        return (x, y, is_active)

    def update_monster(self,x,y,is_active):
        if is_active and abs(x - self.fire_x) < 10 and abs(y-self.fire_y)< 10:
            is_active = False
            self.score += 100
            self.flag=0

        if is_active==False:
            x =200
            y = randint(30, 130)
            is_active = True

        self.monster_x=x
        self.monster_y=y
        return(x,y,is_active)

    def update_fire(self, x, y, is_active,flag):
        if is_active and abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            if pyxel.btn(pyxel.KEY_SPACE):      #スペースキーを押したら炎反転
                is_active = True
                self.score += 100
                flag=1
                #self.player_vy = min(self.player_vy, -8)
                #pyxel.play(3, 4)
            else:
                is_active=False

        if flag==1:
            x+=3
        else:
            x-=3

        if x < -40:
            x=self.monster_x-16
            y=self.monster_y
            is_active = True
            flag=0

        if x > 250:
            x=self.monster_x-16
            y=self.monster_y
            is_active = True
            flag=0

        self.fire_x=x
        self.fire_y=y
        return (x, y, is_active,flag)


App()