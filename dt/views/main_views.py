from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('main',__name__,url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, DT!'

# @bp.route('/')
# def index():
#     return redirect(url_for('question._list'))

@bp.route('/')
def index():
    return render_template('main_html.html')