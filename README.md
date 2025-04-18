Description
This is a simple and user-friendly web application designed to help users manage their tasks efficiently. The application allows users to create, edit, delete, and mark tasks as completed. Built using Flask, it incorporates Bootstrap for a responsive design and integrates several Flask extensions to enhance its functionality.

Features
Add New Tasks: Create tasks with descriptions and optional due dates.

Edit Tasks: Modify task details, including their description and deadline.

Mark as Completed: Track task completion status with a toggle.

Dynamic Date Handling: Automatically disables date fields unless a task is marked as completed.

Interactive Calendar: Uses Flatpickr for date and time selection.

Authentication: User login/logout to secure personal tasks (if implemented).

Responsive UI: Built with Bootstrap for a seamless user experience across devices.

Technologies Used
Backend: Flask, Flask-SQLAlchemy, Flask-Migrate

Frontend: Bootstrap, Flatpickr

Additional Extensions:

Flask-WTF for form handling

Flask-Login for user session management

Flask-CKEditor for enhanced text input (if required)

Database: SQLite (or others via SQLAlchemy)

Environment Configuration: Python-dotenv for environment variable management

Installation and Setup
Clone this repository:

bash
git clone https://github.com/your-username/todolist.git
cd todolist
Create a virtual environment and activate it:

bash
python -m venv venv
source venv/bin/activate   # Linux/MacOS
venv\Scripts\activate      # Windows
Install the dependencies:

bash
pip install -r requirements.txt
Configure environment variables:

Create a .env file in the root directory.

Environment Variables
This application relies on certain environment variables to configure sensitive information. These variables should be stored in a .env file located in the root directory of the project. Below is an example of how the .env file should be structured:

plaintext
MY_EMAIL=your_email@example.com
MY_PASSWORD=your_email_password
SECRET_KEY=your_secret_key
Description of Environment Variables:
MY_EMAIL: The email address the application will use for features such as sending notifications. Replace your_email@example.com with your actual email address.

MY_PASSWORD: The password associated with MY_EMAIL. Replace your_email_password with the password for the email account.

SECRET_KEY: A unique and secure key required by Flask for cryptographic operations (e.g., session cookies). Replace your_secret_key with a strong random value.

Add the following:

dotenv
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
Initialize the database:

bash
flask db init
flask db migrate
flask db upgrade
Run the application:

bash
flask run
Open the application in your browser at http://127.0.0.1:5000.

Usage
Navigate through the interface to add, edit, or delete tasks.

Toggle the completion status of tasks.

Use the calendar to pick deadlines for tasks easily.

Folder Structure
todolist/
│
├── migrations/         # Database migrations
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
├── app.py              # Main application script
├── config.py           # Configuration settings
├── models.py           # Database models
├── forms.py            # Flask-WTF forms
├── .env                # Environment variables
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
Future Enhancements
Add user registration and authentication to secure tasks.

Implement categories or labels for better task organization.

Allow users to set reminders for tasks.

Add drag-and-drop task prioritization.

License
This project is open-source and available under the MIT License.