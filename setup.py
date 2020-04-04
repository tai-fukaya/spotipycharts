from setuptools import setup, find_packages


requires = [
    "beautifulsoup4>=4.8.2",
    "lxml>=4.5.0",
    "requests>=2.22.0",
]


setup(
    name='spotipycharts',
    version='0.1',
    description='Download csv file in spotifycharts',
    url='https://github.com/tai-fukaya/spotipycharts',
    author='Tai Fukaya',
    author_email='taifuun.in@gmail.com',
    license='MIT',
    keywords='spotifycharts',
    packages=[
        "spotipycharts",
    ],
    install_requires=requires,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)