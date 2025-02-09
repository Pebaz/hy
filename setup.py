#!/usr/bin/env python

import os

import fastentrypoints  # Monkey-patches setuptools.
from pathlib import Path
from get_version import __version__
from setuptools import find_packages, setup
from setuptools.command.install import install
from setuptools.command.build_py import build_py

os.chdir(os.path.split(os.path.abspath(__file__))[0])

PKG = "hy"

long_description = """Hy is a Lisp dialect that's embedded in Python.
Since Hy transforms its Lisp code into Python abstract syntax tree (AST)
objects, you have the whole beautiful world of Python at your fingertips,
in Lisp form."""


class install(install):
    def run(self):
        super().run()
        import py_compile

        import hy  # for compile hooks

        for path in set(self.get_outputs()):
            if path.endswith(".hy"):
                py_compile.compile(
                    path,
                    invalidation_mode=py_compile.PycInvalidationMode.CHECKED_HASH,
                )


class bundle_pth_file(build_py):
    "Bundle hy_codec.pth file to support directly running Hy files with Python"

    def run(self):
        "https://stackoverflow.com/a/71137790/6509967"
        super().run()

        destination_in_wheel = 'hy_codec.pth'
        location_in_source_tree = f'{PKG}/hy_codec.pth'

        out_file = Path(self.build_lib) / destination_in_wheel
        self.copy_file(location_in_source_tree, out_file, preserve_mode=0)


# both setup_requires and install_requires
# since we need to compile .hy files during setup
requires = [
    "funcparserlib ~= 1.0",
    "colorama",
    'astor>=0.8 ; python_version < "3.9"',
]

setup(
    name=PKG,
    version=__version__,
    setup_requires=["wheel"] + requires,
    install_requires=requires,
    python_requires=">= 3.7, < 3.12",
    entry_points={
        "console_scripts": [
            "hy = hy.cmdline:hy_main",
            "hy3 = hy.cmdline:hy_main",
            "hyc = hy.cmdline:hyc_main",
            "hyc3 = hy.cmdline:hyc_main",
            "hy2py = hy.cmdline:hy2py_main",
            "hy2py3 = hy.cmdline:hy2py_main",
        ]
    },
    packages=find_packages(exclude=["tests*"]),
    package_data={
        "": ["*.hy"],
    },
    data_files=[("get_version", ["get_version.py"])],
    author="Paul Tagliamonte",
    author_email="tag@pault.ag",
    long_description=long_description,
    description="A Lisp dialect embedded in Python",
    license="Expat",
    url="http://hylang.org/",
    platforms=["any"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: DFSG approved",
        "License :: OSI Approved :: MIT License",  # Really "Expat". Ugh.
        "Operating System :: OS Independent",
        "Programming Language :: Lisp",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Libraries",
    ],
    project_urls={
        "Documentation": "https://docs.hylang.org/",
        "Source": "https://github.com/hylang/hy",
    },
    cmdclass={
        "install": install,
        "build_py": bundle_pth_file
    },
)
