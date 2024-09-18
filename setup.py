from setuptools import setup, find_packages

setup(
    name="pythoyo",  
    version="0.1.0",  
    description="A fun and whimsical UyU programming language written in python", 
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",
    author="Rajdeep Chatterjee",  
    author_email="rc9775295@gmail.com",  
    url="https://github.com/RajChat-hub/pythOyO",  
    packages=find_packages(),  
    entry_points={
        "console_scripts": [
            "pythoyo=pythoyo.pythoyo:main",  
            "shyell=pythoyo.shyell:main",  
        ],
    },
    install_requires=[],  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
)
