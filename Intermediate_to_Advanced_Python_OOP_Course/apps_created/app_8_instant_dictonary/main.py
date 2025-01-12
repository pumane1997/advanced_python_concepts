import justpy as jp
from webapp.home import Home
from webapp.about import About
from webapp.dictonary import Dictonary



jp.Route(path=Home.path, wpfunc=Home.serve)
jp.Route(path=About.path, wpfunc=About.serve)
# jp.Route(path=Dictonary.path, wpfunc=Dictonary.serve)
jp.Route(path=Dictonary.path, wpfunc=Dictonary.serve)
#! Just py does not initialize the class, it just calles the specified 
# method of the class in this case by passing some request to it. The thing is
# that the instance method can only be used after instance of class is created
# so we must write the serve method as class method and not instance method
# after doing this we must do something for the (justpy)request as well
jp.justpy(port=8001)

# python main.py