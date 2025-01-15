import justpy as jp
from definition import Definition

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
        
        input_div = jp.Div(a=div, classes='grid grid-cols-2') 
        input_box = jp.Input(a=input_div, placeholder='Type in a word here', 
                 classes="m-2 bg-grey-100 border-2 border-gray-200 \
                 w-64 focus: bg-white focus:border-purple-500 py-2 px-4 h-8")
        output_div = jp.Div(a=div, classes='m-2 p-2 text-lg border-2 border-gray-200 \
               h-40') 
        jp.Button(a=input_div, text='Get Definition', classes='border-2 text-gray-500 \
                 ', click=cls.get_definition, ip_div = input_box, op_div=output_div)
        
        
        return wp

    @staticmethod
    def get_definition(widget, msg):
        definition = Definition(widget.ip_div.value).get()
        widget.op_div.text = " ".join(definition)


# Static method is a method inside a class that works like function. 
# It does not expect instance of class or class itself as the argument
# It is imdependent and used for organization issues 