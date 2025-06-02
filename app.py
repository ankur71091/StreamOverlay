from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/score")
def get_score_html():
   match_url = request.args.get("url")
   if not match_url:
       return jsonify({"error": "Missing 'url' query parameter"}), 400
   headers = {"User-Agent": "Mozilla/5.0"}
   try:
       res = requests.get(match_url, headers=headers)
       soup = BeautifulSoup(res.text, "html.parser")
       div = soup.find("div", {"class": "BoxStyle__BottomSection-xydo28-3 fTKnqN"})
       if not div:
           return jsonify({"error": "Score section not found"}), 404
       return div.decode_contents()
   except Exception as e:
       return jsonify({"error": str(e)}), 500
