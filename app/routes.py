from flask import render_template

from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('templates/index.html', title='Home', user=user)

if __name__ == "__main__":
    app.run(debug=True)
