#!/usr/bin/env python
import os
import stat
import sys
import platform
from setuptools import setup

VERSION = '1.0.2'

with open('README.md') as f:
    readme = f.read()

executable_stat = os.stat('lib/skopeo_linux')
os.chmod('lib/skopeo_linux', executable_stat.st_mode | stat.S_IEXEC)

executable_stat = os.stat('lib/skopeo_darwin')
os.chmod('lib/skopeo_darwin', executable_stat.st_mode | stat.S_IEXEC)

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None

setup(
    name='skopeo-bin',
    version=VERSION,
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Epiphany Team',
    author_email='',
    url='https://github.com/epiphany-platform/skopeo-bin',
    license='Apache License Version 2.0',
    py_modules=['skopeo'],
    data_files=[
        ('lib', ['lib/skopeo_linux', 'lib/skopeo_darwin']),
    ],
    entry_points={
        'console_scripts': [
            'skopeo = skopeo:main',
        ]
    },
)
