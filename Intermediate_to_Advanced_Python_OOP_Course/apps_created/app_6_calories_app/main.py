from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask 
from flask import render_template 
from flask import request 
from temperature import TemperatureScrapper
from calories import CalorieCalculator

app = Flask(__name__) 

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')

class CaloriesFormPage(MethodView):

    def get(self):

        calorie_form = CaloriesForm() 
        return render_template('calories_form_page.html', 
                               calorie_form=calorie_form)

    def post(self):

        calorie_form = CaloriesForm()

        # Take user inputs for Calories Instance  

        weight = float(calorie_form.weight.data)
        height = float(calorie_form.height.data)
        age = float(calorie_form.age.data)
        gender = calorie_form.gender.data
        activity = float(calorie_form.weight.data)
        city = calorie_form.weight.data
        country = calorie_form.weight.data

        # Calculate temperature and maintainence calories

        temperature = TemperatureScrapper(city=city, country=country).getTemperature()
        maintainence_calories = CalorieCalculator(gender=gender, age=age, height=height, weight=weight, activity=activity, temperature=temperature).calculateCalories()
        print(temperature)

        return render_template('calories_form_page.html', 
                               calorie_form=calorie_form,
                               result = True,
                               maintainence_calories=maintainence_calories)

class CaloriesForm(Form):

    weight = StringField("Weight: ", default='74')
    height = StringField("Height: ", default='170')
    age = StringField("Age: ", default='28')
    gender = StringField("Gender: ", default='male')
    activity = StringField("Activity: ", default='2')
    city = StringField("City: ", default='pune')
    country = StringField("Country: ", default='india')
    button = SubmitField('Calculate')

app.add_url_rule('/', view_func=HomePage.as_view('HomePage'))   
app.add_url_rule('/calories', view_func=CaloriesFormPage.as_view('CaloriesFormPage'))

app.run(debug=True)

# python ./main.py