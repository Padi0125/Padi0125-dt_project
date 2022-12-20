from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from dt import db
from dt.forms import UserCreateForm, UserLoginForm
from dt.models import Item

bp = Blueprint('item', __name__, url_prefix='/item')

@bp.route('/my_item/')
def item():
    item_list = Item.query.order_by(Item.itemname, Item.price, Item.my_user)
    return render_template('item/main_item.html', item_list=item_list)