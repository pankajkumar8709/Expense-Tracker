from expense import app,db

class expenses(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    amount=db.Column(db.Integer(),nullable=False)
    category=db.Column(db.String(50),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    description=db.Column(db.String(),nullable=False)