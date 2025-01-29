import sqlite3

class Card:
    ''' This class represents User'''

    database = 'banking.db'

    def __init__(self, card_type, card_number, cvc, card_holder_name):
        self.card_type = card_type
        self.card_number = card_number
        self.cvc = cvc
        self.card_holder_name = card_holder_name

    def validate(self):
        """Check if the entered card details are valid"""

        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT 1 FROM Card
                WHERE card_number = ? AND cvc = ? AND card_type = ? AND card_holder_name = ?
            ''', (self.card_number, self.cvc, self.card_type, self.card_holder_name))
            
            result = cursor.fetchone()
            return result is not None