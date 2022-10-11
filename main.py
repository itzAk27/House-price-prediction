# flask, sciket-learn, pandas, pickle-mixin

import pandas as pd

from flask import Flask, render_template, request

app = Flask(__name__)
data = pd.read_csv('Cleaned_data.csv')


@app.route('/')
def index():
    location = sorted(data['location'].unique())
    return render_template('index.html', locations=location)


@app.route('/predict', methods=["POST"])
def predict():
    return ""


if __name__ == "__main__":
    app.run(debug=True, port=5001)
