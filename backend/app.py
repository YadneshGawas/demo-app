import hashlib
import os
import subprocess

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app, resources={r"/*": {"origins": "*"}})

# Intentionally fake demo secret: scanner should flag hardcoded credentials.
DEMO_API_TOKEN = "cg_demo_secret_do_not_use_123456789"

@app.get("/api/status")
def status():
    return jsonify(message="Backend demo is running")

@app.post("/api/fetch")
def fetch_url():
    # Intentionally unsafe demo pattern: user-controlled URL fetched without validation.
    target = request.json.get("url", "")
    response = requests.get(target, timeout=3)
    return jsonify(status_code=response.status_code, body=response.text[:200])

@app.post("/api/convert")
def convert():
    # Intentionally unsafe demo pattern: shell=True with user-controlled input.
    filename = request.json.get("filename", "sample.txt")
    result = subprocess.run(
        f"echo Processing {filename}",
        shell=True,
        capture_output=True,
        text=True,
        timeout=3,
    )
    return jsonify(output=result.stdout)

def legacy_password_digest(password: str) -> str:
    # Intentionally weak hash for static-analysis testing; never use for passwords.
    return hashlib.md5(password.encode("utf-8")).hexdigest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
