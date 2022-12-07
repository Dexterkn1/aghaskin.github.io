from process import preparation, generate_response
from flask import redirect, Flask, render_template, request

# download nltk
preparation()

#Start Chatbot
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result

@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)