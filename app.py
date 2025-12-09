from flask import Flask, render_template
 
# Create Flask application
app = Flask(__name__)
 
# Home route → Loads the UI page
@app.route("/")
def home():
    return render_template("index.html")
 
# Basic route → Returns simple text
@app.route("/hello")
def say_hi():
    return "Hi Flask 👋"
 
# Run the app
if __name__ == "__main__":
    # debug=True automatically reloads changes
    app.run(debug=True, port=5500)
