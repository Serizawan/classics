import sqlite3

def main():
    try:
        con = sqlite3.connect('test.db')
        cur = con.cursor()
        cur.executescript("""DROP TABLE IF EXISTS pets;
                             CREATE TABLE pets(Id INT, Name TEXT, price INT);
                             INSERT INTO pets VALUES(1, "Cat", 400);
                             INSERT INTO pets VALUES(2, "Dog", 600);""")

        pets = ((3, 'Rabbit', 200),
                (4, 'Bird', 60),
                (5, 'Goat', 500))

        cur.executemany('INSERT INTO pets VALUES(?, ?, ?)', pets)

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
