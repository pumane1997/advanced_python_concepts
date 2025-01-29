import webbrowser
import os
from fpdf import FPDF

class Ticket:
    ''' This class represents Ticket'''

    def __init__(self, ticket_number, user, price, seat):
        self.ticket_number = ticket_number
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self):
        '''
        A method to generate a ticket
        '''
        pdf = FPDF(orientation='P', unit='pt', format='A4')

        # Adding page
        pdf.add_page()

        # Adding header and header format
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Ticket', border=0, align='C', ln=1)

        # Adding an empty cell
        pdf.cell(w=0, h=20, txt='', border=0, ln=1)
        
        # Adding Ticket Number
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=200, h=40, txt='Ticket Number', border=0)
        pdf.cell(w=10, h=40, txt='', border=0)
        pdf.cell(w=200, h=40, txt=f'{self.ticket_number}', border=0, ln=1)

        # Adding an empty cell
        pdf.cell(w=0, h=20, txt='', border=0, ln=1)

        # Adding User
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=200, h=40, txt='Name', border=0)
        pdf.cell(w=10, h=40, txt='', border=0)
        pdf.cell(w=200, h=40, txt=f'{self.user}', border=0, ln=1)

        # Adding an empty cell
        pdf.cell(w=0, h=20, txt='', border=0, ln=1)

        # Adding Price
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=200, h=40, txt='Price', border=0)
        pdf.cell(w=10, h=40, txt='', border=0)
        pdf.cell(w=200, h=40, txt=f'{self.price}', border=0, ln=1)

        # Adding an empty cell
        pdf.cell(w=0, h=20, txt='', border=0, ln=1)

        # Adding Seat
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=200, h=40, txt='Seat', border=0)
        pdf.cell(w=10, h=40, txt='', border=0)
        pdf.cell(w=200, h=40, txt=f'{self.seat}', border=0, ln=1)

        # Adding an empty cell
        pdf.cell(w=0, h=20, txt='', border=0, ln=1)






        # Change the dir to save file
        os.chdir('tickets')

        # Save the output file
        pdf.output(f'{self.ticket_number}.pdf')

        # Open the file
        webbrowser.open(f'{self.ticket_number}.pdf')


#---------------

my_ticket = Ticket('ADWPNCSDU78', 'John Doe', 10, 'A1')

my_ticket.to_pdf()