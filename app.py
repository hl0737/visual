from flask import Flask
from flask import render_template as rt

app = Flask(__name__)


@app.route('/')
def hello_world():
    return rt('./index.html')


@app.route('/team/<path:team_name>', methods=['GET'])
def get_team_name(team_name):
    return rt('./team_page.html', team_name=team_name)


if __name__ == '__main__':
    app.run()
