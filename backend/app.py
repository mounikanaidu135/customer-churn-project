from flask import Flask, request, jsonify
import pickle
from pymongo import MongoClient

app = Flask(__name__)

# Load model
model = pickle.load(open("../model/model.pkl","rb"))

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["churnDB"]
collection = db["predictions"]

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    tenure = float(data["tenure"])
    monthly = float(data["monthly"])

    prediction = model.predict([[tenure,monthly]])[0]

    result = "Customer will leave" if prediction==1 else "Customer will stay"

    # store in database
    collection.insert_one({
        "tenure":tenure,
        "monthly":monthly,
        "prediction":result
    })

    return jsonify({"prediction":result})

if __name__ == "__main__":
    app.run(port=5000)