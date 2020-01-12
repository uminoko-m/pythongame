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
        pyxel.init(255, 180)        #window sizeの指定　最大(255,255)
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

        # 始めの位置
        self.player_x = 42
        self.player_y = 60
        self.player_vy = 0
        self.monster = [(i * 60, randint(0, 104), True) for i in range(4)]
 
        pyxel.playm(0, loop=True)
        pyxel.run(self.update_game, self.draw_game)

    def update_game(self):
        if pyxel.btnp(pyxel.KEY_Q):     #Qを押したら終了
            pyxel.quit()

        self.update_player()            #キャラ操作

        for i, v in enumerate(self.monster):      #魔物出現
            self.monster[i] = self.update_monster(*v)


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
        pyxel.cls(12)
 
        # 魔物
        for x, y, is_active in self.monster:
            if is_active:
                pyxel.blt(x, y, 0, 0, 90, 16, 14, 0)
 
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
 
        # スコアを表示
        s = "Score {:>4}".format(self.score)
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)

       
        #pyxel.blt(48, 45, 0, 0, 0, -48, 72,0)       #勇者
        #pyxel.blt(60,120, 0, 0, 72, -15, 16,0)      #勇者ミニ
        #pyxel.blt(100, 45, 1, 0, 0, -55, 72,0)      #魔法使い
        #pyxel.blt(110, 120, 1, 0, 72, -15, 16,0)    #魔法使いミニ
        #pyxel.blt(150, 45, 2, 0, 0, -48, 72,0)      #戦士

    def update_monster(self, x, y, is_active):
        if is_active and abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            is_active = False
            self.score += 100
            self.player_vy = min(self.player_vy, -8)
            pyxel.play(3, 4)
 
        x -= 2
 
        if x < -40:
            x += 290
            y = randint(0, 150)
            is_active = True
 
        return (x, y, is_active)


App()