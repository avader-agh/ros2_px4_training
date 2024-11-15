from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'simple_flight'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='developer',
    maintainer_email='mietla@student.agh.edu.pl',
    description='Package for controlling a drone in a simple flight scenario',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'square_flight = simple_flight.square_flight:main',
        ],
    },
)
