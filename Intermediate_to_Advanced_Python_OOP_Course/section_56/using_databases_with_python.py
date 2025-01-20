
def execute_query(db_path, query):
    '''
    x
    '''
    import sqlite3
    connection = sqlite3.connect(db_path)
    connection.execute(query)
    connection.commit()
    connection.close()

def create_table():
    '''
    x
    '''
    import sqlite3
    connection = sqlite3.connect('cinema.db')
    connection.execute('''
        CREATE TABLE "Seat" (
            "seat_id"	TEXT,
            "taken"	INTEGER,
            "price"	REAL,
            PRIMARY KEY("seat_id")
        );
        ''')
    connection.commit()
    connection.close()

def insert_records():
    '''
    x
    '''
    import sqlite3
    connection = sqlite3.connect('cinema.db')
    connection.execute('''
        INSERT INTO 'Seat' ("seat_id", "taken", "price")
        VALUES ('A1', 0, 90),
               ('A2', 0, 100),
               ('A3', 0, 80)
        ''')
    connection.commit()
    connection.close()

# insert_records()

def select_all():
    '''
    x
    '''
    import sqlite3
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT * FROM Seat
        ''')
    result = cursor.fetchall()
    connection.close()
    return result


def select_specific_columns():
    '''
    x
    '''
    import sqlite3
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT seat_id, price FROM Seat
        ''')
    result = cursor.fetchall()
    connection.close()
    return result

def select_with_condition():
    '''
    x
    '''
    import sqlite3
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute('''
        SELECT seat_id, price FROM Seat WHERE price < 100
        ''')
    result = cursor.fetchall()
    connection.close()
    return result

# print(select_all())
# print(select_specific_columns())
# print(select_with_condition())

def update_record(occupied, seat_id):
    '''
    x
    '''
    import sqlite3
    connection = sqlite3.connect('cinema.db')
    connection.execute('''
        UPDATE Seat
        SET taken = ?
        WHERE seat_id = ?
        ''', [occupied, seat_id])
    connection.commit()
    connection.close()


def delete_record():
    '''
    x
    '''
    import sqlite3
    connection = sqlite3.connect('cinema.db')
    connection.execute('''
        DELETE from Seat
        WHERE seat_id = 'A3'
        ''')
    connection.commit()
    connection.close()