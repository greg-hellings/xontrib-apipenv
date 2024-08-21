from setuptools import setup

setup(
    name='xontrib-apipenv',
    version='0.5.0',
    url='https://github.com/greg-hellings/xonsh-apipenv',
    license='MIT',
    author='Greg Hellings',
    author_email='greg.hellings@gmail.com',
    description='Auto activate a Pipenv virtual environment',
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    install_requires=['pipenv>=2022'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Desktop Environment',
        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',
    ]
)
