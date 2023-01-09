from flask_restful import Resource
from icav_tech_challenge.config import user
from flask import request
from icav_tech_challenge.logger import Logger

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


