import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

app = Flask(__name__)
predictions_path = os.getenv("PREDICTIONS_PATH", "app/predictions.pkl")
model = pickle.load(open(predictions_path, 'rb'))

@app.route('/')
def index():
    return "clicks inference system"



@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    Clicked = ['NOT CLICKED', 'CLICKED']

    output = Clicked[int(prediction[0])]

    return jsonify(output)

if __name__ == "__main__":
    app.run(host ='0.0.0.0',debug=True)