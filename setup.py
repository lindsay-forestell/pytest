import setuptools

# Parse the version
with open("pytest/__init__.py", "r") as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            break

# Get the long description from the relevant file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name='pytest',
    version=version,
    author='Lindsay Forestell',
    author_email='lindsay.forestell@gmail.com',
    description='Testing creating and maintenance of python packages on GitHub',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lindsay-forestell/pytest',
    project_urls={
        'Bug Tracker': 'https://github.com/lindsay-forestell/pytest/issues'
    },
    license='Apache 2.0',
    packages=['pytest'],
    install_requires=['pandas', 'numpy']
)
