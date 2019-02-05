from flask import Flask
from lab3_code import *

# Set up application
app = Flask(__name__)


# Routes
@app.route('/')#http://127.0.0.1:5000/
def home_page(): # Route function names can be anything unique
    return '<h1>Welcome to the banking application!</h1>' # Route functions can return plain old text, or text in correctly formatted HTML (or the return values of many special functions we haven't looked at yet)

# Something else to note is that the functions don't get INVOKED the way you may be used to. Running the application and *going to a URL that matches the path in the @app.route() business IS what runs that function!


#amazing = Bank("Amazing New Bank", Dollar, 1)
@app.route('/bank/<name>')#http://127.0.0.1:5000/bank/Amazing%20New%20Bank
def welcomebank(name):
    return '<h1>Welcome to {}!</h1>'.format(name)


#twentyfive_dollars = Dollar(25)
@app.route('/dollar/<amt>')#http://127.0.0.1:5000/dollar/25
def dollaramt(amt):
    if int(amt) <=1:
        return '<h1>{} Dollar</h1>'.format(amt)
    else:
        return '<h1>{} Dollars</h1>'.format(amt)
    #number dollars



@app.route('/yuan/<amt>')#http://127.0.0.1:5000/yuan/1
def yuanamt(amt):
    return '<h1>{} Yuan</h1>'.format(int(amt))



@app.route('/pound/<amt>')
def poundamt(amt):
    if int(amt) <=1:
        return '<h1>{} Pound</h1>'.format(amt)
    else:
        return '<h1>{} Pounds</h1>'.format(amt)


#the last part
#FifthThird = Bank("FifthThird", Dollar, 1000)
#Amazing = Bank("A%20m%20a%20z%20i%20n%20g", Yuan, 17600)
@app.route('/bank/<name>/<currency>/<value>')
def ability(name, currency, value):
    if currency == 'Dollar':
        currency = 'Dollar'
    elif currency == 'Yuan':
        currency = 'Yuan'
    elif currency == 'Pound':
        currency = 'Pound'
    else:
        return '<h1>Invalid URL inputs for bank.</h1>'
    return '<h1>Welcome to the {} bank! {} Bank holds the {} currency and currently holds {} of {}.</h1>'.format(name, name, currency, value, currency)
        #Welcome to the NAME bank! NAME Bank holds the CURRENCY currency and currently holds VALUE of CURRENCY.


if __name__ == '__main__':
    app.run()
