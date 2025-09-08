from flask import Flask, jsonify
from flask_cors import CORS
from crypto_utils import coingecko_data

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "flask esta rodando !!!!" 

@app.route("/api/global", methods=["GET"])
def global_data():
    try:
        data = coingecko_data()
        return jsonify(data)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
