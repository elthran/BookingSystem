from setuptools import setup

setup(
    name='booking',
    packages=['booking'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-JSON',
        'flask-sqlalchemy',
        'flask-wtf',
        'flask-login',
        'flask_mail',
        'werkzeug',
        'wtforms',
        'Pillow',
        'pandas',
        'fuzzywuzzy',
        'python-Levenshtein',
        'pytest'
    ],
)
