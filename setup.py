from setuptools import setup, find_packages

setup(
    name='timer',
    version='1.0',
    description='Simple Timer implementation.',
    url='https://github.com/benikm91/timer-py',
    author='Benjamin Meyer',
    author_email='benjamin.meyer@fhnw.ch',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    python_requires='>=3',
    include_package_data=True,
    install_requires=[
    ],
)