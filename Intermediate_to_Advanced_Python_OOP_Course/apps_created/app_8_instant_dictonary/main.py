import inspect
import re
import justpy as jp
from webapp import page
from webapp.home import Home
from webapp.about import About
from webapp.dictonary import Dictonary

imports = list(globals().values())
# print(imports)

# globals returns a dict of all global names available in this modeule
# It has to be converted to list because while iterating the size of dict 
# increases and we get runtime error

objects = [item for item in imports if isinstance(item, type)]
# print(objects)

# print(f"Page in current module: {Page}")
# print(f"Page in Home module: {Home.__bases__[0]}")

for obj in objects:
    if inspect.isclass(obj): # issubclass function does not work on objects other than class type
        if issubclass(obj, page.Page) and hasattr(obj, 'path'): 
            # the hasattr checks if given object has specified attribute but the 
            # issue is that there might be another obj that may have path attr so
            # we have created abstract class page, made all other page classes its 
            # children & added that filtering condition as well -  issubclass
            jp.Route(obj.path, obj.serve)

'''

jp.Route(path=Home.path, wpfunc=Home.serve)
jp.Route(path=About.path, wpfunc=About.serve)
# jp.Route(path=Dictonary.path, wpfunc=Dictonary.serve)
jp.Route(path=Dictonary.path, wpfunc=Dictonary.serve)

#! Just py does not initialize the class, it just calles the specified 
# method of the class in this case by passing some request to it. The thing is
# that the instance method can only be used after instance of class is created
# so we must write the serve method as class method and not instance method
# after doing this we must do something for the (justpy)request as well

'''

jp.justpy(port=8001)

# python main.py

