from flask import Flask, render_template, redirect, url_for, request, send_file
from math import sqrt
import pandas as pd
import json
import csv

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/biodata")
def biodata():
    return render_template('cv.html')

@app.route("/akar")
def akar():
    return render_template('akarangka.html')

@app.route("/data")
def data():
    return render_template('getdata.html')

@app.route("/form")
def form():
    return render_template('postform.html')

#akar--------------------------------------------------------------
@app.route('/sqroot', methods = ['POST', 'GET'])
def root():
    if request.method == "POST":
        angka=request.form['bil']
        try:
            hasil = round(sqrt(int(angka)),2)
            return redirect(url_for('akar',num=angka, value=hasil))
        except ValueError:
            return redirect(url_for('eroot', num = angka))
    
@app.route('/akar/<float:num>/<float:value>')
def akarz(num,value):
    return f'Akar dari {num} adalah {value}'
    
@app.route('/eroot/<num>')
def eroot(num):
    return f'Akar dari {num} td :('

#get form csv ke json--------------------------------------
@app.route('/convert', methods = ['GET', 'POST'])
def convert():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)

    data = {}
    with open(f.filename) as csvFile:                     
        csvReader = csv.DictReader(csvFile)
        for i, rows in enumerate(csvReader):
            id = i
            data[id] = rows

    with open('array.json', 'w') as jsonFile:       
        jsonFile.write(json.dumps(data, indent=4))

    return send_file('array.json', as_attachment=True)
#postform--------------------------------------------------------
@app.route('/survey', methods =['POST'])
def survey():
    nama=request.form['nama']
    nim=request.form['nim']

    result = {
        'nama': nama,
        'nim': nim
    }
    result=json.dumps(result)
    return result




