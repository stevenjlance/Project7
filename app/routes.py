from app import app
from flask import render_template, request
from app.models import model

@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')
@app.route('/results', methods = ['GET','POST'])
def results():
    userdata = dict(request.form)
    data = model.score_calculator(userdata)
    data = str(data)
    name = userdata['name']
    if request.method == 'GET':
        return 'Please go to the form on the main page to determine your results!'
    elif data == 'HUFFLEPUFF':
        return render_template('Hufflepuff_results.html', data = data, name = name)
    elif data == 'Ravenclaw':
        return render_template('Ravenclaw_results.html',data = data, name = name)
    elif data == 'GRYFFINDOR':
        return render_template('gryffindor_results.html', data = data, name = name)
    elif data == 'SLYTHERIN':
        return render_template('slytherin_results.html', data = data, name = name)
    else:
        return render_template('index.html')
