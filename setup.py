from os import path
import codecs
from setuptools import setup, find_packages

read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()

tests_require = [
    'Django>=1.2',
    'django_nose==1.0.1'
    'unittest2',
    'mock==0.7.2',
    'django-whatever>=0.2.3',
    'south==0.7.3'
]

setup(
    name='django-geoip',
    version='0.2.2',
    author='Ilya Baryshev',
    author_email='baryshev@gmail.com',
    packages=find_packages(exclude=("tests")),
    url='https://github.com/coagulant/django-geoip',
    license='MIT',
    description="App to figure out where your visitors are from by their IP address.",
    long_description=read(path.join(path.dirname(__file__), 'README.rst')),
    install_requires=[
        "django-appconf==0.4.1",
    ],
    tests_require=tests_require,
    test_suite = "runtests",
    extras_require={'test': tests_require},
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)