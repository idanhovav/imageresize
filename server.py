from flask import Flask, render_template, g

app = Flask(__name__)

@app.route('/')
def home:
	return render_template('home.html')

@app.route('/resize')
def resize(image):
	#resize the goddam image and return it to somewhere

if __name__ == '__main__':
	app.run(debug=True)