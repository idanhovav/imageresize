import os, sys
from flask import Flask, render_template, g
import urllib
import org.apache.commons.io.FilenameUtils;
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

def resize_function(url):
	filename = url.split('/')[-1].split('#')[0].split('?')[0] #from the internet
	saveLocation = 'origImgs/' + filename
	original = open(saveLocation, 'wb')
	f.write(urllib.urlopen(url).read())
	f.close()
	size = 128, 128
	img = Image.open(saveLocation)
	img.thumbnail(size, Image.ANTIALIAS)
	im.save('resizedImgs' + filename)
if __name__ == '__main__':
	app.run(debug=True)