# from icav_tech_challenge.config import app
from flask_restful import Api,Resource
# from controllers.signin import Signin
# from controllers.books import BooksINFO
from flask import Flask,request
import os,re
import pandas as pd
import logging as info

app=Flask(__name__)


# set up  info logging to file - see previous section for more details
info.basicConfig(level=info.DEBUG,
                 format='%(asctime)s %(name)-12s %(levelname)-8s %(lineno)d %(message)s',
                 datefmt='%m-%d %H:%M',
                 filename='logger.log',
                 filemode='a')

# define a Handler which writes INFO messages or higher to the sys.stderr
console = info.StreamHandler()
console.setLevel(info.INFO)
# set a format which is simpler for console use
formatter = info.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
info.getLogger('').addHandler(console)

# Logger class
class Logger():
    # def __init__():
    #     pass
    def create_log(module: str, log: str) -> None:
        '''
        create success log from this method
        '''
        try:
            success_log = info.getLogger(module)
            success_log.info(log)
        except Exception as e:
            print(e)
            # create_error_log('logger_module', str(e))

    def create_error_log(module: str, log: str):
        '''
        create error log from this method
        '''
        try:
            error_log = info.getLogger(module)
            error_log.error(log)
        except Exception as e:
            print(e)


basedir = os.path.abspath(os.path.dirname(__file__))
user ={'user_name':'book_management@admin.com','password':'Welcome@123'}


class Signin(Resource):
    def __init__(self):
        pass

    # login call for the user
    def post(self):
        try:
            sign_in = request.get_json()
            print(sign_in)
            username = sign_in['username']
            password = sign_in['password']
            # user check
            if username =='':
                Logger.create_error_log("signin","username required")
                return({"success":False,"message": "username required"},500)
            if password =='':
                Logger.create_error_log("signin","password required")
                return({"success":False,"message": "password required"},500)
            if username==user['user_name']:
                
                #password check
                
                if password == user['password']:
                    return({"success":True,
                        "data": "logged in Book Management",
                        "message": f'Successfully logged in as {username}'},200)
                else:
                    Logger.create_error_log("signin",f"Entered invalid password")
                    return({"success":False,"message": "Invalid password"},500)
                
            else:
                Logger.create_error_log("signin",f"Entered invalid Username")
                return({"success":False,"message": "Invalid username"},500)
               
        except Exception as e:
            Logger.create_error_log("signin",str(e))
            return({"success":False,"message":str(e)},500)


class BooksINFO(Resource):
    def __init__(self):
        pass
    def get(self):
        """
        This method will return list of books info based of rows number passed in headers
        """
        try:
            rows = request.headers['rows']
            df = pd.read_csv(os.path.join(basedir,'books.csv'),header=0)
            if rows!='':
                df=df.head(int(rows))
            data=df.to_dict(orient='records')
            return({"success":True,"books":data})
        except ValueError as e:
            Logger.create_error_log("Booksinfo",str(e))
            return({"success":False,"error_message":str(e),"message":"please pass only numbers or empty string"},500)
        except KeyError as e:
            Logger.create_error_log("Booksinfo",str(e))
            return({"success":False,"error_message":str(e),"message":'please pass no of rows through headers'},500)



def create_app():
    api=Api(app)
    
    api.add_resource(Signin,'/api/signin')
    api.add_resource(BooksINFO,'/api/booksinfo')
    return app


if __name__ == "__main__":
    app=create_app()
    app.run(debug=True,host='0.0.0.0')
