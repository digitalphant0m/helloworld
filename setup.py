import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helloworld",
    version="0.1",
    author="digitalphant0m",
    author_email="author@example.com",
    description="A hello world",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/digtialphant0m/helloworld",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
