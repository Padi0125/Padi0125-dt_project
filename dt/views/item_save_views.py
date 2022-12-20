from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash

from dt import db
from dt.models import User,Item

bp = Blueprint('items', __name__, url_prefix='/items')

@bp.route('/item_save_1/', methods=['POST'])
def item_save_1():
    it = Item(my_user=g.user.username,
              itemname = '란체티 14032 28인치 수화물 대형 여행용캐리어 여행가방 케리어',
              price='89,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/main_html_5.html')

@bp.route('/item_save_2/', methods=['POST'])
def item_save_2():
    it = Item(my_user=g.user.username,
              itemname = '마일드 썬 프로텍션 40ml',
              price='28,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/main_html_5.html')

@bp.route('/item_save_3/', methods=['POST'])
def item_save_3():
    it = Item(my_user=g.user.username,
              itemname = '여행용 응급 세트',
              price='60,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/main_html_5.html')

@bp.route('/item_save_4/', methods=['POST'])
def item_save_4():
    it = Item(my_user=g.user.username,
              itemname = '일회용 우비',
              price='20'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/main_html_5.html')

@bp.route('/item_save_5/', methods=['POST'])
def item_save_5():
    it = Item(my_user=g.user.username,
              itemname = '서울 패키지(1박 2일 서울 패키지)',
              price='1,000,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/tag_html_4/main_tag_4-1.html')

@bp.route('/item_save_6/', methods=['POST'])
def item_save_6():
    it = Item(my_user=g.user.username,
              itemname = '부산 패키지(1박 2일 부산 패키지)',
              price='1,000,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/tag_html_4/main_tag_4-1.html')


@bp.route('/item_save_7/', methods=['POST'])
def item_save_7():
    it = Item(my_user=g.user.username,
              itemname = '일본 패키지(2박 3일 일본 패키지)',
              price='2,000,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/tag_html_4/main_tag_4-2.html')

@bp.route('/item_save_8/', methods=['POST'])
def item_save_8():
    it = Item(my_user=g.user.username,
              itemname = '미국 패키지(2박 3일 미국 패키지)',
              price='2,000,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/tag_html_4/main_tag_4-2.html')


@bp.route('/item_save_9/', methods=['POST'])
def item_save_9():
    it = Item(my_user=g.user.username,
              itemname = '영국 패키지(3박 4일 영국 패키지)',
              price='3,000,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/tag_html_4/main_tag_4-3.html')

@bp.route('/item_save_10/', methods=['POST'])
def item_save_10():
    it = Item(my_user=g.user.username,
              itemname = '독일 패키지(3박 4일 독일 패키지)',
              price='3,000,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/tag_html_4/main_tag_4-3.html')



@bp.route('/item_save_11/', methods=['POST'])
def item_save_11():
    it = Item(my_user=g.user.username,
              itemname = '인천 패키지(4박 5일 인천 패키지)',
              price='4,000,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/tag_html_4/main_tag_4-4.html')

@bp.route('/item_save_12/', methods=['POST'])
def item_save_12():
    it = Item(my_user=g.user.username,
              itemname = '전주 패키지(4박 5일 전주 패키지)',
              price='4,000,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/tag_html_4/main_tag_4-4.html')

@bp.route('/item_save_13/', methods=['POST'])
def item_save_13():
    it = Item(my_user=g.user.username,
              itemname = '제주도 패키지(5박이상 제주도 패키지)',
              price='5,000,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/tag_html_4/main_tag_4-5.html')

@bp.route('/item_save_14/', methods=['POST'])
def item_save_14():
    it = Item(my_user=g.user.username,
              itemname = '베트남 패키지(5박이상 베트남 패키지)',
              price='5,000,000'
              )
    db.session.add(it)
    db.session.commit()
    return render_template('main_tag/tag_html_4/main_tag_4-5.html')