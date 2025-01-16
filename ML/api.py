from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
from sklearn.exceptions import NotFittedError
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
CORS(app)

try:
    ann_model = joblib.load('./model.pkl') 
    scaler = joblib.load('./scaler.pkl')   
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
    raise
except Exception as e:
    print(f"An unexpected error occurred while loading model/scaler: {e}")
    raise

@app.route('/predict', methods=['POST'])
def predict_spoilage():
    try:
        
        data = request.get_json(force=True)

    
        temperature = data.get("temperature", 25.0)
        humidity = data.get("humidity", 50.0)
        sunlight = data.get("sunlight", 75.0)

    
        if any(x is None or not isinstance(x, (int, float)) for x in [temperature, humidity, sunlight]):
            return jsonify({"error": "Invalid input. Please provide numeric values for all features."}), 400


        input_features = np.array([[temperature, humidity, sunlight]])


        try:
            input_scaled = scaler.transform(input_features)
        except NotFittedError:
            return jsonify({"error": "Scaler is not fitted. Ensure the scaler is properly trained."}), 500


        predicted_probability = ann_model.predict(input_scaled)[0] 
        predicted_class = 1 if predicted_probability >= 0.5 else 0


        return jsonify({
            "predicted_spoilage_class": predicted_class,
            "predicted_spoilage_probability": round(predicted_probability, 4)
        })

    except KeyError as e:
        return jsonify({"error": f"KeyError: {e}"}), 400
    except ValueError as e:
        return jsonify({"error": f"ValueError: {e}"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=8000)
