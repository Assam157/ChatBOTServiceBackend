from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Flask API is running!", 200  # ✅ Fix for 405 error

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Ensure JSON request
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "Missing 'message' field"}), 400  # ✅ Handle missing data

        prompt = data["message"]

        # Simulated response (replace with actual API call)
        response = {"reply": f"You said: {prompt}"}

        return jsonify(response), 200  # ✅ Ensure valid JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # ✅ Proper error handling

if __name__ == "__main__":
    app.run(debug=True, port=5000)
