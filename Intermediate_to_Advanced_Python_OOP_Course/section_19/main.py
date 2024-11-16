from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import download_images

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    
    def search_images(self):
        query = self.manager.current_screen.ids.user_query.text 
        download_images.download_image(query)
        self.manager.current_screen.ids.img.source = './files/current_image.jpg'


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self): 
        
        return RootWidget()


MainApp().run()