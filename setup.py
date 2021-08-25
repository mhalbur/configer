from setuptools import setup, find_packages


setup(
    name='easyfig',
    version='0.1.0',
    packages=find_packages(include=['easyfig', 'easyfig.*']),
    install_requires=[
        'PyYAML',
        'python-gnupg',
        'cryptography',
        'Click'
    ],
    entry_points={
        'console_scripts': [
            'easyfig = easyfig.command_line:main'
        ],
    }
)
