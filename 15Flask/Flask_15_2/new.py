# IMPORTING
from flask import Flask

# INTERACTION
web = Flask(__name__)

# MAPPING
@web.route('/')
@web.route('/home')

# INPUTS
def home():
    return "Welcome"

# MAIN
if __name__ == "__main__":
    web.run(debug=True)
