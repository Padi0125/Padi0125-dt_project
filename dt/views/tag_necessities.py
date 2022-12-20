from flask import Blueprint, url_for, render_template
bp = Blueprint('necessities',__name__,url_prefix='/necessities')

@bp.route('/necessities_product/')
def necessities_product1():
    return render_template('/main_tag/main_html_5.html')