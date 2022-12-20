from flask import Blueprint, url_for, render_template
bp = Blueprint('overseas',__name__,url_prefix='/overseas')

@bp.route('/japan/')
def japan():
    return render_template('/main_tag/tag_html_2/main_html_2-1.html')

@bp.route('/us/')
def us():
    return render_template('/main_tag/tag_html_2/main_html_2-2.html')

@bp.route('/uk/')
def uk():
    return render_template('/main_tag/tag_html_2/main_html_2-3.html')

@bp.route('/germany/')
def germany():
    return render_template('/main_tag/tag_html_2/main_html_2-4.html')

@bp.route('/vietnam/')
def vietnam():
    return render_template('/main_tag/tag_html_2/main_html_2-5.html')
