# flaskr

# Project source
This is my work on 
(this)[https://flask.palletsprojects.com/en/2.0.x/tutorial/] 
Flask tutorial.


## Virtual Environment

We are using the bundled `venv` module to create the virtual environment for this project. The steps are:
1. create a directory `venv` inside the main project repo
1. `cd venv`
1. `python3 -m venv venv`

From the main project repo (`flask-tutorial/`):
use the command
```
. venv/bin/activate
```
to activate the virtual environment.
and
use the command
```
deactivate
```
do deactivate the virtual environment
***

## Running the app

run the following three commands in the terminal:
```
export FLASK_APP=flaskr
```
```
export FLASK_ENV=development
```
```
flask run
```
The output should look like this: (copied from the tutorial)
```
* Serving Flask app "flaskr"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761
```
Go to http://127.0.0.1:5000/hello in a browser (the url shown on line 4 plus "hello") and we should see the `Hello world` message defined as the return value of the `hello` function in `__init__.py`.
