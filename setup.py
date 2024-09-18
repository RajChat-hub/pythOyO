from setuptools import setup, find_packages

setup(
    name="pythOyO",  # Package name
    version="0.1.0",  # Initial version
    author="Rajdeep Chatterjee",  # my name
    author_email="rc9775295@gmail.com",  # my email
    description="A fun and whimsical UyU programming language written in python",  # Short description
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RajChat-hub/pythOyO",  # my GitHub repo
    packages=find_packages(),
    py_modules=['pythoyo', 'shyell', 'shÿell', 'styings_with_ayyows'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
