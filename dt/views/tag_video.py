from flask import Blueprint, url_for, render_template
bp = Blueprint('video',__name__,url_prefix='/video')

@bp.route('/play_video/')
def play_video():
    return render_template('/main_tag/main_html_3.html')