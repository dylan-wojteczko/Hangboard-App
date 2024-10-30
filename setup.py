from setuptools import setup, find_packages

setup(
    name="hangboard_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "numpy",
    ],
    entry_points={
        'console_scripts': [
            'hangboard=main:main',  # Assumes `main` function in `main.py`
        ],
    },
)
