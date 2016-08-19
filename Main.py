from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.vector import Vector


class LiveGame(GridLayout):
    #width = ObjectProperty(None)
    #height = ObjectProperty(None)

    def build(self):
        layout = GridLayout(rows=20, cols=20)

        for i in range(20):
            for j in range(20):
                layout.add_widget(Cell(i, j))

        return layout


class Cell(Widget):
    def __init__(self, x, y):
        self.vector = Vector(x, y)
        self.nb = []
    # position
    pos = Vector(1,1)
    pass


class LiveApp(App):
    def build(self):
        game = LiveGame()
        return game

if __name__ == '__main__':
    LiveApp().run()