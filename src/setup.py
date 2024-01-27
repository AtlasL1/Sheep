from setuptools import setup, find_packages

setup(
    name='sheep',
    version='0.0.0',
    author='Atlas',
    description='Effective Notebooking with Sheep.',
    url='https://github.com/AtlasL1/Sheep',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: EPL License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
