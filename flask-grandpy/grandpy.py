import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)


bp = Blueprint(
    'grandpy',
    __name__
)

@bp.route('/')
def index():


    return render_template('grandpy.html')

@bp.route('/show_response', methods=('GET', 'POST'))
def show_response():
    if request.method == 'POST':
        message = request.form['message']
        error = None
    
        if message is None:
            error = "Que souhaites-tu savoir ?"
        
        if error is None:
            return redirect(url_for('index'))
        
        flash(error)
    
    return render_template('grandpy/home.html')