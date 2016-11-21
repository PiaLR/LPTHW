try:
    from setuptools import setuptools
except ImportError:
    from distutil.core import setup

config = {
    'description': 'My Project',
    'author': 'Pia Roepke',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'pia-luisa.roepke@stud.leuphana.de',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts' [],
    'name': 'projectname'
}

setup(**config)
