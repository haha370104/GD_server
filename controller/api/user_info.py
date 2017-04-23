from flask import Blueprint, request

user_bp = Blueprint('user', __name__)


@user_bp.route('/login/', methods=['POST'])
def login():
    phone_num = request.values.get('phoneNum')
    password = request.values.get('password')


@user_bp.route('/register/', methods=['POST'])
def register():
    pass


@user_bp.route('/get_sms_code/', methods=['GET'])
def get_sms_code():
    pass


@user_bp.route('/forget_code/', methods=['POST'])
def forget_code():
    pass


@user_bp.route('/logout/')
def logout():
    pass
