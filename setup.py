from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Read the README file for the long description
with open('README.md') as f:
    long_description = f.read()

setup(
    name='PortScout',
    version='1.0.2',
    author='Maulik Lakhani',
    author_email='maulik.lakhanix@gmail.com',
    description='A high-performance and efficient network port scanner for common ports. ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MaulikxLakhani/PortScout',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'portscout=PortScout:main',
        ],
    },
)
