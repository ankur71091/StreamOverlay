from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)
@app.route("/score")
def get_score_html():
   url = "https://escalive.com/match/137112-7249900/scorecard/?period=2939456"
   headers = {"User-Agent": "Mozilla/5.0"}
   res = requests.get(url, headers=headers)
   soup = BeautifulSoup(res.text, "html.parser")
   # Find the specific div
   target_div = soup.find("div", {"class": "BoxStyle__BottomSection-xydo28-3 fTKnqN"})
   if not target_div:
       return jsonify({"error": "Could not find score section"}), 404
   return target_div.decode_contents()
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)