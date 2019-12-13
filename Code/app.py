from flask import Flask, render_template,request, send_from_directory
import os
import markov_chain

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    file = 'sherlock_no_title_chapters.txt'
    generated = markov_chain.main(file)

    return render_template("index.html", generated=generated)