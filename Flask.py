from flask import Flask,request,jsonify
from flask_cors import CORS
import random
app=Flask(__name__)
CORS(app)
API_KEY=""
url=""
Prince_Image=[
    ]
def get_random_images():
    return random.choice(Prince_Image)
@app.route("/Prince",methods=["POST"])
def Prince():
    data=request.json
    prompt=""
    headers={
        "Authorization":f"Bearer {API_KEY}",
        "Content-Type":"application/json"
        }
    payload={
        "model":"mistralai/Mixtral-8x7B-Instruct-v0.1",
        "role":[{"role":"user","content":prompt}]
        }
    response = request.post(url, json=payload, headers=headers)

    if response.status_code == 200:
         return jsonify({"reply": response.json()["choices"][0]["message"]["content"].strip(),
                         "image":get_random_images()})
    else:
         return jsonify({"error": response.json()}), response.status_code

if __name__ == "__main__":
     app.run(debug=True,port=5000,use_reloader=False)
