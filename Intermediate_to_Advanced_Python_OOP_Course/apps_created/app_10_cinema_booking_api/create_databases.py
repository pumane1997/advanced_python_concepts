
''' 
    We will create databases when there are no tables in the database
'''

def create_db_if_not_exists(db):
    '''xx'''

    import os
    import sqlite3

    if os.path.exists(db):
        pass
    else:
        connection = sqlite3.connect(db)

def check_if_table_exists(db, table):
    '''x'''

    import sqlite3
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' AND name=?
    """, (table,))
    table_exists = cursor.fetchone()
    return table_exists


def check_if_records_exists(db, table):
    '''x'''

    import sqlite3
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT COUNT(*) FROM {table}
        """)
    record_count = cursor.fetchone()[0]
    if record_count > 0:
        return True
    else:
        return False


def create_seat():
    ''' xx '''

    import sqlite3
    connection = sqlite3.connect('cinema.db')
    connection.execute('''
        CREATE TABLE IF NOT EXISTS "Seat" (
            "seat_id" INTEGER,
            "seat_number" TEXT,
            "is_taken"	INTEGER,
            "price"	REAL,
            PRIMARY KEY("seat_id")
        );
        ''')
    connection.commit()
    connection.close()


def create_card():
    ''' xx '''

    import sqlite3
    connection = sqlite3.connect('banking.db')
    connection.execute('''
        CREATE TABLE IF NOT EXISTS "Card" (
            "card_id" INTEGER,
            "user_name" TEXT,
            "card_type" TEXT,
            "card_number" INTEGER,
            "cvc" INTEGER,
            "card_holder_name" TEXT,
            "balance"	REAL,
            PRIMARY KEY("card_id")
        );
        ''')
    connection.commit()
    connection.close()


def populate_seat():
    '''xx'''
    import sqlite3
    connection = sqlite3.connect('cinema.db')
    connection.execute('''
        INSERT INTO Seat (seat_id, seat_number, is_taken, price) VALUES
            (1, 'A1', 0, 10.0),
            (2, 'A2', 1, 10.0),
            (3, 'A3', 0, 10.0),
            (4, 'A4', 1, 10.0),
            (5, 'B1', 0, 12.0),
            (6, 'B2', 0, 12.0),
            (7, 'B3', 1, 12.0),
            (8, 'B4', 0, 12.0),
            (9, 'C1', 0, 15.0),
            (10, 'C2', 1, 15.0);
        ''')
    connection.commit()
    connection.close()


def populate_card():
    '''xx'''
    import sqlite3
    connection = sqlite3.connect('banking.db')
    connection.execute('''
        INSERT INTO Card (card_id, user_name, card_type, card_number, cvc, card_holder_name, balance) VALUES
            (1, 'john_doe', 'Visa', 4111111111111111, 123, 'John Doe', 5000.0),
            (2, 'jane_smith', 'MasterCard', 5555555555554444, 456, 'Jane Smith', 7500.0),
            (3, 'alice_jones', 'Visa', 4012888888881881, 789, 'Alice Jones', 3000.0),
            (4, 'bob_brown', 'Discover', 6011111111111117, 321, 'Bob Brown', 4500.0),
            (5, 'chris_white', 'Amex', 371449635398431, 111, 'Chris White', 6000.0),
            (6, 'ella_black', 'Visa', 4000123456789010, 222, 'Ella Black', 12000.0),
            (7, 'frank_green', 'MasterCard', 5200000000000007, 333, 'Frank Green', 8000.0),
            (8, 'grace_young', 'Visa', 4111222233334444, 444, 'Grace Young', 5500.0),
            (9, 'harry_adams', 'Discover', 6011556448578945, 555, 'Harry Adams', 4000.0),
            (10, 'irene_clark', 'Amex', 378282246310005, 666, 'Irene Clark', 10000.0);
        ''')
    connection.commit()
    connection.close()



