from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask # 'Flask' is a class/object type that represents a webapp
from flask import render_template # render_template is a function - helps you connect your app to external html files
from flask import request # request is used for getting the data that user inputs
from flatmates_bill import flat
from flatmates_bill import reports

# Method view is a class-based view that dispatches request methods to the corrosponding 
# class methods. Ex: if you implement a 'get' method, it will be used to handle 'GET' requests

# With flask you can also make pages/views with functions but that's not the
# best way to structure web apps

# request is a request (to our server) from a visitor when they visit a url 

# we will have to connnect classes with urls, to do that we create an app instance

app = Flask(__name__) # name is a variable, it contains string of current python file, so 'main.py'
                      # Flask class is instansiated

class HomePage(MethodView):

    def get(self): # -> get method will be implement GET request.. so when someone goes to 
                   # this class object (HomePage) - they will se what we define here
        
        # return '<h2>Hello</h2>' -> rather than adding html here (not good practice), we create templates 
        # folder in this dir and create html files to call here
        return render_template('index.html') 
        # we did not write ./templates/index.html because flask knows html templates will be in templates 
        # folder of current directory

class BillFormPage(MethodView):

    def get(self):

        bill_form = BillForm() # The BillForm class gets initialized here 
        #return 'I am bill form page'
        return render_template('bill_form_page.html', 
                               bill_form=bill_form) 
        # in the second arg of render_template, we are assiging the value to
        # variable in html template 


class ResultPage(MethodView):

    '''
    def get(self):
        billform = BillForm(request.form)
        amount = billform.amount.data
        return amount

    Like above, we cannot write get method to display the data that user has entered.
    Because, when we visit the result page through clicking calculate, 
    that is post request so we need a post method for implementing this 

    ! Its imp to remember that when you are writing a post method here, in form
    tag, after the action property, you need to method="post" otherwise error will 
    be thrown that this method is not allowed
    '''

    def post(self):
        billform = BillForm(request.form)

        # Take inputs for Bill Instance 
        bill_amount = billform.amount.data
        bill_period_name = billform.period_name.data
        bill_days = billform.days

        # Take inputs for flatmate 1
        flatmate1_name = billform.name1.data
        flatmate1_days_in_house = billform.days_in_house1.data

        # Take inputs for flatmate 2
        flatmate2_name = billform.name2.data
        flatmate2_days_in_house = billform.days_in_house2.data

        # Take inputs for PDF Report
        bill_file_name = billform.file_name.data

        bill = flat.Bill(bill_amount, bill_days, bill_period_name)
        flatmate1 = flat.Flatmate(flatmate1_name, flatmate1_days_in_house)
        flatmate2 = flat.Flatmate(flatmate2_name, flatmate2_days_in_house)
        # print(f'{flatmate1_name} pays {flatmate1.pay(bill, flatmate2)}')
        # print(f'{flatmate1_name} pays {flatmate2.pay(bill, flatmate1)}')
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        reports.PdfReport(bill_file_name).generatePDF(pdf, flatmate1, flatmate2, bill)

        return f'{flatmate1_name} pays {flatmate1.pay(bill, flatmate2)} & {flatmate1_name} pays {flatmate2.pay(bill, flatmate1)}'

class BillForm(Form):

    # we will have to initialize this class - in BillFormPage() class
    # rather than creating the form with htnl, we will create it here
    amount = StringField("Bill Amount: ") # StringField class is instansiated
    # above way adds lablel as well as input field
    period_name = StringField("Bill Period: ")
    days = StringField("Days in period: ")

    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in house: ")

    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in house: ")

    file_name = StringField("Name of the Bill: ")

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('HomePage')) # '/' is root. as_view is method 
# of MethodView class -> here we specify the name of the view and it is good practice to keep 
# view name same as class name

# normally by default flask was designed for functions, if HomePage were a function, we would
# not have writted .as_view after it, but since its a class we are telling flask to treat it as 
# a view function

app.add_url_rule('/bill', view_func=BillFormPage.as_view('BillFormPage'))
app.add_url_rule('/result', view_func=ResultPage.as_view('ResultPage'))

app.run(debug=True) # we do debug = True so when we do code changes they reflect in app in real time 
                    # rather than having to close and start the app again

# python ./main.py