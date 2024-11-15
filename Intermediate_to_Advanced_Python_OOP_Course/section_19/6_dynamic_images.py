from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    
    def search_images(self): # add methods here in screen classes to add functionality for 
                             # your screens in the app
        self.manager.current_screen.ids.img.source = 'files/Id_card_photo.jpg' 
        # this is done to add functionality for button's on press property (it has search_images function)
        # you need to add id = img to image widget as it is written here
        # self refers to the current instance of FirstScreen class.
        # manager is an attribute of the Screen object - FirstScreen is inheriting this
        # similarly current_screen -> ids
        # ids will give list of ids in the FirstScreen object
        # img is the id name and source is its property

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self): 
        
        return RootWidget()


MainApp().run()