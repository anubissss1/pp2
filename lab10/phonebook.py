import psycopg2
import csv
conn = psycopg2.connect(database = "defense", user = "checker", password = "qwerty")

cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS phonebook1 (
                number_id SERIAL PRIMARY KEY,
                full_name VARCHAR(100),
                phone_number VARCHAR(20)
            )''')
conn.commit()

def insert_data_from_csv():
    with open('dataforphonebook.csv', 'r', encoding='UTF-8') as f:
        cur.copy_from(f, 'phonebook1', sep=',')
        conn.commit()
insert_data_from_csv()      

def insert_data_from_console():
    number_id = input("Enter id: ")
    full_name = input("Enter full name: ")
    phone_number = input("Enter phone number: ")
    cur.execute(
        "INSERT INTO phonebook1 (number_id, full_name, phone_number) VALUES (%s, %s, %s)",
        (number_id, full_name, phone_number)
    )
    conn.commit()

def updating_data():
    cur.execute("UPDATE phonebook1 SET phone_number = '+7 705 133 1223' WHERE number_id = '2';")
    conn.commit()

def select_from_data():
    cur.execute("SELECT phone_number FROM phonebook1 WHERE number_id ='3';")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_from_data():
    cur.execute("DELETE FROM phonebook1 WHERE number_id = '2';")
    conn.commit()

cur.close()
conn.close()
