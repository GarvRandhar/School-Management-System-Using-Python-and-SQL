# School Management System

This Python-based School Management System provides an interactive console application to manage student records. The system includes functionalities for user signup, login, adding, displaying, updating, searching, and deleting student information.

## Features

### 1. Signup and Login
- Users can create accounts with a username and password.
- Login functionality ensures secure access.

### 2. Student Management
- Add student details including name, gender, date of birth, contact, address, stream, and additional subjects.
- View all student records in a tabular format using PrettyTable.
- Update existing student records.
- Search for students by name.
- Delete student records.

### 3. Validation
- Ensures proper data entry for numeric fields, contact numbers, and dates.

### 4. Logging
- Logs user activities such as signup, login, addition, deletion, updates, and searches into `app.log`.

### 5. Database Management
- Uses MySQL to store user and student data.
- Automatically creates necessary tables (signup and data) if they do not exist.

## Python Libraries
- **mysql.connector**: To connect to the MySQL database.
- **PrettyTable**: For formatting and displaying table data.
- **logging**: For activity logging.
- **datetime**: For date validation and manipulation.
- **re**: For regex-based validation.

---

## Setup Instructions

### Prerequisites
1. **Python**: Make sure Python is installed on your machine (version 3.6 or above).
2. **MySQL**: Install MySQL Server and create a database for this application.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/GarvRandhar/School-Management-System-Using-Python-and-SQL.git
   ```
2. Navigate into the project directory:
   ```bash
   cd School-Management-System-Using-Python-and-SQL
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup
1. Open the MySQL terminal and create a database:
   ```sql
   CREATE DATABASE school_management;
   ```
2. Update the database credentials in the Python script (e.g., `School_mgmt.py`) to match your MySQL setup.

### Running the Application
1. Execute the Python script to launch the application:
   ```bash
   python School_mgmt.py
   ```

---

## Usage Examples

1. **Signup and Login**
   - Use `signup()` to create a new account.
   - Log in with existing credentials to access the main menu.

2. **Main Menu Options**
   - **Add Student Details**: Input the student's details, ensuring validation for numeric fields, contact numbers, and dates.
   - **Show All Records**: Displays all student records in a formatted table.
   - **Delete a Record**: Remove a student record by entering their `StudentId`.
   - **Update a Record**: Modify an existing student's details.
   - **Search a Record**: Search for students by name and view their details.
   - **Exit**: Exit the application and log the activity.

---

## Project Roadmap

### Phase 1: Core Functionalities
- [x] Implement user signup and login.
- [x] Add, update, delete, and search student records.
- [x] Log user activities.

### Phase 2: Enhancements
- [ ] Add role-based access control (e.g., admin, teacher, student).
- [ ] Implement attendance tracking and report card generation.
- [ ] Enhance validation for user inputs.

### Phase 3: User Interface
- [ ] Develop a graphical user interface (GUI) using frameworks like Tkinter or PyQt.
- [ ] Add support for exporting data to CSV or Excel.

---

## Logging
All user actions are logged in `app.log`, including:
- User signup and login activities.
- Addition, deletion, and updates to records.
- Search queries.

---

## License
This project is open-source. Feel free to modify and use it as per your requirements.
