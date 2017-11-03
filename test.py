#/usr/bin/env python2
# From: http://codegist.net/code/kivy-datagrid/

import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Note, that all events get fired when pressing start (exit, opt & start)
# Also note, that when uncommenting the canvas it covers the entire screen
# btw: python3, archlinux, kivy 1.9.1-2 (community repo)
Builder.load_string('''
<MainMenu>:
    orientation: 'vertical'

    Button:
        text: "Start"
        on_touch_down: print ('start')

    Button:
        text: "Options"
        on_touch_down: print ('opt')

    Button:
        text: "Quit"
        on_touch_down: print ('quit')

#       canvas.after:
#           Rectangle:
#               size: self.parent.size
#               pos: self.parent.pos
''')


class MainMenu(BoxLayout):
    pass


class TestApp(App):
    running = False

    def build(self):
        root_widget = MainMenu()
        return root_widget


if __name__ == '__main__':
    TestApp().run()