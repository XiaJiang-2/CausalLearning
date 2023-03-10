from flask import Flask, render_template, request, redirect, url_for, flash
import os
import pandas as pd
from pathlib import Path

import PC
import rFCI
import FGES
import GES
import FCI

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'txt', 'csv', 'xlsx', 'dat'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect("/")
        f = request.files['file']
        if f and allowed_file(f.filename):
            f.save(f.filename)
            uploaded_file=True
            return redirect(url_for('CausalLearn_Page', filename=f.filename, uploaded_file=uploaded_file))
        else:
            return redirect("/")

@app.route("/causalLearn", methods=['GET', 'POST'])
def CausalLearn_Page():
    if request.method == 'GET':
        file_uploaded = bool(request.args.get('filename', None))
        if file_uploaded == True:
            filename = request.args.get('filename', None)

            return render_template("CausalLearn_Page.html", name=filename)
        else:
            return redirect('/')
    
    if request.method == 'POST':
        algorithm = request.form['algorithm']
        fileName = request.form['fileName']

        if algorithm == "PC":
            return redirect(url_for("PC_Page", name=fileName))

        if algorithm == "rFCI":
            return redirect(url_for("rFCI_Page", name=fileName))
        
        if algorithm == "FGES":
            return redirect(url_for("FGES_Page", name=fileName))
        
        if algorithm == "GES":
            return redirect(url_for("GES_Page", name=fileName))
        
        if algorithm == "FCI":
            return redirect(url_for("FCI_Page", name=fileName))

@app.route("/PC", methods=['GET'])
def PC_Page():
    if request.method == 'GET':
        fileName = request.args.get('name', None)
        pcObject = PC.PC(fileName)
        os.remove(fileName)
        pcOutput = pcObject.output.split("\n")
        return render_template("PC.html", Lines=pcOutput)

@app.route("/rFCI", methods=['GET', 'POST'])
def rFCI_Page():
    if request.method == 'GET':
        fileName = request.args.get('name', None)

        return render_template("rFCI.html", name=fileName)
    if request.method == 'POST':
        fileName = request.form['fileName']
        delimiter = request.form['delim']

        rfciObject = rFCI.rFCI(fileName, delimiter, "templates/rFCI_Outputs", "rFCI_Result")
        f = open("templates/rFCI_Outputs/rFCI_Result.txt", 'r')
        rFCI_Data = f.readlines()
        f.close()
        os.remove(fileName)
        return render_template("rFCI_Output.html", Lines=rFCI_Data)

@app.route("/FGES", methods=['GET', 'POST'])
def FGES_Page():
    if request.method == 'GET':
        fileName = request.args.get('name', None)

        return render_template("FGES.html", name=fileName)

    if request.method == 'POST':
        fileName = request.form['fileName']
        delimiter = request.form['delim']

        fgesObject = FGES.FGES(fileName, delimiter, "templates/FGES_Outputs", "FGES_Result")
        f = open("templates/FGES_Outputs/FGES_Result.txt", 'r')
        FGES_Data = f.readlines()
        f.close()
        os.remove(fileName)
        return render_template("FGES_Output.html", Lines=FGES_Data)

@app.route("/FCI", methods=['GET', 'POST'])
def FCI_Page():
    if request.method == 'GET':
        fileName = request.args.get('name', None)

        return render_template("FCI.html", name=fileName)

    if request.method == 'POST':
        fileName = request.form['fileName']
        delimiter = request.form['delim']

        df = pd.read_csv(fileName, sep=delimiter)

        fciObject = FCI.FCI(df, "static/images/FCI_Output.png")
        os.remove(fileName)
        return render_template("FCI_Output.html")

@app.route("/GES", methods=['GET', 'POST'])
def GES_Page():
    if request.method == 'GET':
        fileName = request.args.get('name', None)

        return render_template("GES.html", name=fileName)

    if request.method == 'POST':
        fileName = request.form['fileName']
        delimiter = request.form['delim']

        df = pd.read_csv(fileName, sep=delimiter)

        gesObject = GES.GES(df, "static/images/GES_Output.png")
        os.remove(fileName)
        return render_template("GES_Output.html")
            

if __name__ == "__main__":
    app.run(debug=True)