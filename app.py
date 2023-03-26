from flask import Flask    #imports flask web creator
from views import views


app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")   #access routes through slash


if __name__ == '__main__':
    app.run(debug=True, port=8000)  #any changes made means auto refresh