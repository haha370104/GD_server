from flask import Blueprint

drama_info_bp = Blueprint('drama_info', __name__)


@drama_info_bp.route('/search/')
def search():
    pass


@drama_info_bp.route('/drama_detail/')
def drama_detail():
    pass


@drama_info_bp.route('/drama_list/')
def drama_list():
    pass
