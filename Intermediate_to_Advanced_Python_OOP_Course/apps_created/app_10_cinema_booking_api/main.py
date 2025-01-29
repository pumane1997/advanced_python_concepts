
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



