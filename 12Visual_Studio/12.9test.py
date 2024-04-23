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
    name = input('Enter name: ')
    id = input('Enter id: ')
    age = input('Enter age: ')
    query = '''insert into employees(Name,ID,Age) values(%s,%s,%s);'''
    cursor.execute(query,(name,id,age))
    print('Data added successfully')

    conn.commit()
    conn.close()

data()

# def extract():
#     conn = psycopg2.connect(dbname="postgres",user="postgres",password="root",host="localhost",port="5432")

#     cursor = conn.cursor()
#     cursor.execute('''select * from employees;''')
#     #print(cursor.fetchone())
#     show = cursor.fetchone()
#     #print(show[0])
#     #print(show[1])
#     print(show[2])

#     conn.commit()
#     conn.close()

# extract()