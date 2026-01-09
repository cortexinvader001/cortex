from setuptools import setup, find_packages

setup(
    name="cortex",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.3.2",
        "requests>=2.32.0",
        "python-dotenv>=1.0.0"
    ],
    python_requires=">=3.10",
    url="https://github.com/cortexinvader/cortex",
    author="CortexInvader",
    description="Lightweight Facebook Graph API wrapper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
)