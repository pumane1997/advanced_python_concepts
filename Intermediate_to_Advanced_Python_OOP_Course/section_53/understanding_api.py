
# Representational State Transfer API

'''
The client makes URL request & API process it
'''

from definition import Definition
import justpy as jp
import json

class Api:
    '''
        Handles requests at /api?w=word
    '''

    @classmethod
    def serve(cls, req): # this method will handle url requests
        wp = jp.WebPage()
        # we expect from the client to enter url parameters those requests  
        word = req.query_params.get('w') # client will need to give 'w' param
        # jp.Div(a=wp, text=word.title())
        # --- return data as text instead of division element
        # wp.html = word
        # --- retuen actual definition of the word
        definition = Definition(word).get()
        definition = " ".join(definition)
        # wp.html = definition
        # --- returning json response
        response = {
            'word': word,
            'definition': definition
        }
        wp.html = json.dumps(response)
        # ---
        return wp
'''
When server starts & user visits this particular url - /api, 
serve method is executed. The serve method creates webpage & the tries
to access 'query_params' object which is an attribute of req object &
the tries to call get method of this particular object & the get method
tries to get the value of 'w' parameter, hence client needs to mention 
this parameter in url. The paramter that client enters in url is stored 
in variable 'word' that we created which can used for further processing.

The problem with above is that if you inspect the webpage, you'll see a
lot of unnecessary js & html code. We want to serve clean data to client
& not all this unnecessary data. Btw we get that code because we used 
division. We need to only return text.

To do this, we access the html property of the wp variable of webpage
instance & set value for that as word

json is the standard format to return the data via api
'''
jp.Route('/api', Api.serve)
jp.justpy()