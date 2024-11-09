from fpdf import FPDF
import webbrowser

class Bill:
    '''
    This represents the Bill object
    '''

    def __init__(self, amount, period, period_name):
        self.amount = amount
        self.period = period
        self.period_name = period_name


class Flatmate:
    '''
    This class represents a flatmate
    '''

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pay(self, bill, other_flatmate):
        total_bill_amount = bill.amount 
        flatmate_days_in_house = self.days_in_house
        other_flatmate_days_in_house = other_flatmate.days_in_house
        bill_contribution_percentage = flatmate_days_in_house/(flatmate_days_in_house+other_flatmate_days_in_house)
        bill_to_pay = total_bill_amount*bill_contribution_percentage
        return bill_to_pay

class PdfReport:
    '''
    This class represents the PdfReport that needs to be generated
    '''

    def __init__(self, filename):
        self.filename = filename
        
    def generatePDF(self, pdf, flatmate1, flatmate2, bill):
        '''
        A method to generate a pdf
        '''
        # Adding page
        pdf.add_page()

        # Adding house image
        pdf.image('files/house.png', w=30, h=30)
        
        # Adding header and header format
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=0, align='C', ln=1)

        # Adding an empty cell
        pdf.cell(w=0, h=20, txt='', border=0, ln=1)
        
        # Adding further content
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=200, h=40, txt='Period', border=0)
        pdf.cell(w=200, h=40, txt=f'{bill.period_name}', border=0, ln=1)

        # Adding an empty cell
        pdf.cell(w=0, h=20, txt='', border=0, ln=1)

        # Adding details in bill
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=200, h=40, txt='Name', border=0)
        pdf.cell(w=200, h=40, txt='Total Amount', border=0, ln=1)
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=200, h=40, txt=f'{flatmate1.name}', border=0)
        pdf.cell(w=200, h=40, txt=f'{round(flatmate1.pay(bill, flatmate2), 2)}', border=0, ln=1)
        pdf.cell(w=200, h=40, txt=f'{flatmate2.name}', border=0)
        pdf.cell(w=200, h=40, txt=f'{round(flatmate2.pay(bill, flatmate1), 2)}', border=0, ln=1)
        
        pdf.output(f'{self.filename}.pdf')

        webbrowser.open(f'{self.filename}.pdf')


nov_bill = Bill(500, 30, 'November 2025')
pratik = Flatmate(name='Pratik', days_in_house=25)
shraddha = Flatmate(name='shraddha', days_in_house=30)
pratik_contribution = pratik.pay(nov_bill, shraddha)
shraddha_contribution = shraddha.pay(nov_bill, shraddha)
pdf = FPDF(orientation='P', unit='pt', format='A4')
PdfReport('Nov2025Bill').generatePDF(pdf, pratik, shraddha, nov_bill)