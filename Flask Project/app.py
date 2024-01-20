

import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

# ...

@app.route('/')
def homepage():
    # Assuming 'tomorrows_predictions.csv' contains the predictions
    predictions = pd.read_csv('tomorrows_predictions.csv')
    return render_template('index.html', predictions=predictions, columns=predictions.columns)


if __name__ == '__main__':
    app.run(debug=True)


