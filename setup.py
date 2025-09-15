from setuptools import setup
from pathlib import Path

setup(
    name='pyds-stubs',
    version='1.1.1.2',
    author='Niklas Kaaf',
    author_email='nkaaf@protonmail.com',
    description='Typing stubs for NVIDIA DeepStream Python Bindings',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/nkaaf/pyds-stubs',
    project_urls={
        'Bug Tracker': 'https://github.com/nkaaf/pyds-stubs/issues',
        'Releases': 'https://github.com/nkaaf/pyds-stubs/releases',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation',
        'Typing :: Stubs Only',
    ],
    keywords=['nvidia', 'deepstream', 'bindings', 'stubs'],
    license='Apache Software License',
    packages=['pyds-stubs'],
    package_dir={'': 'src'},
    package_data={'pyds-stubs': ['*.pyi']},
    python_requires='>=3.6,<3.7',
    install_requires=['numpy', 'PyGObject-stubs'],
    setup_requires=['setuptools==59.6.0', 'wheel==0.37.1', 'build==0.9.0'],
)
