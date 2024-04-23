import psycopg2
def table():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="root",host="localhost",port="5432")

    cursor = conn.cursor()
    cursor.execute('''create table employees(Name Text, ID int, Age int);''')
    print('Table created successfully')

    conn.commit()
    conn.close()

def data():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="root",host="localhost",port="5432")

    cursor = conn.cursor()
    cursor.execute('''insert into employees(Name,ID,Age) values('Sam', 01, 30);''')
    print('Data added successfully')

    conn.commit()
    conn.close()

data()