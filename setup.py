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
        'werkzeug',
        'wtforms',
        'Pillow',
        'pandas',
        'fuzzywuzzy',
        'python-Levenshtein'
    ],
)
