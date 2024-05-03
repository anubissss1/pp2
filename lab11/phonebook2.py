import psycopg2

conn = psycopg2.connect(database="defense", user="checker", password="qwerty")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS phonebook1
 (
                number_id SERIAL PRIMARY KEY,
                full_name VARCHAR(100),
                phone_number VARCHAR(20)
            )''')
conn.commit()

cur.execute('''
    CREATE OR REPLACE PROCEDURE delete_from_data(
        delete_key VARCHAR
    ) AS
    $$
    BEGIN
        DELETE FROM phonebook1
         WHERE full_name = delete_key OR phone_number = delete_key;
    END;
    $$ LANGUAGE plpgsql;
''')
conn.commit()

"""
cur.execute("CALL delete_from_data('gleb')")
conn.commit()
"""


cur.execute('''
    CREATE OR REPLACE FUNCTION search_records(pattern TEXT) RETURNS SETOF phonebook1
     AS
    $$
    BEGIN
        RETURN QUERY SELECT * FROM phonebook1
         WHERE
            full_name ILIKE '%' || pattern || '%' OR
            phone_number ILIKE '%' || pattern || '%';
    END;
    $$ LANGUAGE plpgsql;
''')
conn.commit()

cur.execute("SELECT search_records('Sasha')")
rows = cur.fetchall()
for row in rows:
    print(row)


cur.execute('''
    CREATE OR REPLACE FUNCTION get_records_with_pagination(
        limit_val INT,
        offset_val INT
    ) RETURNS SETOF phonebook1
     AS
    $$
    BEGIN
        RETURN QUERY SELECT * FROM phonebook1
         LIMIT limit_val OFFSET offset_val;
    END;
    $$ LANGUAGE plpgsql;
''')

"""
cur.execute("SELECT get_records_with_pagination (10, 0)")
rows = cur.fetchall()
for row in rows:
    print(row)
"""
cur.close()
conn.close()