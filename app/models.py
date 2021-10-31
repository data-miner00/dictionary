from app import db

class Base(db.Model):
    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
                                
class Item(Base):
    name          = db.Column(db.String(length=30), nullable=False, unique=True)
    price         = db.Column(db.Integer(), nullable=False)
    barcode       = db.Column(db.String(length=12), nullable=False, unique=True)
    description   = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'