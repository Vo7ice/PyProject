try:
	from setuptools import setup 
except ImportError:
	from distutils.core import setup

config = {
	'description':'My Project',
	'author': 'Vo7ice',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'Vo7ice@outlook.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['first'],
	'scripts': [],
	'name': 'first_project'
	}
	
setup(**config)