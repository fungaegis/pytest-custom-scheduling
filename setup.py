from setuptools import setup

"""
author: fungaegis
github: https://github.com/fungaegis/pytest-custom-scheduling
"""
with open("./README.rst", "r") as readme:
    long_description = readme.read()
setup(
    name='pytest-custom-scheduling',
    url='https://github.com/fungaegis/pytest-custom-scheduling',
    version='1.1',
    author="fungaegis",
    author_email="fungaegis@gmail.com",
    description='Custom grouping for pytest-xdist, rename test cases name and test cases nodeid, support allure report',
    long_description=long_description,
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.7',
    ],
    license='MIT License',
    py_modules=['pytest_custom_scheduling'],
    keywords=[
        'pytest', 'py.test', 'pytest_custom_scheduling', 'concurrency', 'xdist', 'pytest-xdist'
    ],

    install_requires=[
        'pytest',
        'pytest-xdist'
    ],
    entry_points={
        'pytest11': [
            'custom_scheduling = pytest_custom_scheduling',
        ]
    }
)
