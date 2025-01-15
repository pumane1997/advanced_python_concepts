import justpy as jp

class DefaultLayout(jp.QLayout):
    '''
    This class represents default layout of of the web app
    '''

    def __init__(self, view="hHh lpR fFf", **kwargs): # when initialized, the args given will be stored as dict which is kwargs
        super().__init__(view=view, **kwargs) # this instansiates parent i.e. jp.Qlayout in our case

        # layout = jp.QLayout(a=wp, view="hHh lpR fFf") -> these args can be given when parent is initiated
        # the equivalent of this is first line after __init__
        
        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=self, show_if_above=True, v_mode='left',
                            bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroller)
        a_classes ='p-2 m-2 text-lg text-blue-400 hover:text-blue-700'
        jp.A(a=qlist, text='Home', href='/', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='Dictonary', href='/dictonary', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='About', href='/about', classes=a_classes)
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon='menu',
                click=self.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='Instant Dictonary')

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
        
