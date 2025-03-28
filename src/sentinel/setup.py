from setuptools import setup, find_packages

setup(
    name="sentinel",
    version="0.1.0",
    description="API Monitoring & Load Testing CLI Tool",
    author="Jason Alan Smith",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "sentinel=sentinel.cli:main"
        ]
    },
    python_requires=">=3.8",
)