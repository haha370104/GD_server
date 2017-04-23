from flask import Blueprint

mobile_bp = Blueprint('mobile', __name__)


@mobile_bp.route('/index/')
def index():
    pass


@mobile_bp.route('/drama_list/')
def drama_list():
    pass


@mobile_bp.route('/drama_detail/')
def drama_detail():
    pass
