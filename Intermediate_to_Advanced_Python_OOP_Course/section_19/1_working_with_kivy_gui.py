'''
Kivy App is made of 4 objects

- App object
- Screen Manager object
- Screen object
- Widget object: This is a category of the object because we will have multiple and different
                 types of objects such as button, text input, image, drop down list etc. whatever
                 widget the app requires.

For each of these four types of objects, we will class in our code.
'''

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


# App class
'''
Kivy is library and has its own classes. One of it is App class which initializes the actual app.
We inherit it to our class.

The hierarchy is 
    -> App (Main App in our code)
    -> Screen Manager (named as RootWidget by programmers)
    -> Screen (we will have as many screen classes as there are screens on our app)
'''

class FirstScreen(Screen):
    # This will have some methods depending on what you want to do, in our case we want to search images
    
    def search_images(self):
        pass


class RootWidget(ScreenManager):
    pass # This generally always will be an empty class unless any special feature needed.
         # It inherits everything from ScreenManager class

class MainApp(App): # This will be the child of App class of Kivy App class -> all attributes and
                 # methods will be applicable

    def build(self): # There is build method for app class in kivy, we have to overwrite it 
                            # -> This is expeceted by kivy and it should return screen manager
                     # This should return another class that we will be building -> RootWidget
        return RootWidget() # initialized the root widget class

    # So App class, along with its parent functionality will return Rootwidget class

MainApp().run()

## This is boiler plate code (above)