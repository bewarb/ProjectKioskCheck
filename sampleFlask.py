from flask import Flask, request, render_template
import csv

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('testForm.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    # Save the data to a CSV file
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email])

    return 'Data submitted successfully.'

if __name__ == '__main__':
    app.run()
