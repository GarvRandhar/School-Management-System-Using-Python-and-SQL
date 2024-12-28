import logging
from prettytable import PrettyTable
import mysql.connector as sql
from datetime import datetime
import re

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

con = sql.connect(host='localhost', user='root', passwd='your_passwd', database='School_Management')
mycur = con.cursor()
mycur.execute("create table if not exists signup(username varchar(30), password varchar(255))")
mycur.execute("create table if not exists data(StudentId int primary key, name varchar(50), fname varchar(50), gender varchar(10), date_of_birth date, contact bigint, address varchar(100), stream varchar(50), additional_sub varchar(50))")

def validate_date(date_text):
    try:
        return datetime.strptime(date_text, "%Y%m%d")
    except ValueError:
        print("Invalid date format. Use YYYYMMDD.")
        return None

def validate_numeric(input_text):
    if input_text.isdigit():
        return int(input_text)
    else:
        print("Invalid input. Please enter numeric values.")
        return None

def validate_contact(contact):
    if re.fullmatch(r"\d{10}", contact):
        return int(contact)
    else:
        print("Invalid contact number. Must be 10 digits.")
        return None

def signup():
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
    mycur.execute("insert into signup (username, password) values (%s, %s)", (username, password))
    con.commit()
    logging.info(f"New user signed up: {username}")
    print("Signup successful.")

def login():
    username = input("USERNAME: ")
    mycur.execute("select username from signup where username = %s", (username,))
    user = mycur.fetchone()
    if user:
        print(">>>>VALID USERNAME<<<<")
        password = input("PASSWORD: ")
        mycur.execute("select password from signup where username = %s and password = %s", (username, password))
        if mycur.fetchone():
            logging.info(f"User logged in: {username}")
            print("======= LOGIN SUCCESSFUL =======")
            return True
        else:
            print("Incorrect password.")
            logging.warning(f"Failed login attempt for user: {username}")
    else:
        print("Invalid username.")
        logging.warning(f"Failed login attempt with invalid username: {username}")
    return False

def add_data():
    while True:
        student_id = validate_numeric(input("Enter Student Id Number: "))
        if not student_id:
            continue
        name = input("Enter The Name Of The Student: ")
        fname = input("Enter Father's Name: ")
        gender = input("Enter Gender (Male/Female): ")
        date_of_birth = validate_date(input("Enter Date Of Birth (YYYYMMDD): "))
        if not date_of_birth:
            continue
        contact = validate_contact(input("Enter Contact Number: "))
        if not contact:
            continue
        address = input("Enter Address: ")
        stream = input("Enter Stream: ")
        additional_sub = input("Enter Additional Subject (C.S./Physical Education): ")
        
        mycur.execute("""
            insert into data (StudentId, name, fname, gender, date_of_birth, contact, address, stream, additional_sub) 
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (student_id, name, fname, gender, date_of_birth, contact, address, stream, additional_sub))
        con.commit()
        logging.info(f"Added student record: {student_id} - {name}")
        print("Record added successfully.")

        ch = input("Do you want to add more? (y/n): ").lower()
        if ch == 'n':
            break

def show():
    mycur.execute("select * from data")
    res = mycur.fetchall()
    if res:
        t = PrettyTable(['StudentId', 'name', 'fname', 'gender', 'date_of_birth', 'contact', 'address', 'stream', 'additional_sub'])
        for row in res:
            t.add_row(row)
        print(t)
        logging.info("Displayed all student records.")
    else:
        print("No records found.")

def remove_stud():
    student_id = validate_numeric(input("Enter The StudentId Of The Student To Be Deleted: "))
    if not student_id:
        return
    mycur.execute("delete from data where StudentId = %s", (student_id,))
    con.commit()
    if mycur.rowcount > 0:
        logging.info(f"Deleted student record: {student_id}")
        print("Record deleted successfully.")
    else:
        print("No record found with the given StudentId.")

def update():
    old_id = validate_numeric(input("Enter The Old StudentId: "))
    if not old_id:
        return
    new_id = validate_numeric(input("Enter The New StudentId: "))
    if not new_id:
        return
    mycur.execute("update data set StudentId = %s where StudentId = %s", (new_id, old_id))
    con.commit()
    if mycur.rowcount > 0:
        logging.info(f"Updated StudentId from {old_id} to {new_id}")
        print("Record updated successfully.")
    else:
        print("No record found with the given Old StudentId.")

def search():
    name = input("Enter Student Name To Be Searched: ")
    mycur.execute("select * from data where name = %s", (name,))
    data = mycur.fetchall()
    if data:
        t = PrettyTable(['StudentId', 'name', 'fname', 'gender', 'date_of_birth', 'contact', 'address', 'stream', 'additional_sub'])
        for row in data:
            t.add_row(row)
        print(t)
        logging.info(f"Searched student record by name: {name}")
    else:
        print("No records found for the given name.")

def main_menu():
    while True:
        print("\n\t=========================>>> D.P.S INTERNATIONAL <<<=========================")
        print("\n     Press 1 To Add Student Detail")
        print("     Press 2 To Show All Records")
        print("     Press 3 To Delete A Record")
        print("     Press 4 To Update A Record")
        print("     Press 5 To Search A Record")
        print("     Press 6 To Exit.")
        choice = input("Enter Your Choice: ")
        if choice == '1':
            add_data()
        elif choice == '2':
            show()
        elif choice == '3':
            remove_stud()
        elif choice == '4':
            update()
        elif choice == '5':
            search()
        elif choice == '6':
            print("Thank you! Exiting...")
            logging.info("Application exited.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if login():
        main_menu()
    else:
        print("Login failed. Exiting...")
