import os

from setuptools import setup

data_files = [
    ('man/man1', ['man/man1/logview.1'])
]

if os.access('/etc/bash_completion.d', os.W_OK | os.X_OK):
    data_files.append(('/etc/bash_completion.d', ['bash_completion/logview']))

config = {
    'name': 'logview',
    'description': 'logview - refer current and archived log files using shortcuts',
    'author': 'Thorsten Huhn',
    'url': '',
    'download_url': '',
    'author_email': 'thorstenhuhn@users.noreply.github.com',
    'version': '0.1.3',
    'install_requires': [
        'pyyaml',
    ],
    'scripts': [ 'logview' ],
    'data_files': data_files,
}

setup(**config)

