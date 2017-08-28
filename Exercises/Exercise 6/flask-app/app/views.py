from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from app.computeWordCount import computeWordCount
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        wordCounts = computeWordCount(form.data['text'])
        print(wordCounts)
        return render_template('index.html', wordCounts = wordCounts, form=form)
    return render_template('index.html',form=form)
