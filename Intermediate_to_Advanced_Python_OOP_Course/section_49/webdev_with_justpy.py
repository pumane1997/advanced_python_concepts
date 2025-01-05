import justpy as jp 

wp = jp.WebPage() # we create WebPage class instance
# Justpy is made of objects
jp.Div(a=wp, text="Text in Div") # We are adding Div instance to the webpage
jp.Div(a=wp, text="Another Div")

# to host the webpage, i.e. to start the server we use following code
# jp.justpy()

# the webpage needs to be connected to a url

# the above code should be in the function or class methods, lets put it in function
# for now


def home():
    wp = jp.WebPage() 
    jp.Div(a=wp, text="Text in Div") # We are adding Div instance to the webpage
    jp.Div(a=wp, text="Another Div")
    return wp

# one of the ways to connect url to this webpage is to use Route class 
jp.Route(path='/', wpfunc=home) # second arg needs the function that returns webpage instance
# another way to do it is use decorator for the function returning the webpage
# @jp.SetRoute('/')

# -------------- Styling
# for styling we use classes arg to div instance whose value is tailwind code

def about():
    wp = jp.WebPage() 
    jp.Div(a=wp, text="Text in Div", classes="text-green-200") # valid range (100, 900, 100 step)
    jp.Div(a=wp, text="Another Div", classes="text-green-200 \
                                              bg-yellow-500 \
                                              font-serif \
                                              text-lg")
    return wp

def demo_components():
    wp = jp.WebPage() 
    # div component for bg for whole webpage - this is the main div
    div = jp.Div(a=wp, classes='bg-grey-400 h=screen') # we will assign this as parent of all components on teh webpage
    # input component, 'a=wp' arg adds it to webpage
    jp.Input(a=div, placeholder='First value', classes="form-input")
    jp.Input(a=div, placeholder='Second value', classes="form-input")
    # div component
    jp.Div(a=div, text='Result goes here', classes='text-grey-600') 
    # button component
    jp.Button(a=div, text='Calculate', classes='text-white-600 \
        border border-blue-500 \
        m-2 \
        px-2 \
        py-1 \
        rounded \
        hover:bg-red-500 \
        hover:text-white')
    return wp

def adding_components_to_grid():
    wp = jp.WebPage() 
    div = jp.Div(a=wp, classes='bg-grey-400 h-screen') 
    # we implement divs in grid by below method
    
    # ---------
    div1 = jp.Div(a=div, classes='grid grid-cols-3 gap-4 p-4') 
    # following three grids will be assigned this as parent  
    # ---------
    
    jp.Input(a=div1, placeholder='First value', classes="form-input")
    jp.Input(a=div1, placeholder='Second value', classes="form-input")
    jp.Div(a=div1, text='Result goes here', classes='text-grey-600') 
    
    # ---------
    div2 = jp.Div(a=div, classes='grid grid-cols-2 gap-4') 
    # following three grids will be assigned this as parent  
    # ---------
    
    jp.Button(a=div2, text='Calculate', classes='text-white-600 \
        border border-blue-500 \
        m-2 \
        px-2 \
        py-1 \
        rounded \
        hover:bg-red-500 \
        hover:text-white')
    jp.Div(a=div2, text='Cool Interactive div', classes='text-grey-600')
    return wp

# events are handled by other function which will be called 'event-handler'
# the handling_events function is called as request handler
def handling_events():
    wp = jp.WebPage() 
    div = jp.Div(a=wp, classes='bg-grey-400 h-screen') 
    div1 = jp.Div(a=div, classes='grid grid-cols-3 gap-4 p-4') 
    in_1 = jp.Input(a=div1, placeholder='First value', classes="form-input")
    in_2 = jp.Input(a=div1, placeholder='Second value', classes="form-input")
    d_output = jp.Div(a=div1, text='Result goes here', classes='text-grey-600')
    div2 = jp.Div(a=div, classes='grid grid-cols-2 gap-4') 
    jp.Button(a=div2, text='Calculate', classes='text-white-600 border border-blue-500 \
        m-2 px-2 py-1 rounded hover:bg-red-500 hover:text-white', \
        click = sum_up, # this is where event handler function is mentioned
        # the attributes created - 
        in1=in_1, in2=in_2, d = d_output) # in1, in2 can be accessed in event handler function via widget method 
        # -> widget.in1 => this will return the input instances 
    '''
        - When we pass an arg here, ex: in1=in_1 what we are doing is that we are adding attribute 
        to the button instance. In this case the value of that arg is one of the input instances

        - Since the event handler function is mentioned in the button component, the widget is now the
        button and the attribute of the button can be accessed by widget.<attribute>.value
    '''
    jp.Div(a=div2, text='Cool Interactive div', classes='text-grey-600 hover:bg-red-500',
           mouseenter=mouse_enter, mouseleave=mouse_leave)
    return wp

# event handler function
def sum_up(widget, msg): # we need to pass two parameters to this function, these can be named
    # anything, but 'widget' and 'msg' is recommended.
    print(widget.in1.value, widget.in2.value)
    sum = float(widget.in1.value) + float(widget.in2.value)
    widget.d.text = sum

# as we have mentioned this event handler function in line 102, when justpy
# calls this method, it passes value of 
# widget param -> component which generated event (button in this case)
# msg param -> dict which contains info about the event (ex: event type, id, class name etc) 

# another event handler
def mouse_enter(widget, msg):
    widget.text = 'Mouse entered'

def mouse_leave(widget, msg):
    widget.text = 'Mouse left'

def quasar_interface(): # this is diffirent type of styling interface
    # Quasar supports tailwind so you can just put tailwind=True in below line for it 
    # but Quasar should still be used over webpage becasuse it supports some advanced components (nav bar)
    # so it is addition to tailwind as quasar properties can also be used now along with tailwind
    # Quasar is based on Vue.js
    wp = jp.QuasarPage(tailwind=True) 
    div = jp.Div(a=wp, classes='bg-grey-400 h-screen') 
    div1 = jp.Div(a=div, classes='grid grid-cols-3 gap-4 p-4') 
    in_1 = jp.Input(a=div1, placeholder='First value', classes="form-input")
    in_2 = jp.Input(a=div1, placeholder='Second value', classes="form-input")
    d_output = jp.Div(a=div1, text='Result goes here', classes='text-grey-600')
    div2 = jp.Div(a=div, classes='grid grid-cols-2 gap-4') 
    # this is quasar component
    # ------------------------
    jp.QBtn(a=div2, text='Calculate', 
        color='primary', label='primary', 
        click = sum_up, in1=in_1, in2=in_2, d = d_output)
    # ------------------------
    jp.Div(a=div2, text='Cool Interactive div', classes='text-grey-600 hover:bg-red-500',
           mouseenter=mouse_enter, mouseleave=mouse_leave)
    return wp

jp.Route(path='/about', wpfunc=about)
jp.Route(path='/demo_components', wpfunc=demo_components)
jp.Route(path='/adding_components_to_grid', wpfunc=adding_components_to_grid)
jp.Route(path='/handling_events', wpfunc=handling_events)
jp.Route(path='/quasar_interface', wpfunc=quasar_interface)

jp.justpy()



# python webdev_with_justpy.py