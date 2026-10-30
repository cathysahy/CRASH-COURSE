
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.lang import Builder
from kivy.base import runTouchApp


Builder.load_string('''
<RootWidget>:
    text: 'THE BACKGROUND'
    font_size: 150

    Image:
        source: 'colours.png'
        allow_stretch: True
        keep_ratio: False

    Image:
        source: 'colours2.png'
        allow_stretch: True
        keep_ratio: False

    Image:
        source: 'colours.png'
        allow_stretch: True
        keep_ratio: False
''')


class RootWidget(Label):

    def do_layout(self, *args):
        number_of_children = len(self.children)

        if number_of_children == 0:
            return

        width = self.width
        width_per_child = width / number_of_children

        for index, child in enumerate(self.children):
            child.height = self.height
            child.x = self.x + index * width_per_child
            child.y = self.y
            child.width = width_per_child

    def on_size(self, *args):
        self.do_layout()

    def on_pos(self, *args):
        self.do_layout()

    def add_widget(self, widget, *args, **kwargs):
        super(RootWidget, self).add_widget(
            widget, *args, **kwargs
        )
        self.do_layout()

    def remove_widget(self, widget, *args, **kwargs):
        super(RootWidget, self).remove_widget(
            widget, *args, **kwargs
        )
        self.do_layout()


runTouchApp(RootWidget())
