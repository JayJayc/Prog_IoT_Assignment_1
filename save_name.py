import sqlite3


def getInput():
    name = input("Add phone's name to raspberry pi's database: ")
    return name


def setName(user_name):
    query = """INSERT INTO NAMES ('name') values ('%s')"""
    dbname = "names.db"
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    try:
        curs.execute(query % (user_name))
    except ValueError:
        print('Non-numeric data found in the file.')
    except TypeError:
        print('a type error has occurred')

    conn.commit()
    conn.close()


def main():
    setName(getInput())


main()
