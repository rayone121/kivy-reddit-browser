from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import requests
from kivy.uix.widget import Widget
from post import Post
import json

with open('credential.json', 'r') as f:
    cred = json.load(f)

client_auth = requests.auth.HTTPBasicAuth(cred['client_id'], cred['secret_key'])

post_data = {
    'grant_type': 'password',
    'username': cred['username'],
    'password': cred['password'],
}

headers = {'User-Agent': 'Api/0.0.1'}

TOKEN_ACCESS_ENDPOINT = 'https://www.reddit.com/api/v1/access_token'

res = requests.post(TOKEN_ACCESS_ENDPOINT, data=post_data, headers=headers, auth=client_auth)

if 'error' in res.json():
    print(f'error: {res.json()["error"]}')
    exit(-1)
token_id = res.json()['access_token']

headers['Authorization'] = f'bearer {token_id}'

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).json()

Builder.load_file('post.kv')

class Search(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def search_func(self):
        search_url = f'https://oauth.reddit.com/r/{self.ids.search_box.text}'
        res = requests.get(search_url, headers=headers)
        if res.status_code != 200:
            self.results.add_widget(Label(text='[size=24][b]Subbreddit not found[/b][/size]',
                                          markup=True,
                                          color='#b80000'
                                          ))
            return
        for post in res.json()['data']['children']:
            self.results.add_widget(Post(title=post['data']['title'],
                                         ptext=post['data']['selftext'],
                                         sub=post['data']['subreddit_name_prefixed']
                                         ))

    def remove_item(self):
        self.ids.search_results.clear_widgets()

class Subreddit(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class UserProfile(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainWindow(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


kv = Builder.load_file('main.kv')


class MainApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MainApp().run()
