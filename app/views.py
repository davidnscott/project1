"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from app.forms import PropertyForm
from app.models import Property
from app import app, db
from app.config import *
from werkzeug.utils import secure_filename
import os


###
# Routing for your application.
###
@app.route('/property',methods=['GET','POST'])
def property():
	form = PropertyForm()
	if request.method == 'POST':
		print("check1")
		if form.validate_on_submit():
			print("check2")
			photo = form.photo.data	
			file = secure_filename(photo.filename)
			photo.save(os.path.join(app.config['UPLOAD_FOLDER'],file))
			
			entry = Property(
			title = form.title.data,
			bedrooms = form.bedrooms.data,
			bathrooms = form.bathrooms.data,
			location = form.location.data,
			price = form.price.data,
			type = form.type.data,
			description = form.description.data,
			photofile = file)
			
			db.session.add(entry)
			db.session.commit()
			flash('Property succefully added')
		return redirect(url_for('properties'))

	return render_template('property.html',form=form,type=type)

@app.route('/properties')
def properties():
	props = Property.query.all()
	return render_template("properties.html",props=props)
	
@app.route('/property/<propertyid>')
def view_property(propertyid):
	prop = Property.query.get(propertyid)
	return render_template("viewproperty.html",prop=prop)
	
@app.route("/uploads/<filename>")
def get_image(filename):
	rootdir = os.getcwd()
	return send_from_directory(rootdir + "/" + app.config['UPLOAD_FOLDER'],filename)

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
