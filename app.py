from flask import Flask, request, jsonify
from flask_cors import CORS
from playwright.sync_api import sync_playwright
import os
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
   return "Playwright-based scraper is live!"
@app.route("/score")
def get_score():
   match_url = request.args.get("url")
   if not match_url:
       return jsonify({"error": "Missing 'url' query parameter"}), 400
   try:
       with sync_playwright() as p:
           browser = p.chromium.launch(headless=True)
           page = browser.new_page()
           page.goto(match_url, timeout=60000)
           page.wait_for_selector("div.BoxStyle__BottomSection-xydo28-3.fTKnqN", timeout=10000)
           html = page.inner_html("div.BoxStyle__BottomSection-xydo28-3.fTKnqN")
           browser.close()
           return html
   except Exception as e:
       return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port)
