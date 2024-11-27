from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask # 'Flask' is a class/object type that represents a webapp
from flask import render_template # render_template is a function - helps you connect your app to external html files
from flask import request # request is used for getting the data that user inputs
from flat import Bill, Flatmate
from reports import PdfReport, FileSharer
from fpdf import FPDF

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
        bill_amount = int(billform.amount.data)
        bill_period_name = billform.period_name.data
        bill_days = int(billform.days.data)

        # Take inputs for flatmate 1
        flatmate1_name = billform.name1.data
        flatmate1_days_in_house = int(billform.days_in_house1.data)

        # Take inputs for flatmate 2
        flatmate2_name = billform.name2.data
        flatmate2_days_in_house = int(billform.days_in_house2.data)

        # Take inputs for PDF Report
        bill_file_name = billform.file_name.data

        # Processing the data
        bill = Bill(bill_amount, bill_days, bill_period_name)
        flatmate1 = Flatmate(flatmate1_name, flatmate1_days_in_house)
        flatmate2 = Flatmate(flatmate2_name, flatmate2_days_in_house)
        
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        PdfReport(bill_file_name).generatePDF(pdf, flatmate1, flatmate2, bill)

        cloud_invoice_link = FileSharer(f'{bill_file_name}.pdf').share()

        return render_template('results.html',
                                name1 =  flatmate1_name,
                                name2 =  flatmate2_name,
                                amount1 = flatmate1.pay(bill, flatmate2),
                                amount2 = flatmate2.pay(bill, flatmate1),
                                link = cloud_invoice_link)

class BillForm(Form):

    # we will have to initialize this class - in BillFormPage() class
    # rather than creating the form with htnl, we will create it here
    amount = StringField("Bill Amount: ", default='100') # StringField class is instansiated
    # above way adds lablel as well as input field
    # the second arg add default value. This is good for developmentg because you wont have to 
    # enter values for interating everytime 
    period_name = StringField("Bill Period: ", default='November 2024')
    days = StringField("Days in period: ", default='30')

    name1 = StringField("Name: ", default='Pratik')
    days_in_house1 = StringField("Days in house: ", default='21')

    name2 = StringField("Name: ", default='Shraddha')
    days_in_house2 = StringField("Days in house: ", default='15')

    file_name = StringField("Name of the Bill: ", default='Nov2024Bill')

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