from paul import __appname__, __version__
from setuptools import setup


long_description = ""

setup(
    name=__appname__,
    version=__version__,
    scripts=[],
    packages=[
        'paul',
    ],
    author="Leo Cavaille",
    author_email="leo@cavaille.net",
    long_description=long_description,
    description='paul',
    license="Expat",
    url="http://deb.io/",
    platforms=['any'],
    entry_points={
        'console_scripts': [
            'paul = paul.client:main',
        ],
    }
)
