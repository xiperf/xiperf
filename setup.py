#!/usr/bin/env python3
""" X iperf
"""

import setuptools

setuptools.setup(
    name='xiperf',
    version='0.0.1.dev1',
    description='Graphical Iperf',
    url='https://github.com/xiperf/xiperf',
    author='Dylan Scott Grafmyre',
    author_email='dylan.grafmyre@gmail.com',
    classifiers=[
       'Development Status :: 2 - Pre-Alpha',
       'Intended Audience :: Developers',
       'Intended Audience :: End Users/Desktop',
       'Intended Audience :: Information Technology',
       'Intended Audience :: Telecommunications Industry',
       'Topic :: Internet',
       'Topic :: System :: Networking',
       'Topic :: Utilities',
       'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
       'License :: OSI Approved :: BSD License',
       'Programming Language :: Python :: 3',
    ],
    keywords='iperf xiperf',
    py_modules='xiperf',
    entry_points={
        'gui_scripts': [
            'xiperf = xiperf:main',
        ],
    },
)

