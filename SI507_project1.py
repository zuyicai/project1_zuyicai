from flask import Flask
from lab3_code import *
# import statements

# Set up application
app = Flask(__name__)


# Routes
@app.route('/')#http://127.0.0.1:5000/
def home_page():
    return '<h1>Hi! Welcome to Zuyi Cai\'s banking application!</h1>'


#amazing = Bank("Amazing New Bank", Dollar, 1)
@app.route('/bank/<name>')#http://127.0.0.1:5000/bank/Amazing%20New%20Bank
def welcomebank(name):
    bank = Bank(name, Dollar, 0)
    return '<h1>Welcome to {}!</h1>'.format(bank.name)


#twentyfive_dollars = Dollar(25)
@app.route('/dollar/<amt>')#http://127.0.0.1:5000/dollar/25
def dollaramt(amt):
    dollar = Dollar(int(amt))
    return '<h1>NUMBER Dollars /{} {}</h1>'.format(dollar.value,dollar.unit_name)
    #number dollars



@app.route('/yuan/<amt>')#http://127.0.0.1:5000/yuan/1
def yuanamt(amt):
    yuan = Yuan(int(amt))
    return '<h1>NUMBER Yuan /{} {}</h1>'.format(yuan.value,yuan.unit_name)



@app.route('/pound/<amt>')#http://127.0.0.1:5000/pound/100
def poundamt(amt):
    pound = Pound(int(amt))
    return '<h1>NUMBER Pounds /{} {}</h1>'.format(pound.value,pound.unit_name)


#the last part
#FifthThird = Bank("FifthThird", Dollar, 1000)
#Amazing = Bank("A%20m%20a%20z%20i%20n%20g", Yuan, 17600)
@app.route('/bank/<name>/<currency>/<value>')#http://127.0.0.1:5000/bank/A%20m%20a%20z%20i%20n%20g/Yuan/17600
def bank_ability(name, currency, value):
    validcurrency = ['Dollar', 'Yuan', 'Pound']
    if currency == valid_urrency[0]:
        bank = Bank(name, Dollar, int(value))
    elif currency == validcurrency[1]:
        bank = Bank(name, Yuan, int(value))
    elif currency == validcurrency[2]:
        bank = Bank(name, Pound, int(value))
    else:
        return '<h1>Invalid URL inputs for bank.</h1>'
    return '<h1>Welcome to the {} bank! {} Bank holds the {} currency and currently holds {} of {}.</h1>'.format(bank.name, bank.name, bank.current_account.unit_name, bank.current_account.value, bank.current_account.unit_name)
        #Welcome to the NAME bank! NAME Bank holds the CURRENCY currency and currently holds VALUE of CURRENCY.


if __name__ == '__main__':
    app.run()
