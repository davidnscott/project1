from . import db

class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),unique=True)
    bedrooms = db.Column(db.String(80))
    bathrooms = db.Column(db.String(80))
    location = db.Column(db.String(80))
    price = db.Column(db.String(80))
    type = db.Column(db.String(80))
    description = db.Column(db.String(255))
    photofile = db.Column(db.String(80))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
	
    def __init__(self,title,bedrooms,bathrooms,location,price,type,description,photofile):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photofile = photofile
		
