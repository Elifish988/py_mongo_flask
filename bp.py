from flask import Blueprint

import servis

bp_crud = Blueprint('bp_crud', __name__)



base_url = 'https://jsonplaceholder.typicode.com/'

servis.seed('users', f'{base_url}users')
servis.seed('posts', f'{base_url}posts')

@bp_crud.route('/users/', methods=['GET'])
def get_users():
    return servis.get_users()


@bp_crud.route('/posts/', methods=['GET'])
def get_posts():
    return  servis.get_posts()


@bp_crud.route('/posts/<int:user_id>', methods=['GET'])
def get_user_posts(user_id):
    return servis.get_user_posts(user_id)


@bp_crud.route('/')
def home_page():  # put application's code here
    return servis.home_page()