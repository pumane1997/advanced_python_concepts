import sqlite3

class Seat:
    ''' This class represents a Seat in the cinema'''

    database = 'cinema.db'

    def __init__(self, seat_number):
        self.seat_number = seat_number

    def get_price(self):
        """Fetch the price of this seat from the database"""
        
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT price
                FROM Seat
                WHERE seat_number = ?
            ''', (self.seat_number,))  # Use tuple instead of list for safety
            
            result = cursor.fetchone()  # Fetch a single result
            return result[0] if result else None  # Return the price or None if not found

    def is_free(self):
        """Check if the seat is available"""

        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT is_taken
                FROM Seat
                WHERE seat_number = ?
            ''', (self.seat_number,))
            
            result = cursor.fetchone()
            return True if result[0] == 1 else False

    def occupy(self):
        """Mark the seat as occupied"""

        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE Seat
                SET is_taken = 1
                WHERE seat_number = ?
            ''', (self.seat_number,))
            connection.commit()


#----

# print(Seat('A1').get_price())