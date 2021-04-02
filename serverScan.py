import socket 
import ssl 
from datetime import datetime 
import pickle
import subprocess
import platform

class Server():
    def __init__(self, name, port, connection, priority):
        self.name = name 
        self.port = port 
        self.connection = connection.lower()
        self.priority = priority.lower()
        self.history = []
        self.alert = False 

    def check_connetion(self):
        msg = ""
        success = False
        now = datetime.now()
        
