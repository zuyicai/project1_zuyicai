# Project1_zuyicai: A simple banking app

This's a whole web application — a very simple one, using the web framework called Flask. Using this small application, you can get different outputs in the form of URLs.

Actually, I import everything from lab3_code.py to make the use of "Currency"  "Bank" class. Readers need to follow the steps to install everything needed to run this application.

## Getting Started

* Anaconda installed
* Open your terminal window! `cd` to the place where you want this project to go.
* This repository cloned to somewhere in your computer (the place).
```
git clone <git url>
```
* `cd` into where the project lives
* Create a virtual environment for it
```
virtualenv env
```
* Activate the virtual environment
```
Activate
```
* install all requirement
```
pip install -r requirements.txt
```
```
Deactivate
```
* Just run the banking app!
```
python SI507_project1.py runserver
```
* Check out what’s happening in your terminal window!
* Open a web browser, type in and check out this URL:
http://127.0.0.1:5000/
you will see "Welcome to the banking application!"

* Open another tab and go to:
http://127.0.0.1:5000/bank/<name>
e.g. http://127.0.0.1:5000/bank/Amazing%20New%20Bank you will see "Welcome to Amazing New Bank!"

* Now try going to:
http://127.0.0.1:5000/<currency>/<amt>
e.g. http://127.0.0.1:5000/dollar/25 you will see"25 Dollars"

* Now try going to:
http://127.0.0.1:5000/bank/<name>/<currency>/<value>
e.g. http://127.0.0.1:5000/bank/A%20m%20a%20z%20i%20n%20g/Yuan/17600 you will see "Welcome to the A m a z i n g bank! A m a z i n g Bank holds the Yuan currency and currently holds 17600 of Yuan."
e.g. http://127.0.0.1:5000/bank/specialbank/Franz/100 you will see "Invalid URL inputs for bank."

* Exit it / stop it running on the local server by typing `Control + C`
