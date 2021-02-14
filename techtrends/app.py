import sqlite3
import logging

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort


# Variable to store the total amount of connections to the database
databaseConnectionsCount = 0

# Function to get a database connection.
# This function connects to database with the name `database.db`


def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

# Function to get a post using its ID


def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                              (post_id,)).fetchone()
    connection.close()
    global databaseConnectionsCount
    databaseConnectionsCount += 1

    return post


# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route of the web application


@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    global databaseConnectionsCount
    databaseConnectionsCount += 1
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered
# If the post ID is not found a 404 page is shown


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        app.logger.info('Article Not Found')
        return render_template('404.html'), 404
    else:
        app.logger.info('Article "' + post['title'] + '" retrieved!')
        return render_template('post.html', post=post)

# Define the About Us page


@app.route('/about')
def about():

    app.logger.info('The "About Us" page is retrieved')
    return render_template('about.html')

# Define the post creation functionality


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                               (title, content))
            connection.commit()
            connection.close()
            global databaseConnectionsCount
            databaseConnectionsCount += 1
            app.logger.info('Article "' + title + '" created!')
            return redirect(url_for('index'))

    return render_template('create.html')

# Define the endpoint that returns the health status of the application


@app.route('/healthz')
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    return response

# Define the metrics endpoint


@app.route('/metrics')
def metrics():
    connection = get_db_connection()
    posts_num = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    global databaseConnectionsCount
    databaseConnectionsCount += 1
    response = app.response_class(
        response=json.dumps(
            {"db_connection_count": databaseConnectionsCount, "post_count": len(posts_num)}),
        status=200,
        mimetype='application/json'
    )

    return response


# start the application on port 3111
if __name__ == "__main__":

    # stream logs to app.log file
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    app.run(host='0.0.0.0', port='3111')
