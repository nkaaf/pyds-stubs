# Typing stubs for NVIDIA DeepStream Python Bindings

![PyPI - Status](https://img.shields.io/pypi/status/pyds-stubs?style=for-the-badge)
![PyPI - Types](https://img.shields.io/pypi/types/pyds-stubs?style=for-the-badge)

> [!NOTE]
> This is the main/production branch of this repository. For more information about the different
> releases go to the release tab or switch the branch to "X.Y.Z-stubs".

This project provides type stubs for [pyds](https://github.com/NVIDIA-AI-IOT/deepstream_python_apps)
to improve the support of these important bindings in IDEs.

With the usage of this project, you agree to the license terms, found in the [License](#license)
chapter. This project is not affiliated with NVIDIA or the authors and maintainer of
the [pyds](https://github.com/NVIDIA-AI-IOT/deepstream_python_apps) repository. It is the result of
the need for type hints for a simpler and more stable implementation of DeepStream pipelines in
Python.

## Index

* [Installation](#installation)
    * [Versioning](#versioning)
* [Usage](#usage)
* [License](#license)
* [Appendix](#appendix)
    * [Links](#links)
    * [Notice for NVIDIA](#notice-for-nvidia)

## Installation

This library can be easily installed with pip.

### Versioning

The stub versions matches the versions of pyds. For example, stub version `1.1.8` fits to pyds
version
`1.1.8`. If any fix has to be applied, the fourth position would be incremented. So the first fix of
`1.1.8` results in `1.1.8.1`.

Please pin your version directly or limit it upper-wise like:

`pyds-stubs>=1.1.8,<1.1.9`

## Usage

There is no magic, just only import pyds as you would normally do. This package is intended to be
used during the development and can be omitted in runtime environments.

## License

This project is published
under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) - please comply
with it, if you use/modify/distribute it. The license can be found in "LICENSE".

## Appendix

### Links

* [Project Home](https://github.com/nkaaf/pyds-stubs)
* [pyds - NVIDIA DeepStream Python Bindings](https://github.com/NVIDIA-AI-IOT/deepstream_python_apps)
* [pybind11-stubgen](https://github.com/sizmailov/pybind11-stubgen)

### Notice for NVIDIA

I recently (Jun, 2025) saw
a [discussion](https://forums.developer.nvidia.com/t/feature-request-add-python-stubs-to-pyds-library/333191/4)
on your forum. If there is any official stub support by NVIDIA, this project will be deprecated and
publicly archived. I hope to hear from you ;)
