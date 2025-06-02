from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
   return "API is live"
@app.route("/score")
def get_score_html():
   match_url = request.args.get("url")
   if not match_url:
       return jsonify({"error": "Missing 'url' query parameter"}), 400
   headers = {"User-Agent": "Mozilla/5.0"}
   try:
       res = requests.get(match_url, headers=headers)
       soup = BeautifulSoup(res.text, "html.parser")
       div = soup.find("div", {"class": "BoxStyle__BottomSection-xydo28-3"})
      print(res.text[:1000])
       if not div:
           return jsonify({"error": "Score section not found"}), 404
       return div.decode_contents()
   except Exception as e:
       return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port)
