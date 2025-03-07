# # config.py
# import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
#     SQLALCHEMY_DATABASE_URI = os.environ.get('jdbc:mysql://LAPTOP-A4M98RC9:3306/workspace_management') or 'mysql+pymysql://deepsiya:deepsiya19@localhost/workspace_management'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


    # config.py
# import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
#     SQLALCHEMY_DATABASE_URI = os.environ.get(
#         'DATABASE_URL',  'mysql+pymysql://deepsiya:deepsiya19@%/workspace_management' % 'localhost'
#     )

#     SQLALCHEMY_TRACK_MODIFICATIONS=False

# import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')

#     # Corrected MySQL connection URI
#     SQLALCHEMY_DATABASE_URI = os.environ.get(
#         'DATABASE_URL',
#         f'mysql+pymysql://deepsiya:deepsiya19@localhost/workspace_management'
#     )

#     SQLALCHEMY_TRACK_MODIFICATIONS = False

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')

    print("Attempting to connect to the database...")  # Before connection

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        f'mysql+pymysql://deepsiya:deepsiya19@localhost/workspace_management'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    print("Database connection URI configured.")  # After connection
