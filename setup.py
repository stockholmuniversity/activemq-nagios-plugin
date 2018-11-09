#!/usr/bin/env python2
# vim: set fileencoding=utf-8
import sys
from setuptools import setup, find_packages

version = "0.7.2"

setup(
    name="activemq-nagios-plugin",
    version=version,
    description="Monitor Apache ActiveMQ's health, queuesizes and subscribers",
    long_description=open("README.md").read(),
    author="Thomas Bayer <bayer@predic8.de>",
    url="https://github.com/predic8/activemq-nagios-plugin",
    license="Apache License 2.0",
    scripts=['check_activemq.py'],
    install_requires=open('requirements.txt').readlines(),
)
