from flask_restful import Resource
from flask import request
from icav_tech_challenge.config import basedir
import os,re
import pandas as pd
from icav_tech_challenge.logger import Logger

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
        




