import justpy as jp
from webapp.home import Home
from webapp.about import About


jp.Route(path=Home.path, wpfunc=Home.serve)
jp.Route(path=About.path, wpfunc=About.serve)
jp.justpy(port=8001)

# python main.py