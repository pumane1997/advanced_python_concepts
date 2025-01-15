import justpy as jp
from webapp import layout

class Home:
    '''
        xxxx
    '''

    path = '/'

    @classmethod
    def serve(clas, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-grey-400 h-screen p-2') 
        jp.Div(a=div, text='This is the home page', classes='text-4xl m-2')
        jp.Div(a=div, text='''
        The light was out on the front porch of the house. This was strange. Judy couldn't remember a time when she had ever seen it out. 
        She hopped out of her car and walked to the door. It was slightly ajar and she knew this meant something terrible. 
        She gently pushed the door open and hall her fears were realized. "Surprise! Happy Birthday!" everyone shouted.
        ''', classes='text-lg m-2')
        return wp