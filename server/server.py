from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/process", methods=["POST"])
def process_request():
    # ---- SERVER RECEIVES REQUEST HERE ----
    data = request.get_json()

    print("Server received:")
    print(data)

    # Simulate work
    result = "work completed"

    return jsonify({"status": result})


if __name__ == "__main__":
    app.run(port=8000, debug=True)
