#This file generates logs
#this code is same for every project
import logging

class LogGen:
    @staticmethod
    def loggen():
      logging.basicConfig(filename=".\\Logs\\automatomation.log",
                           format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%s %p')
      logger=logging.getLogger()
      logger.setLevel(logging.INFO)
      return logger