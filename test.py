import pyxel


class App:
    def __init__(self):
        pyxel.init(128, 128, title="test")
        pyxel.load("test.pyxres")
        self.x = 50
        self.y = 50

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.y = self.y - 1

        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = self.y + 1

        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = self.x - 1

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = self.x + 1

        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8, 0)
        pass


App()
