
import os

class Config:
    """Global setting"""
    BASE_URL =  os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    BROWSER = os.getenv("BROWSER", "chrome")
    USERNAME = os.getenv("USERNAME", "Admin")
    PASSWORD = os.getenv("PASSWORD", "admin123")
    TIMEOUT = int(os.getenv("TIMEOUT",10))

class ProdConfig(Config):
    """Production setting"""