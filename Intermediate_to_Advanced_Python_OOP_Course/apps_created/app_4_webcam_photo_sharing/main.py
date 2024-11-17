from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import FileSharer
import time
from kivy.core.clipboard import Clipboard
import webbrowser


Builder.load_file('frontend.kv')

class CameraScreen(Screen): # we are not going to build separate WebCam 
                            # class becasue we already have this CameraScreen 
                            # class which kind of represents WebCam. This is both
                            #  kivy screen and our webcam object 
    
    def start(self):
        self.ids.cam.play = True
        self.ids.camera_button.text = 'Stop'
        self.ids.cam.texture = self.ids.cam._camera.texture

    def stop(self):
        self.ids.cam.play = False
        self.ids.camera_button.text = 'Start'
        self.ids.cam.texture = None

    def capture(self):
        camera = self.ids.cam
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filename = 'captured_image'+current_time+'.png' # if you want anyy variable to be part of the class, then you have
                                                             # the you have to prefix itr with 'self.' else it is just a local 
                                                             # variable. After prefixing, you can access its value outside of 
                                                             # class/function
        self.filepath = 'files/'+self.filename
        if camera.play:
            camera.export_to_png(self.filepath)
            print(f"Image captured and saved as '{self.filename}'!")
        else:
            print('Camera is not on')
        self.manager.current = 'image_screen' # here we access manager attribute of Screen Class which is parent of this one
        self.manager.current_screen.ids.img.source = self.filepath
        # there is difference betweeb self.ids.<id name> vs self.manager.current_screen.ids.<id name>
        # self.ids - this access the widget of class where code is written
        # self.manager.current_screen.ids - will access widget of screen that usere is using


class ImageScreen(Screen):
    
    link_message = 'Create a link first!' # This is a class variable and not and instance variable - this will be same for every instance

    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        self.url = FileSharer(file_path).share() # the method is executed here
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url) # we dont even need to instansiate the Clipboard class because copy() is a class method and not an object method
            # we need to design this method in such a way that this only executes when user has already created a link, else this eill error out
            # as user will not have pressed create link -> so create_link() will not be executed and there will be no self.url
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self): 
        
        return RootWidget()


MainApp().run()