from flask import Flask
from bp import bp_crud

app = Flask(__name__)

app.register_blueprint(bp_crud)

if __name__ == '__main__':
    app.run(debug=True)
