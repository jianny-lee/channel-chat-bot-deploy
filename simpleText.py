from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/test", methods=["GET"])
def test():
    data = jsonify(
        version = 1.0,
        value_list = [
            "abc",
            "def"
        ]
    )
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
