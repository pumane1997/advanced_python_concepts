
class User:
    ''' This class represents User'''

    def __init__(self, name):
        self.name = name

    def buy(preferred_seat, card):
        pass


class Seat:
    ''' This class represents User'''

    database = 'cinema.db'

    def __init__(self, seat_id, price):
        self.seat_id = seat_id

    def get_price():
        pass

    def is_free():
        pass

    def occupy():
        pass

class Card:
    ''' This class represents User'''

    database = 'banking.db'

    def __init__(self, type, number, cvc, name):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.name = name

    def validate():
        pass

class Ticket:
    ''' This class represents User'''

    def __init__(self, ticket_number, user, price, seat):
        self.ticket_number = ticket_number
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf():
        pass