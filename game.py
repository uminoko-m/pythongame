import pyxel

class App:
    def __init__(self):
        pyxel.init(255, 180)        #window sizeの指定　最大(255,255)
        pyxel.load("picture.pyxres")     #画像読み込み

        # Starting Point
        self.player_x = 72
        self.player_y = 16

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):     #Qを押したら終了
            pyxel.quit()
        self.update_player()

    def update_player(self):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.player_x = max(self.player_x - 2, 0)
 
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)
 
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD_1_UP):
            self.player_y = max(self.player_y - 2, 0)
 
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD_1_DOWN):
            self.player_y = min(self.player_y + 2, pyxel.height - 16)

    def draw(self):
        pyxel.cls(0)

        pyxel.blt(self.player_x,self.player_y, 0, 0, 72, -15, 87,0)      #勇者ミニ
        #pyxel.blt(48, 45, 0, 0, 0, -48, 72,0)       #勇者
        #pyxel.blt(60,120, 0, 0, 72, -15, 87,0)      #勇者ミニ
        #pyxel.blt(100, 45, 1, 0, 0, -55, 72,0)      #魔法使い
        #pyxel.blt(110, 120, 1, 0, 72, -15, 87,0)    #魔法使いミニ
        #pyxel.blt(150, 45, 2, 0, 0, -48, 72,0)      #戦士


App()