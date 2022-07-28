import pandas as pd
import pickle as pkl
from flask import Flask, render_template, request

app = Flask(__name__)
model = pkl.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    clump = request.form.get('clump')
    size = request.form.get('size')
    shape = request.form.get('shape')
    adhesion = request.form.get('adhesion')
    epithelial = request.form.get('epithelial')
    nuclei = request.form.get('nuclei')
    chromatin = request.form.get('chromatin')
    nucleoli = request.form.get('nucleoli')
    mitoses = request.form.get('mitoses')
    input = pd.DataFrame([[clump, size, shape, adhesion, epithelial, nuclei, chromatin, nucleoli, mitoses]], columns = ['Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses'])
    prediction = model.predict(input)[0]
    if prediction == 2:
        return render_template('index.html', prediction_text = f'The Cancer is Benign')
    if prediction == 4:
        return render_template('index.html', prediction_text = f'The Cancer is Malignant')

if __name__ == '__main__':
    app.run(debug = True)