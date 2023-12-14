from flask import Flask, request, render_template
from datetime import datetime
import csv
import hashlib

# Hash the password using a SHA-256
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('login.html')



@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    user_passcode = hash_password(request.form.get('passcode'))

    # Save the data to a CSV file
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email, datetime.now().strftime('%m-%d-%Y %H:%M')[0:10], datetime.now().strftime('%m-%d-%Y %H:%M')[11:16]])
    file = csv.reader(open("user_credentials.csv"))
    for name, password in file:
        if password == user_passcode:
            return render_template("printer-page.html")

    return "Incorrect password"

@app.route('/submit2', methods=['POST'])
def submit2():
    return 'This is the next page'

if __name__ == '__main__':
    app.run()