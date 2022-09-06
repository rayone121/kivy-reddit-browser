from kivy.app import App
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
import kivy.utils


class Red_post(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__()

        with self.canvas.before:
            Color(255, 0, 0, .64)
            self.rect = RoundedRectangle(radius=[10])
        self.bind(pos=self.update_rect, size=self.update_rect)

        self.title = Label(text='[b]' + kwargs['title'] + '[/b]',
                           markup=True,
                           pos_hint={"center_x": .5, "top": .9}, size_hint=(.5, .3),
                           halign="center"
                           )
        self.title.text_size = (self.bind(size=self.update_rect), None)
        self.title.height = self.title.texture_size[1]

        self.post_text = Label(text='[b]' + kwargs['ptext'] + '[/b]',
                               markup=True,
                               pos_hint={"center_x": .5, "top": .5}, size_hint=(.5, .3),
                               halign="center"
                               )
        self.post_text.text_size = (self.bind(size=self.update_rect), None)
        self.post_text.height = self.post_text.texture_size[1]

        #self.author = Label(text='[b]By' + kwargs['author'] + '[/b]',
                           #markup=True,
                           #pos_hint={"center_x": .5, "top": .7}, size_hint=(.5, .3),
                           #halign="left"
                           #)

        #self.author.text_size = (self.author.width * dp(2), None)
        #self.author.height = self.author.texture_size[1]

        #self.subreddit = Label(text=kwargs['subreddit'])

        self.add_widget(self.title)
        #self.add_widget(self.author)
        # self.add_widget(self.subreddit)
        self.add_widget(self.post_text)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
