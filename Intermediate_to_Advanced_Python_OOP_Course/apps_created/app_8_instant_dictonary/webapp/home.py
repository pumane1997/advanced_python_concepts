import justpy as jp

class Home:
    '''
        xxxx
    '''

    path = '/'

    @classmethod
    def serve(clas, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode='left',
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
                click=clas.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='Instant Dictonary')
        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes='bg-grey-400 h-screen p-2') 
        jp.Div(a=div, text='This is the home page', classes='text-4xl m-2')
        jp.Div(a=div, text='''
        The light was out on the front porch of the house. This was strange. Judy couldn't remember a time when she had ever seen it out. 
        She hopped out of her car and walked to the door. It was slightly ajar and she knew this meant something terrible. 
        She gently pushed the door open and hall her fears were realized. "Surprise! Happy Birthday!" everyone shouted.
        ''', classes='text-lg m-2')
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True