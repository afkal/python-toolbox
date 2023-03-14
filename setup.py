import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-toolbox',
    version='0.0.1',
    author='Timo Laitila',
    author_email='timo@proactor.dev',
    description='Python toolbox for common functions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/afkal/python-toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/afkal/python-toolbox/issues"
    },
    license='MIT',
    packages=['toolbox'],
    #install_requires=['requests'],
)