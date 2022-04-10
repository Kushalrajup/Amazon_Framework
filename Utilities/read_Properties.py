#This utility file used to get the data from config.ini file
import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURl():
        url=config.get('common data','baseURL')
        return url
    @staticmethod
    def getUsername():
        user=config.get('common data','username')
        return user
    @staticmethod
    def getPasssword():
        passkey=config.get('common data','password')
        return passkey
