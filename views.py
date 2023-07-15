```python
from flask import render_template, request, redirect, url_for, flash
from app import app
from db import db
from models import Todo

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        new_todo = Todo(title=title)
        db.session.add(new_todo)
        db.session.commit()
        flash('Todo Created Successfully')
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    todo = Todo.query.get(id)
    if request.method == 'POST':
        todo.title = request.form['title']
        db.session.commit()
        flash('Todo Updated Successfully')
        return redirect(url_for('index'))
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    todo = Todo.query.get(id)
    if request.method == 'POST':
        db.session.delete(todo)
        db.session.commit()
        flash('Todo Deleted Successfully')
        return redirect(url_for('index'))
    return render_template('delete.html', todo=todo)
```