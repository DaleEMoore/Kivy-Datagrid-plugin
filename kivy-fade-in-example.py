#!/usr/bin/env python2

# From: http://codegist.net/search/kivy-datagrid/2

'''
Under WTFPL - http://www.wtfpl.net
'''
import kivy

kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.animation import Animation
from kivy.core import window

SIZE = 30
FORMAT = (10, 16)
window.Window.size = [SIZE * i for i in FORMAT]
window.Window.clearcolor = [0.2, 0.2, 0.2, 1]


class lightButton(Button):
    def __init__(self, *args, **kws):
        kws.update(background_color=[1, 1, 1, 1])
        Button.__init__(self, *args, **kws)
        self.border = [16, 16, 30, 16]


class lightLabel(Label):
    def __init__(self, *args, **kws):
        Label.__init__(self, *args, **kws)


class TestApp(App):
    def compl(self, *args, **kws):
        print "complete:animation"

    def animate_label(self, instance):
        self.main_label.color = [1, 1, 1, 0]
        anim = Animation(color=[1, 1, 1, 0.7])
        anim.bind(on_complete=self.compl)
        anim.start(self.main_label)

    def build(self):
        self.main_grid = GridLayout(rows=2, cols=1, padding=50)
        print("Needs ./Aliquam.ttf")
        self.main_label = lightLabel(text='Text example test', color=[1, 1, 1, 0.0],
                                     font_name='./Aliquam.ttf', font_size='30px')
        self.main_button = lightButton(text='ok', on_press=self.animate_label)
        self.main_grid.add_widget(self.main_label)
        self.main_grid.add_widget(self.main_button)
        return self.main_grid


if __name__ == '__main__':
    TestApp().run()
