import openai
import requests 
from flask import Flask,request,jsonify
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
 
API_KEY = "riXezrVqPczSVIcHnsqxlsFkiKFiiyQu"
url = "https://api.deepinfra.com/v1/openai/chat/completions"
@app.route("/chat",methods=["POST"])
@app.route("/",methods=["GET"])
def home():
    print("FlaskAPI is running")
def chat():
   data=request.get_json()
   if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' field"}), 400  
   prompts=data["json"]
    
   headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
   payload = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",  # You can change to "meta-llama/Meta-Llama-3-8B"
        "messages": [{"role": "user", "content": prompt}]
    }
    
   response = requests.post(url, json=payload, headers=headers)

   if response.status_code == 200:
        return jsonify({"reply": response.json()["choices"][0]["message"]["content"].strip()})
   else:
        return jsonify({"error": response.json()}), response.status_code

if __name__ == "__main__":
    app.run(debug=True,port=5000,use_reloader=False)
