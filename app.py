from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/features')
def features_page():
    return render_template('features.html')


@app.route('/prices')
def prices_page():
    return render_template('prices.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
