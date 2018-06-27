from setuptools import setup

setup(
    name='booking',
    packages=['booking'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-wtf',
        'flask-login',
        'werkzeug',
        'wtforms',
        'Pillow',
        'pandas', 'fuzzywuzzy'
    ],
)
