from app import db
from datetime import datetime

class Assistantship(db.Model):
    sid = db.Column(db.Integer,primary_key=True)
    term = db.Column(db.String(2),db.CheckConstraint('term in (FA,SP,SU)'))
    year = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Assistantship {}>'.format(self.sid)
