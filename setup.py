import setuptools

with open("README.md", 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pytest',
    version='1.0.0',
    author='Lindsay Forestell',
    author_email='lindsay.forestell@gmail.com',
    description='Testing creating and maintenance of python packages on GitHub',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lindsay-forestell/pytest',
    project_urls = {
        'Bug Tracker': 'https://github.com/lindsay-forestell/pytest/issues'
    },
    license='Apache 2.0',
    packages=['pytest'],
    install_requires=['pandas', 'numpy']
)