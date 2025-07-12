from flask import Flask, render_template, request, redirect 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# Home route
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form.get('title')  # ✅ FIX: use form.get() to avoid KeyError
        desc = request.form.get('desc')
        
        if title and desc:  # ✅ Basic Validation
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)

# Test route
@app.route('/show')
def index():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'This is Product page'

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form.get('title')  # ✅ FIX: use form.get() to avoid KeyError
        desc = request.form.get('desc')
        
        if title and desc:  # ✅ Basic Validation
            todo = Todo.query.filter_by(sno=sno).first()
            todo.title = title
            todo.desc = desc
            db.session.add(todo)
            db.session.commit()
            return redirect('/')
        
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

# Run and create DB
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # ✅ Make sure tables are created inside app context
    app.run(debug=True)
