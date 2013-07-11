#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(packages=['create_node'],
                             package_dir={'': 'src'},
                             scripts=['scripts/kinect_breaker_enabler.py']
#                             requires=['roslib', 'rospy']
)

setup(**d)