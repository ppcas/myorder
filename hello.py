from flask import Flask, url_for
from imooc import route_imooc
from common.libs.UrlManger import UrlManger
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/mysql'
db = SQLAlchemy(app)

app.register_blueprint(route_imooc, url_prefix="/imooc")


@app.route('/')
def index():
    url = url_for('index')
    print(url)
    url_1 = UrlManger.buildstaticurl('/api')
    app.logger.error(url)
    app.logger.info(url_1)
    return "hello world"


@app.route("/api")
def hello_world():

    from sqlalchemy import text
    sql = text("SELECT * FROM user")
    result = db.engine.execute(sql)
    for row in result:
        app.logger.info(row)

    return "api hello"

@app.errorhandler(404)
def page_not_fonud(error):
    return "error This page does not exit",404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
