import pyxel

class App:
    def __init__(self):
        pyxel.init(255, 180)        #window sizeの指定　最大(255,255)
        pyxel.load("picture.pyxres")     #画像読み込み
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(48, 45, 0, 0, 0, -48, 72,0)       #勇者
        pyxel.blt(100, 45, 1, 0, 0, -55, 72,0)      #魔法使い
        pyxel.blt(150, 45, 2, 0, 0, -48, 72,0)      #戦士

App()