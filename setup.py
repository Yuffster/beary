from setuptools import setup, find_packages

VERSION = '0.0.1'

config = {
    'description': "🐻 Terminal library on top of bearlibterminal.",
    'author': "Michelle Steigerwalt",
    'author_email': "msteigerwalt@gmail.com",
    'url': 'http://github.com/Yuffster/beary',
    'version': VERSION,
    'packages': find_packages(exclude=["tests"]),
    'name': 'beary',
    'zip_safe': True,
    'install_requires':[
        'bearlibterminal',
    ]
}

setup(**config)
