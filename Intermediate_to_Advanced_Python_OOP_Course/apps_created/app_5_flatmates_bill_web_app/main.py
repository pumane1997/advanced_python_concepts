from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask 
from flask import render_template 
from flask import request 
from flat import Bill, Flatmate
from reports import PdfReport, FileSharer
from fpdf import FPDF

app = Flask(__name__) 

class HomePage(MethodView):

    def get(self):
        return render_template('index.html') 


class BillFormPage(MethodView):

    def get(self):

        bill_form = BillForm() 
        return render_template('bill_form_page.html', 
                               bill_form=bill_form) 

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

        return render_template('bill_form_page.html',
                                result = True, 
                                bill_form=billform,
                                name1 =  flatmate1_name,
                                name2 =  flatmate2_name,
                                amount1 = flatmate1.pay(bill, flatmate2),
                                amount2 = flatmate2.pay(bill, flatmate1),
                                link = cloud_invoice_link)

        


class ResultPage(MethodView):

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

    amount = StringField("Bill Amount: ", default='100') 
    period_name = StringField("Bill Period: ", default='November 2024')
    days = StringField("Days in period: ", default='30')
    name1 = StringField("Name: ", default='Pratik')
    days_in_house1 = StringField("Days in house: ", default='21')
    name2 = StringField("Name: ", default='Shraddha')
    days_in_house2 = StringField("Days in house: ", default='15')
    file_name = StringField("Name of the Bill: ", default='Nov2024Bill')
    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('HomePage'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('BillFormPage'))
app.add_url_rule('/result', view_func=ResultPage.as_view('ResultPage'))

app.run(debug=True) 

# python ./main.py