import webbrowser
import os

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
        
        # Change the dir to save file
        os.chdir('files ')
        
        # Save the output file
        pdf.output(f'{self.filename}.pdf')

        # Open the file
        webbrowser.open(f'{self.filename}.pdf')