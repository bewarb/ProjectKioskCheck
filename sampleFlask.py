from flask import Flask, request, render_template
import csv

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('testForm.html')

@app.route('/submit', methods=['POST'])
def submit():
    passcode = request.form.get('passcode')
    file = csv.reader(open("kioskers.csv"))
    for name, password in file:
        if passcode == password:
            return "Correct Password. Hello " + name + "!"

    return 'Data submitted successfully.'

if __name__ == '__main__':
    app.run()
    
