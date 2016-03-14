import sqlite3

def main():
    try:
        con = sqlite3.connect('test.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE pets(Id INT, Name TEXT, price INT)')
        cur.execute('INSERT INTO pets VALUES(1, "Cat", 400)')
        cur.execute('INSERT INTO pets VALUES(2, "Dog", 600)')
        cur.execute('INSERT INTO pets VALUES(3, "Rabbit", 200)')
        cur.execute('INSERT INTO pets VALUES(4, "Bird", 60)')
        con.commit()

        cur.execute('SELECT * FROM pets')
        data = cur.fetchall()

        for row in data:
            print(row)

    except sqlite3.Error:
        if con:
            print('Error! Rolling back')
            con.rollback()
    finally:
        if con:
            con.close()

if __name__ == '__main__':
    main()
