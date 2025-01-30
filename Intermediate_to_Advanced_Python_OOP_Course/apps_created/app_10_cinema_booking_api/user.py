from ticket import Ticket

class User:
    ''' This class represents User'''

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        if seat.is_free():
            if card.validate(): 
                seat.occupy()
                ticket = Ticket(user=self.name, price=seat.get_price(), seat=seat)
                ticket.to_pdf()
                return 'Purchase Successful'
            else:
                print('The card details are wrong')
        else:
            print('The seat is taken')