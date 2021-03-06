from setuptools import setup



setup(
    name = 'hello',
    version = '1.0',
    py_modules = ['hello'],
    install_requires = [
        'Click',
        'requests',
        'python-dotenv',
        'win10toast',
        'geocoder',
        'mysql-connector-python',
        'choice',
        'bcrypt'
    ],
    entry_points = '''
        [console_scripts]
        hello = hello:cli
    ''',
)


