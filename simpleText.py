from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/skill", methods=["POST"])
def skill():
    data = {
        "version" : "2.0",
        "template" : {
        "outputs" : [
                {
                    "simpleText": {
                    "text": "This is a simple text."
                        }
                    }
                ]
            }
        }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
