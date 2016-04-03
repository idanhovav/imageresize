import os, sys
from flask import Flask, render_template, g
import urllib
#import org.apache.commons.io.FilenameUtils;
import Image

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/resize')
def resize():
	#resize the goddam image and return it to somewhere
	IMAGE = [0]
	return render_template('resize.html', image=IMAGE)

def resize_function(inFile):
	size = 128, 128
	inFileName, inExtension = os.path.splitext(inFile)
	outFile = inFileName + ".thumbnail"
	try:
		im = Image.open(inFile)
		im.thumbnail(size, Image.ANTIALIAS)
		im.save(outFile, "JPEG")
	except IOError:
		print("issue")
if __name__ == '__main__':
	app.run(debug=True)