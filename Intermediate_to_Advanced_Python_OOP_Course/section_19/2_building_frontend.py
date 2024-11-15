from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

'''
to build the widgets there are two ways
     - either write code in first screen class -> modify it
     - correct way and the best way is to create new file 
        - give file a meaningful name (frontend) and give extension as .kv
        - in this file we need to write simple kivy code
        - this code defines how screen looks like  

checkout frontend.kv file
'''

# following steps are needed to connect this file with frontend.kv file - line 17 & 18

from kivy.lang import Builder
Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    
    def search_images(self):
        pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self): 
        
        return RootWidget()


MainApp().run()