from setuptools import setup, find_packages

setup(
    name='my-stripe-extension',
    version='0.1.0',
    author='awadbs',
    author_email='awadspam@gmail.com',
    packages=find_packages(),
    install_requires=[
        'stripe',
        'json'
    ],
)
