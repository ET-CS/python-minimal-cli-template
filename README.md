# python-minimal-cli-template

Minimal template for a python based cli app

It includes the minimum necessary for you to create a python CLI with `setup.py` and `setup.cfg`.

This project was inspired by https://github.com/AnthonyBloomer/python-cli-template 
While using more recent up-to-date way of doing things. 

## Usage

While there a lot of ways to build, install and deploy this app.

The simple quickstart (after you clone this repo) would be:

```commandline
python setup.py install
```

and then run the cli:
```commandline
app
```

You'd probably later want a builder, such as [PyPA](https://pypa-build.readthedocs.io/en/latest/index.html) build. read more [here](https://setuptools.pypa.io/en/latest/userguide/quickstart.html#basic-use)

## setup.cfg

The bread and butter of this template is the `setup.cfg` file.
Python have gone a long way from distutils to setuptools, and you can find a lot
of examples and tutorials out there for creating a `setup.py` file for your project.

Though, today is considered best practice to use `setup.cfg` instead of `setup.py`
Read more here: https://setuptools.pypa.io/en/latest/userguide/quickstart.html#transitioning-from-setup-py-to-setup-cfg

## What you have

* A very bare minimal `setup.cfg` to create an installable python cli app.
* setup.py to support development mode.
* a simple cli module using argparse that does anything special.
* `pyproject.toml` which declares you want to use setuptools to package your project.
* A VERY basic .gitignore (you can get more complete version [here](https://github.com/github/gitignore/blob/master/Python.gitignore))

## What you DON'T have

* requirements.txt, Pipfile or any other package management configuration. No external libraries
* pre-commit configuration (git hooks)
* actual cli application that does anything important...