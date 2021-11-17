import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='gitb',
    version='0.0.1',
    author='Daniel Koves',
    author_email='daniel.koves@icloud.com',
    description='Interactive Git Branch Selector',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/koeves/gitb',
    project_urls = { },
    license='MIT',
    packages=['gitb'],
    install_requires=['simple_term_menu'],
)