import requests
from flask import jsonify, render_template_string

from db import get_db


def get_users():
    client, db = get_db()
    users = list(db.users.find({}, {'_id': False}))
    client.close()
    return jsonify(users)

def get_posts():
    client, db = get_db()
    posts = list(db.posts.find({}, {'_id': False}))
    client.close()
    return jsonify(posts)


def get_user_posts(user_id):
    client, db = get_db()
    posts = list(db.posts.find({"userId": user_id}, {'_id': False}))
    client.close()
    return jsonify(posts)


def home_page():  # put application's code here
    return render_template_string("""
    <h1>choose route</h1>
    <ul>
    <li><a href="/users/">users</a></li>
    <li><a href="/posts/">posts</a></li>
    </ul>
    """)


def seed(collection_name, api_url):
    client, db = get_db()
    collection = db[collection_name]
    if collection.count_documents({}) == 0:
        try:
            response = requests.get(api_url)  # השתמש ב-requests.get כאן
            data = response.json()
            collection.insert_many(data)
        except requests.exceptions.ConnectionError:
            print(f"אנא בדוק חיבור ל {api_url}")
            return
    client.close()