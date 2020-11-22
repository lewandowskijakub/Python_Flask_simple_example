from flask import Flask, render_template, request, redirect, url_for

import user_story

app = Flask(__name__)


@app.route('/')
@app.route('/stories')
def index():
    user_stories = user_story.get_user_stories()
    headers = user_story.get_headers()
    return render_template("index.html", stories=user_stories, headers=headers)


@app.route('/stories/<story_id>')
def get_story(story_id):
    story = user_story.get_user_story(story_id)
    headers = user_story.get_headers()
    return render_template("story.html", story=story, headers=headers)


@app.route('/add-story-form')
def add_story_form():
    headers = user_story.get_headers()
    return render_template("story-form.html", headers=headers)


@app.route('/stories', methods=["POST"])
def add_story():
    new_story = dict(request.form)
    headers = user_story.get_headers()
    new_story[headers[0]] = user_story.get_new_id()
    new_story[headers[6]] = user_story.get_statuses()[0]

    user_story.add_user_story(new_story)

    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()
