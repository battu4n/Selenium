from selenium import webdriver
import logging
logging.basicConfig(filename="D:/screenshots/test.log",format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")