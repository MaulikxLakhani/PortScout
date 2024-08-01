from setuptools import setup, find_packages

# Read the content of the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="PortScout",
    version="0.1.0",
    author="Maulik Lakhani",
    author_email="maulik@example.com",  # Update this to the author's email address
    description="A simple port scanning tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaulikxLakhani/PortScout",
    packages=find_packages(),
    py_modules=["PortScout"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your project's dependencies here.
        # You can add dependencies by listing them like this:
        # 'requests>=2.25.1',
        # 'numpy>=1.19.5',
      argparse,
      tabulate,
    ],
    entry_points={
        'console_scripts': [
            'portscout=PortScout:main',
        ],
    },
)
