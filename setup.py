from setuptools import setup

setup(
    name='geolocation',
    packages=['geolocation'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_restful',
        'requests',
        'os',
    ],
)
