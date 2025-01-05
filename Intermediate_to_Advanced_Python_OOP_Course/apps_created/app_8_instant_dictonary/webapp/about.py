import justpy as jp

class About:
    '''
        xxxx
    '''

    path = '/about'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True) # we have instansiated jp class here so this is a case of composition (different from inheritance)
        div = jp.Div(a=wp, classes='bg-grey-400 h-screen') 
        jp.Div(a=div, text='This is the about page', classes='text-4xl m-2')
        jp.Div(a=div, text='''
        The light was out on the front porch of the house. This was strange. Judy couldn't remember a time when she had ever seen it out. She hopped out of her car and walked to the door. It was slightly ajar and she knew this meant something terrible. She gently pushed the door open and hall her fears were realized. "Surprise! Happy Birthday!" everyone shouted.
        ''', classes='text-lg m-2')
        return wp