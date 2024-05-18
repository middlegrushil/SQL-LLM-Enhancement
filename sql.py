import mysql.connector
connection=mysql.connector.connect("student")
##Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()
##Create the table
table_info = """create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)
##Insert some records
cursor.execute('''Insert Into STUDENT values('Leonard', 'Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Amy', 'Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Raj', 'Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Sheldon', 'DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Howard', 'DEVOPS','A',35)''')
# Insert additional records into the table
insert_statements = [
    "INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Penny', 'Data Science', 'A', 95)",
    "INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Bernadette', 'Data Science', 'B', 98)",
    "INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Stuart', 'Data Science', 'A', 88)",
    "INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Emily', 'Data Science', 'A', 92)",
    "INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Leslie', 'Data Science', 'B', 96)",
    "INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Zack', 'Data Science', 'A', 85)",
    "INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Priya', 'Data Science', 'B', 91)",
    "INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Bert', 'Data Science', 'A', 89)",
    "INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Barry', 'Data Science', 'A', 93)",
    "INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Wil', 'Data Science', 'B', 97)"
]

for insert_statement in insert_statements:
    cursor.execute(insert_statement)
##Display all the records
print("Inserted Records: ")
data = cursor.execute('''Select * From STUDENT''')
for row in data:
    print(row)
##Close the connection
connection.commit()
connection.close()