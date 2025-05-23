import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', "http://localhost:3000").split(',')
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')

    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
    CONTACT_SHEET_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'contact_sheets')
    SCATTER_DATA_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'scatter_plots_data')

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(CONTACT_SHEET_FOLDER, exist_ok=True)
    os.makedirs(SCATTER_DATA_FOLDER, exist_ok=True)

    CONTACT_SHEET_IMAGES_PER_CLUSTER = 9
    CONTACT_SHEET_GRID_SIZE = (3, 3)
    CONTACT_SHEET_THUMBNAIL_SIZE = (100, 100)
    CONTACT_SHEET_OUTPUT_FORMAT = 'JPEG'
    
    MAX_SCATTER_PLOT_POINTS = int(os.getenv('MAX_SCATTER_PLOT_POINTS', '10000'))