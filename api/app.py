from flask import Flask , request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = load_model("../Model/RNN_Model_Bidirectional")

class_labels = {
    0: 'toxic',
    1: 'severe_toxic',
    2: 'obscene',
    3: 'threat',
    4: 'insult',
    5: 'identity_hate',
    6: 'good'
}

@app.route('/')
def index():
    return 'Hello World!'


@app.route('/prediction', methods=['POST'])
def predict():
    data = request.json.get('data')

    test_str = [data]
    probs = model.predict(test_str)
    squeezed_probs = tf.round(probs[0])

    # Convert EagerTensor to a Python list
    squeezed_probs_list = squeezed_probs.numpy().tolist()
    
    labeled_predictions = [
        {"label": class_labels[i], "prediction": float(pred)}
        for i, pred in enumerate(squeezed_probs_list)
    ]
    

    return jsonify(labeled_predictions)








if __name__ == '__main__':
    app.run()

