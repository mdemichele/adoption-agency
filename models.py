from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""
    db.app = app 
    db.init_app(app)
    
# Pet Model 
class Pet(db.Model):
    """Defines a pet instance"""
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.String(1000))
    age = db.Column(db.Integer)
    notes = db.Column(db.String(50))
    available = db.Column(db.Boolean, nullable=False, default=True)
    
