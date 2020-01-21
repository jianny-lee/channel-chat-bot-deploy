from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return "Hi! If you wanna get response about Skill server, Go to /skill"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)