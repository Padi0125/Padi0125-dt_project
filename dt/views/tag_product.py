from flask import Blueprint, url_for, render_template
bp = Blueprint('product',__name__,url_prefix='/product')

@bp.route('/product1/')
def product1():
    return render_template('/main_tag/tag_html_4/main_tag_4-1.html')

@bp.route('/product2/')
def product2():
    return render_template('/main_tag/tag_html_4/main_tag_4-2.html')

@bp.route('/product3/')
def product3():
    return render_template('/main_tag/tag_html_4/main_tag_4-3.html')

@bp.route('/product4/')
def product4():
    return render_template('/main_tag/tag_html_4/main_tag_4-4.html')

@bp.route('/product5/')
def product5():
    return render_template('/main_tag/tag_html_4/main_tag_4-5.html')
