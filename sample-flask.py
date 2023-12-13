from flask import Flask, request, render_template
from datetime import datetime
import csv

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    user_passcode = request.form.get('passcode')

    # Save the data to a CSV file
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email, datetime.now().strftime('%m-%d-%Y %H:%M')[0:10], datetime.now().strftime('%m-%d-%Y %H:%M')[11:16]])
    file = csv.reader(open("kioskers.csv"))
    for name, password in file:
        if password == user_passcode:
            return render_template("printer-page.html")

    return "Incorrect Passcode"


if __name__ == '__main__':
    app.run()