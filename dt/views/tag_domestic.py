from flask import Blueprint, url_for, render_template

bp = Blueprint('domestic',__name__,url_prefix='/domestic')

@bp.route('/seoul/')
def seoul():
    return render_template('/main_tag/tag_html_1/main_html_1-1.html')

@bp.route('/incheon/')
def incheon():
    return render_template('/main_tag/tag_html_1/main_html_1-2.html')

@bp.route('/jeonju/')
def jeonju():
    return render_template('/main_tag/tag_html_1/main_html_1-3.html')

@bp.route('/busan/')
def busan():
    return render_template('/main_tag/tag_html_1/main_html_1-4.html')

@bp.route('/jeju_island/')
def jeju_island():
    return render_template('/main_tag/tag_html_1/main_html_1-5.html')
