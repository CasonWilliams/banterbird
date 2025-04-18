from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/posts')
def get_posts():
    with open('post.json, 'r' ') as file:
        post = json.load(file)
        return jsonify(post)

if __name__ == '__main__':
    app.run(debug=True)
