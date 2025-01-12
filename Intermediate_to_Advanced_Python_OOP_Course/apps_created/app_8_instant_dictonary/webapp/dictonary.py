import justpy as jp

class Dictonary:
    '''
        xxxx
    '''

    path = '/dictonary'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True) 
        div = jp.Div(a=wp, classes='bg-grey-400 h-screen')
        jp.Div(a=div, text='Instant English Dictonary', 
               classes='grid grid-cols-1 gap-4 p-4 text-4xl m-2')
        jp.Div(a=div, text='Get the meaning of any word instantly as you type', 
               classes='gap-4 p-4 text-lg') 
        jp.Input(a=div, placeholder='Type in a word here', 
                 classes="m-2 bg-grey-100 border-2 border-gray-200 \
                 w-64 focus: bg-white focus:border-purple-500 py-2 px-4")
        jp.Div(a=div, classes='m-2 p-2 text-lg border-2 border-gray-200 \
               h-40') 
        
        return wp