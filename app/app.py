from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>DevSecOps Security Lab</h1>
    <p>Application Python sécurisée par CI/CD</p>
    <a href='/health'>Health Check</a><br>
    <a href='/echo?name=student'>Echo</a>
    """

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

@app.route("/echo")
def echo():
    name = request.args.get("name", "student")
    command = "echo " + name
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
