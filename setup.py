from setuptools import setup

setup(
  name = 'media',
  packages = ['media','media.migrations','media.management'],
  version = '0.1',
  description = 'Versitle django image store',
  author = 'Chris Cauley',
  author_email = 'chris@lablackey.com',
  url = 'https://github.com/chriscauley/django-unrest-media',
  keywords = ['images','django','unrest'],
  license = 'GPL',
  include_package_data = True,
)
