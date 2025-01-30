
import create_databases
import os
from card import Card
from user import User
from ticket import Ticket
from seat import Seat

# create databases if they do not exist
create_databases.create_db_if_not_exists('cinema.db')
create_databases.create_db_if_not_exists('banking.db')

# create tables if they do not exist
create_databases.create_seat()
create_databases.create_card()

# populate tables if they are empty
if not create_databases.check_if_records_exists('cinema.db', 'Seat'):
    create_databases.populate_seat()

if not create_databases.check_if_records_exists('banking.db', 'Card'):
    create_databases.populate_card()

# implement core logic

if __name__ == "__main__":

    # taking inputs
    name = input('Your full name: ')
    seat_number = input('Preferred seat number: ')
    card_type = input('Your card type: ')
    card_number = int(input('Your card_number: '))
    cvc = int(input('Your cvc: '))
    card_holder_name = input('card_holder_name: ')

    # Instansiating objects
    card = Card(card_type=card_type, card_number=card_number,
                cvc=cvc, card_holder_name=card_holder_name)
    seat = Seat(seat_number=seat_number)
    user = User(name=name)

    print(user.buy(seat=seat, card=card))