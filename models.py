```python
from flask_sqlalchemy import SQLAlchemy
from db import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return f'<Todo {self.task}>'
```