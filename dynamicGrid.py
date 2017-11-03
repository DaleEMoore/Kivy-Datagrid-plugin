#!/usr/bin/env python2
# From: https://stackoverflow.com/questions/15497629/kivy-template-with-dynamic-grid-layout
# This MIGHT BE a tangent from what's being said here...
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
import datetime

Builder.load_string('''
#:kivy 1.6
[SideBar@BoxLayout]:
    content: content
    orientation: 'vertical'
    size_hint: ctx.size_hint if hasattr(ctx, 'size_hint') else (1, 1)
    Image:
        source: ctx.image
        size_hint: (1, None)
        height: root.width
    GridLayout:
        cols: 2
        # just add a id that can be accessed later on
        id: content

<Root>:
    Button:
        center_x: root.center_x
        text: 'press to add_widgets'
        size_hint: .2, .2
        on_press:
            # what comes after `:` is basically normal python code
            sb.content.clear_widgets()
            # however using a callback that you can control in python
            # gives you more control
            root.load_content(sb.content)
    SideBar:
        id: sb
        size_hint: .2, 1
        image: 'data/images/image-loading.gif'
''')

class Root(FloatLayout):

    def load_content(self, content):
        for but in range(20):
            content.add_widget(Button(
                                text=str(but)))
            print("add button " + str(but))
        now = datetime.datetime.now()
        print str(now)


class MyApp(App):
    def build(self):
        return Root()

if __name__ == '__main__':
    MyApp().run()