import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from utils.config import Config


logger = logging.getLogger(__name__)

def get_driver():
    """Initialize webdriver"""
    logger.info("Starting the Chrome browser...")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    print("Browser launched successfully") 
    return driver

def close_driver(driver):
    """Close the webdriver"""
    driver.quit()
    logger.info("Driver closed.")