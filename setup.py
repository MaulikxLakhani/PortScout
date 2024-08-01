from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Read the README file for the long description
with open('README.md') as f:
    long_description = f.read()

setup(
    name='PortScout',
    version='0.1.0',
    author='Maulik Lakhani',
    author_email='your.email@example.com',  # Replace with the author's email
    description='A high performance network port scanner.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MaulikxLakhani/PortScout',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'portscout=PortScout:main',
        ],
    },
)
