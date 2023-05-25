from flask import Flask
from model.Modles import db
from model.Modles import Store
import os

app = Flask(__name__)


# adding configuration for using a sqlite database
# 'mysql+pymysql://root:@localhost/product'
# postgres://smchatbotdatabase_user:YLSGBHn1SnRKmRKRpiY2ZImMjdb0CciZ@dpg-chn735vdvk4n43a6131g-a.oregon-postgres.render.com/smchatbotdatabase
# set DATABASE_URL=postgresql://smchatbotdatabase_user:YLSGBHn1SnRKmRKRpiY2ZImMjdb0CciZ@dpg-chn735vdvk4n43a6131g-a.oregon-postgres.render.com/smchatbotdatabase
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.rout('/', methods=['GET'])
def main():
    return "hi welcome :)"


@app.route('/test', methods=['GET'])
def test():
    print("it is work at lest")
    try:
        s = Store.query.filter_by(name='ss').first()
        return s.name
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.init_app(app)
        db.create_all()
    app.run(debug= True)
