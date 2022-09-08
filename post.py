from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.properties import ColorProperty


Builder.load_file('post.kv')

class Post(FloatLayout):
    color = ColorProperty()
    def __init__(self, **kwargs):
        super().__init__()

        self.ids.title.text ='[b]' + kwargs['title'] + '[/b]'
        self.ids.ptext.text = kwargs['ptext']
        self.ids.sub.text = '[b]'+ kwargs['sub'] + '[/b]'


