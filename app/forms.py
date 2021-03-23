from flask_wtf import FlaskForm
from wtforms import SelectField, TextField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
	title = TextField('Property Title',[DataRequired()])	
	bedrooms = TextField('No. of Rooms',[DataRequired()])
	bathrooms = TextField('No. of Bathrooms',[DataRequired()])
	location = TextField('Location',[DataRequired()])
	price = TextField('Price',[DataRequired()])
	type = SelectField('Property Type',choices=[('House','House'),('Apartment','Apartment')])
	description = TextAreaField('Description', [DataRequired()])
	photo = FileField('Photo',validators = [FileRequired(),FileAllowed(['jpg','png'],'imagesonly')])