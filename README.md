This webapp resizes a downloaded image. To use, download an image to imageResize/origImages.

Then, to run the website, run the command "python3 server.py" in the terminal while in the imageResize directory.

Now, maneuver to localhost:5000 in your preferred browser, and fill out the given form, press submit, and get your image back with the given dimensions.

A copy of the file is also stored in imageResize/static/resizedImages.

Important points:
- Flask, a microframework for python to run web servers, is used. Website is http://flask.pocoo.org/
- pillow, a fork of PIL, or Python Image Library, is used. Also needed with this is libjpeg for jpg functionality. Pillow is used for the resizing of the image. https://pypi.python.org/pypi/Pillow
- flask.ext.wtf is needed for obtaining data from an HTML form. https://flask-wtf.readthedocs.org/en/latest/
- resizedImages is in the static folder because that is where Flask's front-end looks to get images.

Some decisions I made along the way:
- I chose to use Flask over Spark because I've had more experience with it and it's easier to identify endpoints. This is because each endpoint is a function with a decorator showing which endpoint is being coded for.

- I turned off CSRF protection because this is a local website, so unless I attack myself this isn't an issue.

- I had to create a secret key because I'm using form data in my server, specifically for resizing the given image. I just made a random key because again, this is for one person and would only become an issue if this was used by multiple users.


Possible addons: 
- login/users
- slidebar for sizes.
- url linking instead of downloading images.
- choosing an image from anywhere in the computer.

Find this project on github: https://github.com/idanhovav/imageresize.

Forks welcome!

- Idan Hovav, 03 April 2016
