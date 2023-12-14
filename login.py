from flask import Flask, request, render_template
from datetime import datetime
import csv
import hashlib

app = Flask(__name__)
app.debug = True

def hash_password(password):
    '''
    Hashes the user password using SHA-256 encryption algorithm.

    Args:
        password (str): password to be hashed

    Returns:
        A new string that is encrypted with SHA-256
    '''
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


@app.route('/')
def index():
    '''
    Sets the default route of the webpage.

    Returns:
        A rendered page of the html.
    '''
    return render_template('login.html')


@app.route('/kiosk-form', methods=['POST'])
def kiosk_form():
    '''
    When submit button is pressed: opens a new 
    page to kiosk-form.html. Takes the name and 
    email and saves it to data.csv file.

    Returns:
        A new page
    '''
    
    name = request.form.get('name')
    email = request.form.get('email')
    user_password = hash_password(request.form.get('passcode'))

    # Save the data to a CSV file
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email, datetime.now().strftime('%m-%d-%Y %H:%M')[0:10], datetime.now().strftime('%m-%d-%Y %H:%M')[11:16]])
    file = csv.reader(open("user-credentials.csv"))
    for name, password in file:
        if password == user_password:
            return render_template("kiosk-form.html")

    return "Incorrect password"

@app.route('/final-check', methods=['POST'])
def final_check():
    # TODO add more to this comments
    '''
    Collects data from the kiosk-form.html and 
    adds it to ____________.csv.

    Return:
        Some pages. 
    '''
    return render_template('end-page.html')


@app.route('/end', methods=['POST'])
def end():
    '''
    When button is pressed: opens a new 
    page to a thank you message. Writes true 
    or false and the day it was pressed to the 
    missing-equipment.csv file

    Returns:
        A new page with a message
    '''

    with open('missing-equipment.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if request.form['button'] == 'Yes':
            writer.writerow([True, datetime.today().strftime('%Y-%m-%d')])
        elif request.form['button'] == 'No':
            writer.writerow([False, datetime.today().strftime('%Y-%m-%d')])
    
    return "Thank you for your submission. Please make sure to write a ticket if any equipment is missing!"

if __name__ == '__main__':
    app.run()