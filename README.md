# Todos_web

📋 README.md for todos_web

# 📝 Todos Web App

A simple web-based **ToDo List Application** built using **Flask**, **SQLite**, and **Bootstrap**.  
This app allows users to **Create**, **Read**, **Update**, and **Delete** (CRUD) todo tasks.

---

## 🚀 Features

- Add a new Todo with title & description
- View all todos in a Bootstrap-styled table
- Update existing todos
- Delete unwanted todos
- Stores all tasks using SQLite database
- Fully responsive with Bootstrap 5

---

## 🧱 Technologies Used

- [Flask](https://flask.palletsprojects.com/) - Python web framework
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - ORM for database
- [SQLite](https://www.sqlite.org/) - Lightweight database
- [Bootstrap 5](https://getbootstrap.com/) - For UI styling

---

## 📂 Project Structure

todos_web/
│
├── app.py # Main Flask app
├── todo.db # SQLite database (auto-created)
├── templates/
│ ├── base.html # Base layout with navbar
│ ├── index.html # Home page with todo list and add form
│ └── update.html # Update form for editing a todo
├── static/ # (Optional) Static files like CSS/JS if added
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/todos_web.git
   cd todos_web
Create Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate    # For Linux/macOS
venv\Scripts\activate       # For Windows
Install Required Packages

pip install -r requirements.txt
Run the Application

python app.py
Visit the App
Open your browser and go to: http://127.0.0.1:5000
