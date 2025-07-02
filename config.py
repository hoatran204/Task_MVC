import mysql.connector
import gspread
from google.oauth2.service_account import Credentials
import json
import sys
import io
import os
from mysql.connector import Error

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="task_management"
    )