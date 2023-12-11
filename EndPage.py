from flask import Flask, request, render_template
from datetime import datetime
import csv

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('endPage.html')

@app.route('/submit', methods=['POST'])
def submit():
    
    with open('missingEquipmentData.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if request.form['button'] == 'Yes':
            writer.writerow([True, datetime.today().strftime('%Y-%m-%d')])
        elif request.form['button'] == 'No':
            writer.writerow([False, datetime.today().strftime('%Y-%m-%d')])
    
    return "Thank you for your submission. Please make sure to write a ticket if any equipment is missing!"

if __name__ == '__main__':
    app.run()
    
