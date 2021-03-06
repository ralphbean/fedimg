#!/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup

setup(
    name='fedimg',
    version='0.0.1',
    description='Service to automatically upload built Fedora images \
                    to internal and external cloud providers.',
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU Affero General Public License \
            v3 or later (AGPLv3+)",
    ],
    keywords='python Fedora cloud image uploader',
    author='David Gay',
    author_email='oddshocks@riseup.net',
    url='https://github.com/oddshocks/fedimg',
    license='AGPLv3+',
    include_package_data=True,
    zip_safe=False,
    install_requires=["fedmsg",
                      "apache-libcloud"],
    packages=[],
    entry_points="""
    [moksha.consumer]
    kojiconsumer = fedimg.consumers:KojiConsumer
    """,
)
