from icav_tech_challenge.config import app
from flask_restful import Api
from icav_tech_challenge.controllers.signin import Signin
from icav_tech_challenge.controllers.books import BooksINFO


def create_app():
    api=Api(app)
    
    api.add_resource(Signin,'/api/signin')
    api.add_resource(BooksINFO,'/api/booksinfo')
    return app


if __name__ == "__main__":
    app=create_app()
    app.run(debug=True,host='0.0.0.0')
