from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask 
from flask import render_template 
from flask import request 

app = Flask(__name__) 

class HomePage(MethodView):

    def get(self):
        return render_template('index.html') 

app.add_url_rule('/', view_func=HomePage.as_view('HomePage'))   

app.run(debug=True)

# python ./main.py