from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "project": "Secure CI/CD Pipeline",
        "status": "running",
        "message": "Application deployed successfully!"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )