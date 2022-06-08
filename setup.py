from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long = (here / 'README.md').read_text(encoding='utf-8')
short = long.split('\n')[1]

version = (0, 1, 0)

setup(
    name='xivpy',
    version='.'.join(map(str, version)),
    description=short,
    long_description=long,
    long_description_content_type='text/markdown',
    url='https://github.com/HazelTheWitch/XIVPy',
    author='Hazel Rella',
    author_email='hazelrella11@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only'
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.10, <4',
    install_requires=[
        'aiohttp'
    ]
)
