from flask import Flask, escape

app = Flask(__name__)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'  


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'  


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Sub-path {escape(subpath)}'


@app.errorhandler(404)
def page_not_found(error):
    return "There is no page here..."