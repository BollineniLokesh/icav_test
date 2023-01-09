from flask import Flask
import os


app=Flask(__name__)

user ={'user_name':'book_management@admin.com','password':'Welcome@123'}
basedir = os.path.abspath(os.path.dirname(__file__))