from . import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    price = db.Column(db.Integer)

    def __repr__(self):
        return self.name


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    item = db.relationship('Item', backref=db.backref('purchases', lazy='dynamic'))
    date_purchase = db.Column(db.Date)

    def __repr__(self):
        return self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return self.username
