from flask import Flask, render_template

import user_story

app = Flask(__name__)


@app.route('/')
def index():
    user_stories = user_story.get_user_stories()
    headers = user_story.get_headers()
    return render_template("index.html", stories=user_stories, headers=headers)


if __name__ == '__main__':
    app.run()