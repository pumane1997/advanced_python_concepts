from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import FileSharer
import time

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
        filename = 'captured_image'+current_time+'.png'
        if camera.play:
            camera.export_to_png(f"files/{filename}")
            print("Image captured and saved as 'captured_image.png'!")
        else:
            print('Camera is not on')
 

class ImageScreen(Screen):
    
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self): 
        
        return RootWidget()


MainApp().run()