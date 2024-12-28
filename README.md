# School Management System
This Python-based School Management System provides an interactive console application to manage student records. The system includes functionalities for user signup, login, adding, displaying, updating, searching, and deleting student records.

## Features

**1. Signup and Login:**

Users can create accounts with a username and password.

Login functionality ensures secure access.

**2. Student Management:**

Add student details including name, gender, date of birth, contact, address, stream, and additional subject.

View all student records in a tabular format using PrettyTable.

Update existing student records.

Search for students by name.

Delete student records.

**3. Validation:**

Ensures proper data entry for numeric fields, contact numbers, and dates.

**4. Logging:**

Logs user activities such as signup, login, addition, deletion, updates, and searches into app.log.

**5. Database Management:**

Uses MySQL to store user and student data.

Automatically creates necessary tables (signup and data) if they do not exist.

## Python Libraries:

mysql.connector: To connect to the MySQL database.

PrettyTable: For formatting and displaying table data.

logging: For activity logging.

datetime: For date validation and manipulation.

re: For regex-based validation.

## Functionality Overview

**Signup and Login**

Use signup() to create a new account.

Log in with existing credentials to access the main menu.

**Main Menu Options**

*Add Student Details:*

Input the student's details.

Validates numeric fields, contact numbers, and dates.

*Show All Records:*

Displays all student records in a formatted table.

*Delete a Record:*

Remove a student record by entering their StudentId.

*Update a Record:*

Update a student's StudentId.

*Search a Record:*

Search for students by name and view their details.

*Exit:*

Exit the application and log the activity.

## Logging
All user actions are logged in app.log, including:

User signup and login activities.

Addition, deletion, and updates to records.

Searched queries.

## License
This project is open-source. Feel free to modify and use it as per your requirements.
