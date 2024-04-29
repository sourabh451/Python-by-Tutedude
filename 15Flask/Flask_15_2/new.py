# IMPORTING
from flask import Flask, render_template, request

# INTERACTION
web = Flask(__name__)

# MAPPING
@web.route('/')
@web.route('/register')

# INPUTS
def homepage():
    return render_template('register.html')

# MAPPING
@web.route("/confirmation", methods=['POST','GET'])
# INPUT
def register():
    if request.method == "POST":
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phone number')
        return render_template('confirm.html', name=n, city=c, phonenumber=p)

# MAIN
if __name__ == "__main__":
    web.run(debug=True)


