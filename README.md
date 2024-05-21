# Blood Donation Application

This is a blood donation application. In this application, people can search for a particular blood group, post requests for blood in urgent need, and other users can comment, reply, and share information. Only registered users will get full access to the application.

## Technologies Used

- **Programming Language**: Python
- **Designing**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Framework**: Django, Django Rest Framework
- **IDE**: PyCharm, Visual Studio Code

## Features

- Search for a particular blood group
- Post requests for urgent blood needs
- Comment, reply, and share information
- Full access for registered users

## Installation and Setup

To start the application on your local server, follow these steps:

### Step 1: Create Virtual Environment
Open a command line interface (VS Code terminal or any command line tool) and run the following commands:

```bash
# Create Virtual Environment:
# --------------------------------
python -m pip install virtualenv
python -m venv venv
venv\Scripts\activate

# Now run the commands:
# ---------------------
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
