from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as db1:
        email =  data['email']
        subject = data['subject']
        msg = data['msg']
        csv_writer = csv.writer(db1, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,msg])

def write_to_file(data):
    with open('database.txt', mode='a') as db:
        email =  data['email']
        subject = data['subject']
        msg = data['msg']
        file = db.write(f'\n{email},{subject},{msg}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST' :
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/tq.html')
    else:
        return 'something went wrong'
