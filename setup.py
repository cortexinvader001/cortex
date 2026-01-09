from setuptools import setup, find_packages

setup(
    name="cortex",
    version="0.1.0",
    description="Lightweight Facebook Graph API wrapper",
    author="CortexInvader",
    author_email="cortexinvader@gmail.com",
    url="https://github.com/cortexinvader001/cortex",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        "Flask>=2.3.2",
        "requests>=2.32.0",
        "python-dotenv>=1.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
