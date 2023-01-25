import enum
from app.database import db
from datetime import datetime

# Task Status Model
class TaskStatusEnum(enum.Enum):
    pending = 'pending'
    completed = 'completed'

# Task Model
class Task(db.Model):
    STATUS = [
        ('pending', 'pending'),
        ('completed', 'completed')
    ]
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    status = db.Column(
        ChoiceType(STATUS), 
        default=TaskStatusEnum.pending,
        nullable=False
    )
    last_updated = db.Column(db.DateTime, default=datetime.now())
    
    
    def __repr__(self) -> str:
        return self.name