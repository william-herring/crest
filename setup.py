from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="Crest",
    version="1.0.0",
    description="A web framework designed for simplicity and efficiency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/william-herring/crest",
    author="William Herring",
    author_email="william.herring.au@gmail.com",

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        'License :: OSI Approved :: BSD 3-Clause "New" or "Revised" License',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],

    keywords="web, framework, python, crest",
    package_dir={"": "crest"},
    packages=find_packages(where="crest"),
    python_requires=">=3.7, <4",
    install_requires=[
        'typer>=0.7.0'
    ],

    project_urls={
        "Bug Reports": "https://github.com/william-herring/crest/issues",
        "Source": "https://github.com/william-herring/crest/",
    },
)