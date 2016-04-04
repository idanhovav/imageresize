import os, sys
from flask import Flask, render_template, flash, redirect, session
from PIL import Image
from flask.ext.wtf import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'KJHDJKHKSANM<*&(*^21ngjk574754' # not sure why i need this
originalImageFolderName = "origImages/"
resizedImageFolderName = "static/resizedImages/"


@app.route('/', methods=['GET', 'POST'])
def home():
	form = ImageForm(csrf_enabled=False) # off because localhost
	if form.validate_on_submit():
		fileName = form.fileName.data
		width = form.width.data
		height = form.height.data
		flash('Resizing Image={0} to {1}, {2}'.format(fileName, str(width), str(height)))
		newImg = resize_function(fileName, width, height)
		return render_template('resize.html', image=newImg, picWidth=width, picHeight=height)
	return render_template('home.html', form=form)

#@app.route('/resize')
#def resize(img):
	#resize the goddam image and return it to somewhere
#	return render_template('resize.html', image=img)

# returns filename as a string
def resize_function(inFile, width, height):
	size = int(float(width)), int(float(height))
	inFileName, inExtension = os.path.splitext(inFile)
	outFile = resizedImageFolderName + inFileName + "_RESIZED.jpg"
	try:
		im = Image.open(originalImageFolderName + inFile)
		im.thumbnail(size, Image.ANTIALIAS)
		im.save(outFile, "JPEG")
		return outFile
	except IOError:
		print("issue")

class ImageForm(Form):
	fileName = StringField('fileName', validators=[DataRequired()])
	width = StringField('width', validators=[DataRequired()])
	height = StringField('height', validators=[DataRequired()])

if __name__ == '__main__':
	app.run(debug=True)
