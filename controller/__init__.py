from controller.api.user_info import user_bp
from controller.api.drama import drama_info_bp
from controller.api.favorite import favorite_bp
from controller.api.post import post_bp
from controller.api.mobile import mobile_bp

blue_prints = []
blue_prints.append((user_bp, '/api/user_info'))
blue_prints.append((drama_info_bp, '/api/drama_info'))
blue_prints.append((favorite_bp, '/api/favorite'))
blue_prints.append((post_bp, '/api/post'))
blue_prints.append((mobile_bp, '/api/mobile'))
