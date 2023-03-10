import csv

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


# @app.route("/<string:page_name>")
# def html_page(page_name: Any):
#   return render_template('page_name')
# url_for('static', filename='main.css')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as csvfile:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        csv_writer = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, name, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('/thankyou.html')  # "sent...thank you I'll be in touch!!"
    else:
        return "Oops! :( Something went wrong please try again!."
