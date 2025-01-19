from definition import Definition
import justpy as jp
import json

class API:
    '''
        Handles requests at /api?w=word
    '''
    

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        definition = Definition(word).get()
        definition = " ".join(definition)
        response = {
            'word': word,
            'definition': definition
        }
        wp.html = json.dumps(response)
        return wp